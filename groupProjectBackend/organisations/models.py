from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
# from PIL import Image
import os
import uuid
from django.utils.timezone import now


def upload_image_to(self, filename):
        print(filename)
        filename_base, filename_ext = os.path.splitext(filename)
        print(os.path.splitext(filename))
        u = uuid.uuid4()
        return 'posts/%s/%s' % (
            now().strftime("%Y%m%d"),
            u.hex
        )
        s
class Organisation(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_organisation'
    )
    logo = models.ImageField(default=None, upload_to=upload_image_to, blank=True, null=True)
    organisation = models.TextField(max_length=150, blank=True)
    description = models.TextField(max_length=300, blank=True)
    website = models.URLField()
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.organisation

    def save(self, *args, **kwargs):
        self.slug = slugify(self.organisation)
        super(Organisation,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('organisation', kwargs={'slug': self.slug})

