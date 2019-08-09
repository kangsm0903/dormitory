from django.shortcuts import render
from .forms import SearchForm
from .models import Advice

def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def apply(request):
    return render(request, 'apply.html')

def comment(request):
    advice = Advice.objects
    return render(request, 'comment.html', {'advice': advice})

def room(request):
    return render(request, 'room.html')

def search(request):
    return render(request, 'search.html')

def submit(request):
    return render(request, 'submit.html')

def etc(request):
    return render(request, 'etc.html')

def road(request):
    return render(request, 'road.html')

def base(request):
    return render(request, 'dorm_project/base.html')

def new(request):
    
    return render(request, 'new.html')
# class search(): 
    # pass
    # form_class = SearchForm 
    # template_name = 'search.html'

    # def form_valid(self,form):
    #     word = '%s' %self.request.POST['word']
    #     post_list = Post.objects.filter(
    #         Q(title__icontains = word) | Q(content__icontains = word)
        
    #     ).distinct()
    #     context = {}
    #     context['object_list'] = post_list
    #     context['search_word'] = word
    #     return context
    
    
