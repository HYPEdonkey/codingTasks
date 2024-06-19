from django.test import TestCase
from django.urls import reverse
from notes.models import Note, User

# Create your tests here.


class NoteModelTest(TestCase):
    def setUp(self):
        # Create a User object.
        user = User.objects.create(name='Test User')
        # Create a Note object for testing.
        Note.objects.create(title='Test Note', content='This is a test note.', user=user)

    def test_note_has_title(self):
        # Test that a Note object has the expected title.
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        # Test that a Note object has the expected content.
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

class NoteViewTest(TestCase):
    def setUp(self):
        # Create a User object.
        user = User.objects.create(name='Test User')
        # Create a Note object for testing views.
        Note.objects.create(title='Test Note', content='This is a test note.', user=user)
    
    def test_note_list_view(self):
        # Test the note-list view
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    def test_notes_detail_view(self):
        # Test the note-detail view
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('notes_detail',args=[str(note.id)]))
        print(response.content.decode())  # Print the response content for debugging
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')