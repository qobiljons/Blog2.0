from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Article
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "home.html"


class ArticleDetailedView(DetailView):
    model = Article
    template_name = "post.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "post.html"


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'subtitle', 'body', 'photo']
    template_name = "update_view.html"
    success_url = reverse_lazy("home")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "delete.html"




