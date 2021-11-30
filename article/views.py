from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from article.models import Posts
# Create your views here.


def home(request):
    context = {}
    context['posts'] = Posts.objects.order_by('-time')

    return render(request, 'home.html', context)

def contacts(request):
    return render(request, 'contacts.html')