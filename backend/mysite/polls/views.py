from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from rest_framework import viewsets,generics,permissions
from serializers import QuestionSerializer


from polls.models import Question
class QuestionDetail(DetailView):
    model = Question
    success_url = reverse_lazy('question_detail')
    fields = ['title', 'description', 'author']

        
class QuestionList(ListView):
    model = Question
    fields = ['title', 'description', 'author']



class QuestionCreate(CreateView):
    model = Question
    success_url = reverse_lazy('question_list')
    fields = ['title', 'description', 'author']

class QuestionUpdate(UpdateView):
    model = Question
    success_url = reverse_lazy('question_list')
    fields = ['title', 'description', 'author']

class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('question_list')
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'author']

def question_detail(request, template_name='polls/question_detail.html'):
    questions = Question.objects.all()
    data = {}
    data['object_list'] = questions 
    return render(request, template_name, data)        

def question_list(request, template_name='polls/question_list.html'):
    questions = Question.objects.all()
    data = {}
    data['object_list'] = polls 
    return render(request, template_name, data)

def question_create(request, template_name='polls/question_form.html'):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render(request, template_name, {'form':form})

def question_update(request, pk, template_name='polls/question_form.html'):
    server = get_object_or_404(Server, pk=pk)
    form = ServerForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render(request, template_name, {'form':form})

def question_delete(request, pk, template_name='polls/question_confirm_delete.html'):
    server = get_object_or_404(Server, pk=pk)    
    if request.method=='POST':
        question.delete()
        return redirect('question_list')
    return render(request, template_name, {'object':question})

class QuestionViewSet(viewsets.ModelViewSet):
  
    queryset = Question.objects.all().order_by('-author')
    serializer_class = QuestionSerializer
