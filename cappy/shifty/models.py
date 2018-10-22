from django.db import models

# this is the information that will be saved in the database
# saved needs to be input field, date and time

class userName(models.Model):
    name = models.CharField(max_length=20)
    day = models.CharField(max_length=20)


    def __str__(self):
        return self.name + " - " + self.day



# class userTime(models.Model):
#     time = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.time


