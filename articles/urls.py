from django.urls import path
from .views import ArticleListView, ArticleDetailedView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('article/<int:pk>', ArticleDetailedView.as_view(), name="article_detailed"),
    path('update/article/<int:pk>', ArticleUpdateView.as_view(), name="update")
]

