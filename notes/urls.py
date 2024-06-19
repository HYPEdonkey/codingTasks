# notes/urls.py
from django.urls import path
from .views import notes_list, notes_detail, notes_create, notes_update, notes_delete

urlpatterns = [
    # URL pattern for displaying a list of all notes
    path('', notes_list, name='notes_list'),

    # URL pattern for displaying details of a specific note.
    path('notes/<int:pk>/', notes_detail, name='notes_detail'),

    # URL pattern for creating a new note.
    path('notes/new', notes_create, name='notes_create'),

    # URL pattern for updating an existing note.
    path('notes/<int:pk>/edit/', notes_update, name='notes_update'),

    # URL pattern for deleting an existing note.
    path('note/<int:pk>/delete/', notes_delete, name='note_delete'),

]