from django.test import TestCase
from .models import User, Bus


class BusTestCase(TestCase):
    def test_setUp(self) -> None:
        self.user = User.objects.create(user_id=1, name="testUser", password="1234", email="testUser@gmail.com")


    def test_createBus(self):
        self.bus = Bus.objects.create(bus_name="Mersedes", source="Київ", dest="Львів", nos=20, rem=20, price=300,
                                      date="2021-06-01", time="08:30:00")

