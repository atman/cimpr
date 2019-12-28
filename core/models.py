from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


def upload_image(instance, filename):
    return "relations/{user}/{filename}".format(user=instance.User, filename=filename)


class ContactQuerySet(models.QuerySet):
    pass


class ContactManager(models.Manager):
    def get_queryset(self):
        return ContactQuerySet(self.model, using=self.db)


class User(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Contact(models.Model):
    DAILY = 'D'
    WEEKLY = 'W'
    MONTHLY = 'M'
    YEARLY = 'Y'

    TYPE_OF_RELATIONSHIP_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (YEARLY, 'Yearly'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=TYPE_OF_RELATIONSHIP_CHOICES, default=MONTHLY)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = ContactManager()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return str(self.first_name)
