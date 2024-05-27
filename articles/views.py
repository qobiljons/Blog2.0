from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Article
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "home.html"


class ArticleDetailedView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "post.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "create_view.html"
    fields = ['title', 'subtitle', 'body', 'photo']
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'subtitle', 'body', 'photo']
    template_name = "update_view.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user




