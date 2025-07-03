from django.urls import path
from .views import liste_articles, detail_article, ajouter_article

urlpatterns = [
    path('', liste_articles, name='liste_articles'),
    path('article/<int:article_id>/', detail_article, name='detail_article'),
    path('ajouter/', ajouter_article, name='ajouter_article'),
]
