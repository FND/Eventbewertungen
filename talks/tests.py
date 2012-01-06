from django.utils import unittest
from django.test import TestCase
from talks.models import Talk


class TalkTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def clienttests(self):
        response = self.client.get('/talks/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['talk']), 3)
