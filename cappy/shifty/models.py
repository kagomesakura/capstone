from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings


# this is the information that will be saved in the database

class DayOff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField()

    def __str__(self):
        return f'{self.user.username} - {self.start} - {self.end}'


    def to_dict(self):
        return {'id': self.id, 'title': self.user.username, 'start': self.start.strftime('%Y-%m-%d'), 'end': self.end.strftime('%Y-%m-%d')}

    def to_pretty_dict(self):
        return {'id': self.id, 'title': self.user.username, 'start': self.start.strftime('%b %e'), 'end': self.end.strftime('%b %e')}


# def __str__(self)

