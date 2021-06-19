from django.urls import path

from . import views
# from .views import index, details, results
#
# app_name = 'pollingApp'
# urlpatterns = [
#     path('', index, name='homepage'),
#     path('<int:question_id>/results', results, name='results'),
#     path('<int:question_id>/voting', views.vote, name='voting'),
#     path('<int:question_id>/', details, name='details')
#
# ]

# using the generic views
app_name = 'pollingApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote')
    ]