from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {
    'blank': True,
    'null': True
}


class UserRoles(models.TextChoices):
    USER = 'user', _('User')
    ADMIN = 'admin', _('Admin')


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=60, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=60, verbose_name=_('Last Name'))
    phone = PhoneNumberField(max_length=30, verbose_name=_('Phone Number'), **NULLABLE)
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    image = models.ImageField(upload_to='users/images', verbose_name=_('Avatar'), **NULLABLE)
    role = models.CharField(
        max_length=50,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name=_('Role')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
