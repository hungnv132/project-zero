from django.db import models
from django.contrib.auth.models import User


class TrackingTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TrackingUser(models.Model):
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created",
                                   blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_modified",
                                    blank=True, null=True)

    class Meta:
        abstract = True
