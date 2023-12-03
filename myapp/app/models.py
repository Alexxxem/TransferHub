from django.db import models
from django.utils import timezone
import uuid


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    fio = models.CharField(max_length=255)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    jersey_number = models.IntegerField(max_length=99)

    def __str__(self):
        return self.fio


class Transfer(models.Model):
    transfer_id = models.UUIDField(default=uuid.uuid4, editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    from_club = models.ForeignKey(Club, related_name='from_club', on_delete=models.CASCADE)
    to_club = models.ForeignKey(Club, related_name='to_club', on_delete=models.CASCADE)
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_date = models.DateTimeField(default=timezone.now)
    additional_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transfer {self.transfer_id} - {self.player.fio} ({self.from_club.name} to {self.to_club.name})"


class Contract(models.Model):
    contract_id = models.CharField(max_length=8, unique=True, default=uuid.uuid4().hex[:8])
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    CONTRACT_TYPES = [
        ('standard', 'Стандартный'),
        ('rental', 'Аренда'),
    ]
    contract_type = models.CharField(max_length=10, choices=CONTRACT_TYPES)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    additional_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Contract {self.contract_id} - {self.transfer.player.fio} ({self.club.name}, {self.contract_type})"