from django.db import models

# Create your models here.
class Note(models.Model):
    """
    Model representing a sticky notes application.

    Fields:
    - title: Name given to the note using a Charfield 
        with a maximum length of 255 characters.
    - content: Text used to describe the note and what information must be 
        put in using a TextField.
    - date_created: Using a DateTimeField to set the current date and time when 
    the note is created.

    Relationships:
    - user: ForeignKey representing the user of the sticky notes application.

    Methods:
    - No methods are defined yet in this model.

    :param models.Model: Django's base model class.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)

class User(models.Model):
    """
    Model representing the user of the sticky notes application.

    Fields:
    - name: User's name inputted as a CharField.
    - username: User's username also inputted as a CharField.
    - password: special CharField created by the user to securely log in to their account.
    - phone_number: IntegerField to record the user's contact telephone number.

    """

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField

