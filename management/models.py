import uuid
from django.db import models
from django.conf import settings

class Competition(models.Model):
    name = models.CharField(max_length=120)
    competition_id = models.CharField(max_length=120)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.competition_id

class Round(models.Model):
    round_number = models.IntegerField()
    is_final = models.BooleanField(default=False)
    event = models.CharField(max_length=10)

class Group(models.Model):
    label = models.CharField(max_length=20, default="Unlabelled group")
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    competitors = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.label

class Station(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=20, default="Unlabelled station")
    competitor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="competitor_station")
    judge = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="judge_station")
    current_group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"Station {self.code}"
