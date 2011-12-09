"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.utils import unittest
from django.test import TestCase
from events.models import Event


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class EventTestCase(unittest.TestCase):
    #fixtures = ['eventbewertung.json']
    
    def setUp(self):
        self.event1 = Event.objects.create(name="Event1", pub_date=datetime.datetime.now())
        self.event2 = Event.objects.create(name="Event2", pub_date=datetime.datetime.now())

    def test(self):
        self.assertEqual(self.event1.name, 'Event1')
        self.assertEqual(self.event2.name, 'Event2')
        self.assert_(self.event1.was_published_today)
        self.assertTrue(self.event2.was_published_today)

    def testfixtures(self):
        testevent = Event.objects.get(id=1)
        self.assert_(testevent != None)
        self.assert_(testevent.name == "Event1")
