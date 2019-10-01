from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.conf import settings
from django.apps import apps

class RelatedManager(models.Manager):

    def __init__(self, *args):
        super(RelatedManager, self).__init__()
        self.related_fields = args

    def get_queryset(self):
        qs = super(RelatedManager, self).get_queryset()
        if self.related_fields:
            qs = qs.select_related(*self.related_fields)
        return qs


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def get_user_model():
    """
    Returns the User model that is active in this project.
    """
    try:
        return apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )
