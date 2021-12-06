from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from account.forms import MakePostForm
from article.models import Posts
# Create your views here.


def home(request):
    context = {}
    context['posts'] = Posts.objects.order_by('-time')

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