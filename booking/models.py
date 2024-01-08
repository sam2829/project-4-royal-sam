from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# These are a list of the available times a player can choose to tee off

AVAILABLE_TIMES = (
    ("07:30", "07:30"), ("07:50", "07:50"), ("08:10", "08:10"), ("08:30", "08:30"),
    ("08:50", "08:50"), ("09:10", "09:10"), ("09:30", "09:30"), ("09:50", "09:50"),
    ("10:10", "10:10"), ("10:30", "10:30"), ("10:50", "10:50"),
    ("11:10", "11:10"), ("11:30", "11:30"), ("11:50", "11:50"),
    ("12:10", "12:10"), ("12:30", "12:30"), ("12:50", "12:50"),
    ("13:10", "13:10"), ("13:30", "13:30"), ("13:50", "13:50"),
    ("14:10", "14:10"), ("14:30", "14:30"), ("14:50", "14:50"),
    ("15:10", "15:10"), ("15:30", "15:30"), ("15:50", "15:50"),
    ("16:10", "16:10"), ("16:30", "16:30"), ("16:50", "16:50"),
    ("17:10", "17:10"), ("17:30", "17:30"), ("17:50", "17:50"),
)

# List of number of players

NUMBER_OF_PLAYERS = (
    ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
)

# This is the model and necessary fields for booking a tee time


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    email = models.EmailField()
    date = models.DateField(default=datetime.now)
    time = models.CharField(choices=AVAILABLE_TIMES,
                            max_length=10, default="7:30")
    number_of_players = models.CharField(choices=NUMBER_OF_PLAYERS,
                                         max_length=1, default="1")
    member = models.BooleanField(default=False)
    buggy = models.BooleanField(default=False)

    class Meta:

        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.user.username} booked {self.date} at {self.time} for {self.number_of_players}"
