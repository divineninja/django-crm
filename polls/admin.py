# polls/admin.py
from django import forms
from django.contrib import admin
from .models import Question, Choice, Condition, Campaign


class ConditionInline(admin.TabularInline):
    model = Condition
    raw_id_fields = ['parent_question']
    filter_horizontal = ('parent_answer',)
    fk_name = 'question'  # Specify the ForeignKey to 'Question'
    extra = 1  # Adjust the number of conditions displayed inline


class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ('choices',)
    inlines = [ConditionInline]
    list_filter = ('status', 'campaign')
    list_display = ('question_code', 'order', 'status', 'pub_date')
    search_fields = ['question_text', 'question_code']


class CampaignAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)  # This will display questions as checkboxes
    list_filter = ('status',)
    list_display = ('campaign_code', 'campaign_name', 'status', 'pub_date')
    search_fields = ['campaign_code', 'campaign_name']


class ConditionAdmin(admin.ModelAdmin):
    raw_id_fields = ['question', 'parent_question']
    filter_horizontal = ('parent_answer',)  # This will display questions as checkboxes


admin.site.register(Condition, ConditionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Campaign, CampaignAdmin)
