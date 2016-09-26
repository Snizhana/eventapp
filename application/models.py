import uuid
from django.db import models

from events.models import Event


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}{}".format(uuid.uuid4(), extension)

class Application(models.Model):

    mail = models.EmailField(max_length=100)
    event = models.ForeignKey(Event)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    sur_name = models.CharField(max_length=40, blank=True)
    user_info = models.TextField(max_length=1000, blank=True, null=True)
    job = models.CharField(max_length=40, blank=True)
    user_image = models.ImageField(
        'uploaded images',
        upload_to="scramble_uploaded_filename",
        blank=True,
        null=True)
    info_source = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.mail

    class Meta:
        ordering = ('-created_at',)
