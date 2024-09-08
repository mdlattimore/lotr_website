from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Verses

class VersesListView(ListView):
    model = Verses
    template_name = "verses_list.html"
    context_object_name = "verses"
    ordering = ['book', 'sub_book', 'chapter', 'page']


class VerseDetailView(DetailView):
    model = Verses
    context_object_name = "verse"
    template_name = "verse_detail.html"

    