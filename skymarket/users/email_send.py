from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage
from djoser import utils
from djoser.conf import settings


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        context = super().get_context_data()
        user = context['user']
        current_site = get_current_site(self.request)
        reset_url = reverse('password-reset-confirm', kwargs={
            'uid': utils.encode_uid(user.pk),
            'token': default_token_generator.make_token(user),
        })
        reset_url = f'http://{current_site.domain}{reset_url}'
        context['password_reset_url'] = reset_url

        return context
