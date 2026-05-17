from django.shortcuts import render

ARTICLES = [
    {
        "title": "Who Is Jesus?",
        "slug": "who-is-jesus",
        "excerpt": "Explore the life and message of Jesus Christ.",
        "content": "Jesus Christ is central to the Christian faith..."
    },
    {
        "title": "How to Pray",
        "slug": "how-to-pray",
        "excerpt": "A simple guide to talking with God.",
        "content": "Prayer is a conversation with God..."
    },
    {
        "title": "Knowing God Personally",
        "slug": "knowing-god-personally",
        "excerpt": "Understand the basics of a relationship with God.",
        "content": "God loves you and offers a wonderful plan for your life."
    },
]

def home(request):
    return render(request, 'home.html', {'articles': ARTICLES[:3]})

def about(request):
    return render(request, 'about.html')

def articles(request):
    return render(request, 'articles.html', {'articles': ARTICLES})

def article_detail(request, slug):
    article = next((a for a in ARTICLES if a['slug'] == slug), None)
    if not article:
        article = {"title": "Article Not Found", "content": "The requested article does not exist."}
    return render(request, 'article_detail.html', {'article': article})

def contact(request):
    sent = request.method == 'POST'
    return render(request, 'contact.html', {'sent': sent})
