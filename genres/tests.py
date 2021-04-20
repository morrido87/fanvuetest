from django.db.models import Q
from django.test import TestCase

from genres.models import Genre


class GenresTestCase(TestCase):

    def test_counters_starting_with_w(self):
        with_w = Genre.objects.artists_count()
        without_w = Genre.objects.artists_count(Q(artists__name__startswith='W'))

        for element1, element2 in zip(with_w, without_w):
            self.assertEqual(element1.name, element2.name)
            self.assertGreaterEqual(element1.total, element2.total)
        self.assertEquals(len(with_w), len(without_w))
