# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Friend(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    characterid = models.UUIDField(
        db_column="CharacterId"
    )  # Field name made lowercase.
    friendid = models.UUIDField(db_column="FriendId")  # Field name made lowercase.
    accepted = models.BooleanField(db_column="Accepted")  # Field name made lowercase.
    requestopen = models.BooleanField(
        db_column="RequestOpen"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Friend"
        unique_together = (("characterid", "friendid"),)
