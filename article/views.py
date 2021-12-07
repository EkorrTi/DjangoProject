from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from account.forms import MakePostForm
from article.models import Posts
# Create your views here.


def home(request):
    context = {}
    context['posts'] = Posts.objects.order_by('-time')
    context['user'] = request.user

    return render(request, 'home.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def post_form(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        form = MakePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.text = form.cleaned_data.get('text')
            post.save()
            return redirect('home')
    else:
        form = MakePostForm()
        context['post_form'] = form
    return render(request, 'post-form.html', context)

def post_delete_form(request, id):
    context = {}
    obj = get_object_or_404(Posts, id = id)
    context['post'] = obj

    if request.POST:
        obj.delete()
        return redirect('home')
    
    return render(request, 'post_delete.html', context)