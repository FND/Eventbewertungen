"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import unittest
from django.test import TestCase
from talks.models import Talk

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TalkTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        
    def clienttests(self):
        response = self.client.get('/talks/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['talk']), 3)
