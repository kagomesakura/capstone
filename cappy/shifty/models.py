from django.db import models

# this is the information that will be saved in the database

class DayOff(models.Model):
    name = models.CharField(max_length=20)
    start = models.DateField(max_length=20)
    end = models.DateField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.start} - {self.end}'


    def to_dict(self):
        return {'title': self.name, 'start': self.start.strftime('%Y-%m-%d'), 'end': self.end.strftime('%Y-%m-%d')}

    #(name=title, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))


