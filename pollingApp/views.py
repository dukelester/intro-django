from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
# Create your views here.
from django.template import loader
from django.urls import reverse

from pollingApp.models import Question, Choice


def index(request):
    latest_update_posts = Question.objects.order_by('-pub_date')[:5]
    total_posts = Question.objects.all()
    posts = []
    for post in total_posts:
        posts.append(post)
    total_posts = len(posts)

    # output = ','.join([q.question_text for q in latest_update_posts])
    print(latest_update_posts)
    # template = loader.get_template('polls/index.html')

    # return HttpResponse(output)
    context = {
        'latest_update_posts': latest_update_posts,
        'posts': posts,
        'total_posts': total_posts,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    # details view
    try:
        question_detail = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:

        raise Http404('The page for the details does not exist')

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question_detail': question_detail,
        'question': question,
    }

    return render(request, 'polls/details.html', context)
    # return HttpResponse('You are looking for the question %s' % question_id)


def results(request, question_id):
    return HttpResponse('The results of the above is %s ' % question_id)


def voting(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html',
                      {'question': question, 'error_message': 'You did not select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

    # return HttpResponse('You are voting on the question %s' % question_id)
    return HttpResponseRedirect(reverse("pollingApp:results", args=question_id))
