from django.db.models import Manager
from django.db.models.query import QuerySet

__author__ = 'Derek Stegelman'
__date__ = '11/9/12'

class TripQuerySet(QuerySet):

    def published(self):
        return self.filter(published=True)

class TripManager(Manager):

    def get_query_set(self):
        return TripQuerySet(self.model, self._db)

    def published(self):
        return self.get_query_set().published()