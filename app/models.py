from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse


class URLMapper(models.Model):
    create = models.DateTimeField(auto_now_add=True, blank=True)
    url = models.URLField()

    objects = models.Manager()

    def get_absolute_url(self):
        print(self.pk)

        return reverse("fetch_url", args=[str(self.pk)])

    @property
    def shorten_url(self):
        domain = Site.objects.get_current().domain
        return f"http://{domain}{self.get_absolute_url()}"
