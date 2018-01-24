from django.contrib import admin
from myapp.models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('q_text','q_date')
    inlines = [ChoiceInline]
    fieldsets = [
        ('Question',{'fields':['q_text']}),
        ('Date information',{'fields':['q_date']})
    ]

admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)