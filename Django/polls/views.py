from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from polls.forms import LoginForm

# Create your views here.
#def index(request):
    #new_questions = Question.objects.order_by('-pub_date')[:5]

    #output = ', '.join([q.question_text for q in new_questions])
    #return HttpResponse(output)

    #template = loader.get_template('poll_output.html')
    #context = {'new_questions' : new_questions,}
    #return HttpResponse(template.render(context, request))

    #context = {'new_questions' : new_questions,}
    #return render(request, 'poll_output.html', context)
class IndexView(generic.ListView):
    template_name = 'poll_output.html'
    context_object_name = 'new_questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


#def detail(request, question_id):
    #return HttpResponse('Your question id is %s which is in detail field.' % question_id)

    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404('Question not available')
    #return render(request, 'detail.html', {'question': question})

    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'detail.html', {'question': question})
class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

#def results(request, question_id):
    #response = 'Your question id is %s which is in results field.'
    #return HttpResponse(response % question_id)

    #question = get_object_or_404(Question,  pk = question_id)
    #return render(request, 'results.html', {'question': question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

def votes(request, question_id):
    #return HttpResponse('Your question id is %s which is in votes field.' % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def form(request):
    return render(request, 'form.html')

    #login = LoginForm()
    #return render(request, 'form.html', {'form':login})

def detail(request):
    #return render(request, 'detail.html')
    return HttpResponse('Welcome to the form')