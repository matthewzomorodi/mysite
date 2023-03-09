from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.question.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.question.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.question.vote, name='vote'),
    # ex: /new-client/
    path('add-client/', views.client.add_client, name="add_client"),
    # ex: /client/1/
    path('get-client/<int:client_id>/', views.client.get_client, name="get_client")
]