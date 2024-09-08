from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Verses, Characters

class VersesListView(ListView):
    model = Verses
    template_name = "verses_list.html"
    context_object_name = "verses"
    ordering = ['book', 'sub_book', 'chapter', 'page']


class VerseDetailView(DetailView):
    model = Verses
    context_object_name = "verse"
    template_name = "verse_detail.html"
    


class CharactersListView(ListView):
    model = Characters
    context_object_name = "characters"
    ordering = ['name']
    template_name = "characters_list.html"


class CharacterDetailView(DetailView):
    model = Characters
    context_object_name = "character"
    template_name = "character_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verses'] = self.object.verses_set.all()
        return context


    