from django.contrib import admin
from django.urls import path
from .views import VersesListView, VerseDetailView

urlpatterns = [
    path('', VersesListView.as_view(), name="home"), # temporary
    path('verses_list/', VersesListView.as_view(), name="verses_list"),
    path('verse_detail/<int:pk>/', VerseDetailView.as_view(), name="verse_detail"),
]