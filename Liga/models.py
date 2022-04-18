from django.db import models




# Create your models here.
class League(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    no_of_teams = models.IntegerField()
    country = models.CharField(default="Srbija", max_length=25)
    season = models.IntegerField(default=2022)
    year = models.TextField(default="2022")


    def __str__(self):
        return self.name + " - season " + str(self.season)





class Team(models.Model):
    name = models.CharField(max_length=20)
    league = models.ForeignKey(League, related_name="teams", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    position = models.CharField(max_length=20, null=True)
    iscaptain = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField()
    game_week = models.IntegerField()
    home_team = models.ForeignKey(Team, related_name="home_teams", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name="away_teams", on_delete=models.CASCADE)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    isplayed = models.BooleanField(default=False)
    

    def __str__(self):
            return self.home_team.name + " - " + self.away_team.name
