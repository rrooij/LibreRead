from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import BookReader


@receiver(post_save, sender=BookReader)
def add_user(sender, **kwargs):
    pass  # TODO: This is where a user should be registered
