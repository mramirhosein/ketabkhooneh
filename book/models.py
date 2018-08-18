from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200,help_text='Enter a book genre(e.g. Science Fiction,French Poetry etc.)')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200,help_text='Enter a book language(e.g. English,Persian,Chinese etc.)')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000,help_text='Enter a brief description of book.')
    isbn = models.CharField(max_length=13,help_text='13 chararcter <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book.')
    language = models.ManyToManyField(Language, help_text='Select a language for this book.')

    def __str__(self):
        return self.title