from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .models import Question, Answer
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

    def get_initial(self):
        questionid = self.kwargs['question']
        aSession = self.request.session
        if aSession.get(questionid):
            answer = Answer.objects.get(pk=int(aSession[questionid]))
            defaultSocial = answer.social
            defaultEconomic = answer.economic
        else:
            defaultSocial = 0
            defaultEconomic = 0

        return { 'social': defaultSocial, 'economic': defaultEconomic }

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
        
        aSession = self.request.session
        if aSession.get("%d" % questionid):
            context['message'] = "Respondido. Deseja atualizar a resposta?"


        count = Question.objects.all().count()

        context['qcount'] = count
        context['question'] = question
        context['qnext'] = questionid + 1
        return context

    def form_valid(self, form):
        post = self.request.POST
        questionid = post['questionid']
        newanswer = form.save(commit=False)
        if self.request.session.get(questionid):
            lastid = int(self.request.session[questionid])
            lastanswer = Answer.objects.get(pk=lastid)
            lastanswer.social = newanswer.social
            lastanswer.economic = newanswer.economic
            lastanswer.save()
            self.request.session[questionid] = lastanswer.id
        else:
            newanswer.question = Question.objects.get(pk=int(questionid))
            newanswer.save()
            self.request.session[questionid] = newanswer.id

        return HttpResponseRedirect('/vote/%d/' % (int(questionid) + 1))


class ThanksPage(TemplateView):
    template_name = "thanks.html"

