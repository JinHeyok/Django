from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.


def index(request):
    list = Question.objects.order_by('-pun_date')[:]
    # output = ', '.join([q.question_text for q in list])
    # template = loader.get_template('polls/index.html')
    content = {
        'list': list,
    }
    # return HttpResponse(template.render(content, request))
    return render(request, 'polls/index.html', content)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(requset, question_id):
    # return HttpResponse("you're looking at the results of question %s. " % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(requset, 'polls/results.html', {'question': question})


def vote(request, question_id):
   # return HttpResponse("you're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # key value값으로 데이터 받아옴
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message ': 'error'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
