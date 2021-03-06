from django.conf.urls import patterns, include, url
from django.contrib import admin
from poll.views import FrontPage, QuestionPage, ThanksPage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compatibilitica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', FrontPage.as_view()),
    url(r'^vote(/)?$', QuestionPage.as_view()),
    url(r'^vote/(?P<question>\d+)(/)?$', QuestionPage.as_view()),
    url(r'^obrigado/$', ThanksPage.as_view()),
    url(r'^^(admin)\w+', FrontPage.as_view()),
)
