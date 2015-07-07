from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True,default='')

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        if self.likes < 0:
            self.likes = 0

        self.slug = slugify(self.name)
        super(Category, self).save()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    first_visit = models.DateTimeField(auto_now_add=True, blank=True)
    last_visit = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        now = datetime.now()
        if self.first_visit > self.last_visit:
            self.first_visit = self.last_visit
        if self.last_visit > now:
            self.last_visit = now
        if self.first_visit > now:
            self.first_visit = now


        super(Page, self).save()

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username