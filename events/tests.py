import datetime

from django.utils import unittest
from django.test import TestCase
from django.test.client import Client

from events.models import Event


class EventTestCase(unittest.TestCase):
    #fixtures = ['eventbewertung.json']

    def setUp(self):
        self.event1 = Event.objects.create(name="Event1",
                pub_date=datetime.datetime.now())
        self.event2 = Event.objects.create(name="Event2",
                pub_date=datetime.datetime.now())
        self.client = Client()

    def test(self):
        self.assertEqual(self.event1.name, 'Event1')
        self.assertEqual(self.event2.name, 'Event2')
        self.assert_(self.event1.was_published_today)
        self.assertTrue(self.event2.was_published_today)

    def testfixtures(self):
        testevent = Event.objects.get(id=1)
        self.assert_(testevent != None)
        self.assert_(testevent.name == "Event1")

    def test_event_result(self):
        response = self.client.get("/events/1/results/")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['event'])
