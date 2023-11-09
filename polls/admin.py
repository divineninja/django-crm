# polls/admin.py
from django.contrib import admin
from .models import Question, Choice, Condition, Campaign


class CustomAdminSite(admin.AdminSite):
    site_header_color = '#2ecc71'  # Set your desired color


admin_site = CustomAdminSite(name='customadmin')


class ConditionInline(admin.TabularInline):
    model = Condition
    fk_name = 'question'  # Specify the ForeignKey to 'Question'
    extra = 1  # Adjust the number of conditions displayed inline


class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ('choices',)
    inlines = [ConditionInline]
    list_display = ('question_text', 'question_code', 'order', 'status', 'pub_date')
    search_fields = ['question_text', 'question_code']


class CampaignAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)  # This will display questions as checkboxes

    list_display = ('campaign_code', 'campaign_name', 'status', 'pub_date')
    search_fields = ['campaign_code', 'campaign_name']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Condition)
admin.site.register(Campaign, CampaignAdmin)
