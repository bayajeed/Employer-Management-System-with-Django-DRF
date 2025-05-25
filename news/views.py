from django.shortcuts import render
from .models import NewsPost

# Create your views here.

def news(request):
    posts = NewsPost.objects.all().order_by('-published_date')
    context={
        'posts': posts
    }
    return render(request, 'news.html', context)