# -*- coding: utf-8 -*-

from django.conf.urls import url

from faq.views import TopicListView, TopicDetailView, question_detail


# Include these patterns if you want URLs like:
#
#   /faq/
#   /faq/topic/
#   /faq/topic/#question
#

urlpatterns = [
    url(r'^$', TopicListView.as_view(), name='faq-topic-list'),
    url(
        r'^(?P<slug>[-\w]+)/$',
        TopicDetailView.as_view(),
        name='faq-topic-detail'),
    url(
        r'^(?P<topic_slug>[-\w]+)/#(?P<slug>[-\w]+)/$',
        question_detail,
        name='faq-question-detail'),
]
