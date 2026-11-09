from django.urls import path
from django.http import HttpResponse

from .models import Question

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    # the 'name' value as called by the {% url %} template tag
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # added the word 'specifics'
    path("specifics/<int:question_id>/", views.detail, name="detail"),

]


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
