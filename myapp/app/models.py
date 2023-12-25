from django.db import models
import uuid
from django.core.validators import MaxValueValidator


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True, unique=True)
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

    POSITION_TYPES = [
        ('GOALKEEPER', 'Вратарь'),
        ('DEFENDER', 'Защитник'),
        ('MIDFIELDER', 'Полузащитник'),
        ('FORWARD', 'Нападающий'),
    ]

    position = models.CharField(max_length=20, choices=POSITION_TYPES)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    jersey_number = models.IntegerField(validators=[MaxValueValidator(99)], unique=True)

    def __str__(self):
        return self.fio


class Transfer(models.Model):
    transfer_id = models.UUIDField(default=uuid.uuid4, editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    from_club = models.ForeignKey(Club, related_name='from_club', on_delete=models.CASCADE, blank=True, null=True)
    to_club = models.ForeignKey(Club, related_name='to_club', on_delete=models.CASCADE)
    transfer_amount = models.DecimalField(max_digits=12, decimal_places=2)
    transfer_date = models.DateField()
    additional_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.from_club:
            return f"Transfer {self.transfer_id} - {self.player.fio} ({self.from_club.name} to {self.to_club.name})"
        else:
            return f"Transfer {self.transfer_id} - {self.player.fio} (Free agent to {self.to_club.name})"


class Contract(models.Model):
    contract_id = models.CharField(max_length=8, unique=True, default=uuid.uuid4().hex[:8])
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    CONTRACT_TYPES = [
        ('standard', 'Стандартный'),
        ('rental', 'Аренда'),
    ]
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    additional_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Contract {self.contract_id} - {self.transfer.player.fio} ({self.club.name}, {self.contract_type})"
