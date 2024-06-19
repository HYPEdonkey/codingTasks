from django import forms
from .models import Note

class NotesForm(forms.ModelForm):
    """
    Form for creating and updating the objects within the Notes class

    Fields:
    - title: CharField for the note title.
    - content: TextField for the note content.

    Meta class:
    - Defines the model to use (Note) and the fields to include in the form.

    :param forms.ModelForm: Django's ModelForm class.
    """
    class Meta:
        model = Note
        fields = ['title', 'content', 'user']
        