from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Zone(models.Model):
    name = models.CharField(max_length=64, unique=True)

    @classmethod
    def create(cls, name):
        zone = cls(name=name)
        return zone

    def __unicode__(self):
        return str(self.name)


class Corp(models.Model):
    name = models.CharField(max_length=64, unique=True)

    @classmethod
    def create(cls, name):
        corp = cls(name=name)
        return corp

    def __unicode__(self):
        return str(self.name)


class Player(models.Model):
    name = models.CharField(max_length=64, unique=True)
    corp = models.ForeignKey(Corp)

    @classmethod
    def create(cls, name, corp):
        player = cls(name=name, corp=corp)
        return player

    def __unicode__(self):
        return str(self.name)


class Robot(models.Model):
    name = models.CharField(max_length=32, unique=True)

    @classmethod
    def create(cls, name):
        bot = cls(name=name)
        return bot

    def __unicode__(self):
        return str(self.name)


class AttackDetails(models.Model):
    player = models.ForeignKey(Player, unique=False)
    robot = models.ForeignKey(Robot, unique=False)
    damage = models.FloatField()
    killing_blow = models.BooleanField()
    ecm_hits = models.PositiveSmallIntegerField()
    ecm_attempts = models.PositiveSmallIntegerField()
    demob = models.PositiveSmallIntegerField()
    suppress = models.PositiveSmallIntegerField()
    energy = models.FloatField()

    @classmethod
    def create(cls, player, robot, damage, killing_blow, ecm_hits, ecm_attempts, demob, suppress, energy):
        deets = cls(player=player, robot=robot, damage=damage, killing_blow=killing_blow,
                    ecm_hits=ecm_hits, ecm_attempts=ecm_attempts, demob=demob, suppress=suppress, energy=energy)
        return deets

    def __unicode__(self):
        return str(self.player)


class Kill(models.Model):
    date = models.DateTimeField()
    zone = models.ForeignKey(Zone)
    victim_agent = models.ForeignKey(Player)
    victim_robot = models.ForeignKey(Robot)
    attackers = models.ManyToManyField(AttackDetails)

    @classmethod
    def create(cls, date, zone, victim_agent, victim_robot, attackers):
        bot = cls(date=date, zone=zone, victim_agent=victim_agent, victim_robot=victim_robot, attackers=attackers)
        return bot

    def __unicode__(self):
        return str(
            str(self.date) + " " + str(self.zone) + " " + str(self.victim_agent) + " " + str(self.victim_robot))


class Kill_PureText(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return str(self.id)
