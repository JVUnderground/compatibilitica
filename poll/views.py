from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .models import Question
from .forms import AnswerForm
from django.http import HttpResponseRedirect

class FrontPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(FrontPage, self).get_context_data(**kwargs)
        count = Question.objects.all().count()
        context['qcount'] = count
        return context

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
            questionid = 1
            pass

        count = Question.objects.all().count()

        context['qcount'] = count
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
