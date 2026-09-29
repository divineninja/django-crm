from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import Group


@api_view(["POST"])
@permission_classes([AllowAny])
def login_api(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Get user groups
            groups = Group.objects.filter(user=user)
            group_names = [group.name for group in groups]

            # Generate a JWT token
            refresh = RefreshToken.for_user(user)
            token = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            return JsonResponse(
                {"message": "Login successful", "token": token, "groups": group_names}
            )
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=401)

    return JsonResponse({"message": "Invalid request method"}, status=400)
