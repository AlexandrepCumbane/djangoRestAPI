from django.contrib import admin
from .models import Snippet


@admin.register(Snippet)
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register your models here.
