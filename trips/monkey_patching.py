#app/monkey_patching.py
from django.contrib.auth.models import User 

def count_number_of_trips(self):
    return self.trip_set.filter().count()

User.add_to_class("count_number_of_trips",count_number_of_trips)