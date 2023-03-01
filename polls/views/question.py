from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from ..models.question import Question
from ..models.choice import Choice

def detail(request, question_id):
    # if request.method == 'GET':
    #     print('GET: user=', request.GET.get('user', ''))
    # if request.method == 'POST':
    #     print('POST: user=', request.GET.get('user', ''))
    #     print('POST: last-name=', request.POST.get('last-name', ''))
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Question.objects.filter(pub_date__lte=timezone.now()).get(pk=question_id)
        context = {'question': question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question': question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }

        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))