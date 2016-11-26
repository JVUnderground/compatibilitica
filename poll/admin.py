from django.contrib import admin
from .models import Question, Answer
from django.http import HttpResponse
import csv

# Register your models here.

def export_question_data(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dados-votos.csv"'
    writer = csv.writer(response)

    header = ["Question ID", "Question Title", "Answer ID", "Social Score", "Economic Score"]
    writer.writerow(header)

    for question in queryset:
        answers = Answer.objects.filter(question=question)
        for answer in answers:
            row = [question.id, question.title, answer.id, answer.social, answer.economic]
            writer.writerow(row)

    return response

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    ordering = ['id']

    actions = [export_question_data]


admin.site.register(Question, QuestionAdmin)