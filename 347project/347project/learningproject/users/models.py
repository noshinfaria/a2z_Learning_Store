from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class TeacherRegister(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    institute = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'message from - ' + self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_picture/', blank=True, null=True)

    def __str__(self):
        return ' profile -  ' + self.name


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Help(models.Model):
    title = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=2000, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('help')


class ContactUs(models.Model):
    sno = models.AutoField(primary_key=True, default = 1)
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=100, blank=False)
    describe = models.TextField(max_length=2000, blank=False)
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ' contact -  ' + self.name

    def get_absolute_url(self):
        return reverse('contact_us')