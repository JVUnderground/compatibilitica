from django.views.generic.edit import FormView
from .models import Question
from .forms import AnswerForm
from django.http import HttpResponseRedirect
# Create your views here.

class QuestionPage(FormView):
    template_name = "poll.html"
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super(QuestionPage, self).get_context_data(**kwargs)
        questionid = 1
        try:
            questionid = int(self.kwargs['question'])
        except KeyError:
            pass

        try:
            question = Question.objects.get(pk=questionid)
        except Question.DoesNotExist:
            question = Question.objects.get(pk=1)
            pass

        context['question'] = question
        context['qnext'] = questionid + 1
        return context

    def form_valid(self, form):
        post = self.request.POST
        questionid = int(post['questionid'])
        answer = form.save(commit=False)
        answer.question = Question.objects.get(pk=questionid)
        answer.save()
        return HttpResponseRedirect('/vote/%d/' % (questionid + 1))
