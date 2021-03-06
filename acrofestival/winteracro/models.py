from django.db import models

# Create your models here.

class Workshop(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=10)
    teachers = models.TextField(max_length=120, blank=True, null=True)
    workshop = models.TextField(max_length=300, blank=True, null=True)
    prerequisites = models.TextField(max_length=300, blank=True, null=True)

    def day(self):
        return self.date.strftime("%A")


Styles = (
    ("style1", "Style 1"),
    ("style2", "Style 2"),
    ("style3", "Style 3"),
    ("style4", "Style 4"),
    ("style5", "Style 5"),
)

Icons = (
    ("icon fa-home", "Home"),
    ("icon fa-flag-checkered", "Flag"),
    ("icon fa-fire", "Fire"),
    ("icon fa-utensils", "Cutlery"),
    ("icon fa-cogs", "Cogs"),
    ("icon fa-om", "Om"),
    ("icon fa-snowflake", "Snow"),
    ("icon fa-magic", "Magic"),
)


class Day(models.Model):
    day = models.CharField(max_length=20)

    def __str__(self):
        return self.day


class Entrie(models.Model):
    style = models.CharField(max_length=8, choices=Styles)
    icon = models.CharField(max_length=25, choices=Icons)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=30)
    when = models.ForeignKey(Day, on_delete=models.CASCADE)
