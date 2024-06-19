from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NotesForm

# Create your views here.

def notes_list(request):
    """
    View to display a list of all the notes.

    :param request: HTTP request object.
    :return: Rendered template with a list of notes.

    """

    notes = Note.objects.all()

    # This creates a dictionary on the note's context
    context = {
        'notes': notes,
        'page_title': 'List of Notes',

    }

    return render(request, 'notes/notes_list.html', context)

def notes_detail(request, pk):
    """
    View to show details of a specific note.

    :param request: HTTP request object.
    :param pk: Primary key of the note.
    :return: Rendered template that contains the details of the specified note.
    """

    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/notes_detail.html', {'note': note})

def notes_create(request):
    """
    View to create new notes.

    :param request: HTTP request object.
    :return: Rendered template for creating a new post.
    """

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            # if request.user.is_authenticated:
            #     note.user = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NotesForm
    return render(request, 'notes/notes_form.html', {'form': form})

def notes_update(request, pk):
    """
    View to update an existing note.

    :param request: HTTP request object.
    :param pk: Primary key of the note to be updated.
    :return: Rendered template for updating the specified note.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes_list')
    else:
        form = NotesForm(instance=note)
    return render(request, 'notes/notes_form.html', {'form': form})

def notes_delete(request, pk):
    """
    View to delete an existing note.

    :param request: HTTP request object.
    :param pk: Primary key of the note to be deleted.
    :return: Redirect to the notes list after deletion.
    """

    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes_list')
