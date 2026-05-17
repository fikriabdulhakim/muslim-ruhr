from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ContactForm

def home(request):
    articles = Article.objects.all()[:3]
    return render(request, 'core/home.html', {'articles': articles})

def about(request):
    return render(request, 'core/about.html')

def articles(request):
    return render(request, 'core/articles.html', {'articles': Article.objects.all()})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'core/article_detail.html', {'article': article})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
