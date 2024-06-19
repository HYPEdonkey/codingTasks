# notes/admin.py

from django.contrib import admin
from .models import Note
from .models import User

# Register your models here.

# Notes model
admin.site.register(Note)

# User model
admin.site.register(User)