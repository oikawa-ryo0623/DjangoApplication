from django.contrib import admin

#Questionオブジェクトがadminインターフェイスをもつ
from .models import Question,Choice

#
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

#adminサイトにQuestionを登録
admin.site.register(Question,QuestionAdmin)


#adminサイトにChoiceを登録
admin.site.register(Choice)


# Register your models here.
