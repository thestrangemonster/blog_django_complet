from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django import forms

def liste_articles(request):
    articles = Article.objects.order_by('-date_creation')
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/detail_article.html', {'article': article})

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu']

def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'blog/ajouter_article.html', {'form': form})
