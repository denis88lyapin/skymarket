from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from .models import Ad

from rest_framework_simplejwt.tokens import AccessToken

from ..users.models import User


class HabitCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@teast.ru')
        self.user.set_password('test')
        self.user.save()

        self.token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.habit = Ad.objects.create(
            title='название товара',
            price=1000,
            description='описание товара',
            author=self.user,
        )

    def test_habit_list(self):
        url = reverse('ads:ads-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
