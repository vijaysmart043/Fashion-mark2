from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model for Indian e-commerce platform supporting email, mobile verification,
    and customer profile attributes.
    """
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(_('mobile number'), max_length=15, unique=True, blank=True, null=True)
    is_mobile_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
