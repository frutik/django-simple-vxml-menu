from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    greeting = models.TextField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    menu = models.ForeignKey(Menu)
