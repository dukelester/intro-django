from django.urls import path
from .views import index, details, voting, results

app_name = 'pollingApp'
urlpatterns = [
    path('', index, name='homepage'),
    path('<int:question_id>/results', results, name='results'),
    path('<int:question_id>/voting', voting, name='voting'),
    path('<int:question_id>/details', details, name='details')

]
