from django.test import TestCase
from . models import*
# Create your tests here.

class TestNeighbor(TestCase):
    def setUp(self):
        self.karatina = Neighborhood(name='karatina')
        self.karatina.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Karatina,Neighborhood))