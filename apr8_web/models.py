from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Player(models.Model):
    # id = models.BigIntegerField(default=0, primary_key=True)
    player_id = models.CharField(default='', max_length=200)
    player_name = models.CharField(max_length=200)
    player_position = models.CharField(max_length=200)

    def __str__(self):
        return self.player_name
    # end str()
# end class


class PlayerSeason(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # player_name = models.CharField(max_length=200)
    season = models.PositiveIntegerField(default=datetime.datetime.now().year,
                                         validators=[MinValueValidator(1920),
                                                     MaxValueValidator(datetime.datetime.now().year)])
    games_played = models.PositiveIntegerField(default=0,
                                               validators=[MinValueValidator(0),
                                                           MaxValueValidator(16)])
    games_started = models.PositiveIntegerField(default=0,
                                                validators=[MinValueValidator(0),
                                                            MaxValueValidator(16)])
    pass_completions = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    pass_attempts = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    # comp_percent = models.FloatField(default=0, validators=[MinValueValidator(0)])
    passing_yards = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    touchdowns = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    # td_percent = models.FloatField(default=0, validators=[MinValueValidator(0)])
    interceptions = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    # int_percent = models.FloatField(default=0, validators=[MinValueValidator(0)])
    passer_rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(158.3)])
    # passer_rating_plus = models.FloatField(default=0, validators=[MinValueValidator(0)])

    # str method
    def __str__(self):
        return str(self.season) + ": " + self.player.player_name
    # end str

    # create methods for the above rate stats below:

# end class()
