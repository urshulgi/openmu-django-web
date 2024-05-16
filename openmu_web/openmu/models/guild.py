# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Guild(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    hostilityid = models.ForeignKey(
        "self", models.DO_NOTHING, db_column="HostilityId", blank=True, null=True
    )  # Field name made lowercase.
    allianceguildid = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        db_column="AllianceGuildId",
        related_name="guild_allianceguildid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.CharField(
        db_column="Name", unique=True, max_length=8
    )  # Field name made lowercase.
    logo = models.BinaryField(
        db_column="Logo", blank=True, null=True
    )  # Field name made lowercase.
    score = models.IntegerField(db_column="Score")  # Field name made lowercase.
    notice = models.TextField(
        db_column="Notice", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Guild"


class Guildmember(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    guildid = models.ForeignKey(
        Guild, models.DO_NOTHING, db_column="GuildId"
    )  # Field name made lowercase.
    status = models.SmallIntegerField(db_column="Status")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GuildMember"
