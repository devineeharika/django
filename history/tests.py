from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.
class test_url(TestCase):

    def setUp(self):
    
        self.client = None
        self.request_url = '/manager/history'


    def test_anonymous_ping(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)
