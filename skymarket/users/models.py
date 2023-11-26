from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {
    'blank': True,
    'null': True
}


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'

    choices = [
        (USER, _('user')),
        (ADMIN, _('admin'))
    ]


class User(AbstractBaseUser):
    username = None

    first_name = models.CharField(max_length=60, verbose_name='имя')
    last_name = models.CharField(max_length=60, verbose_name='фамилия')
    phone = PhoneNumberField(max_length=30, verbose_name='номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    image = models.ImageField(upload_to='users/images', verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='роль')

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

    # @property
    # def is_superuser(self):
    #     return self.is_admin
    #
    # @property
    # def is_staff(self):
    #     return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
