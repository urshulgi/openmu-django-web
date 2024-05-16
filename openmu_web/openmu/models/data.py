# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    vaultid = models.OneToOneField(
        "Itemstorage", models.DO_NOTHING, db_column="VaultId", blank=True, null=True
    )  # Field name made lowercase.
    loginname = models.CharField(
        db_column="LoginName", unique=True, max_length=10
    )  # Field name made lowercase.
    passwordhash = models.TextField(
        db_column="PasswordHash"
    )  # Field name made lowercase.
    securitycode = models.TextField(
        db_column="SecurityCode"
    )  # Field name made lowercase.
    email = models.TextField(db_column="EMail")  # Field name made lowercase.
    registrationdate = models.DateTimeField(
        db_column="RegistrationDate"
    )  # Field name made lowercase.
    state = models.IntegerField(db_column="State")  # Field name made lowercase.
    timezone = models.SmallIntegerField(
        db_column="TimeZone"
    )  # Field name made lowercase.
    vaultpassword = models.TextField(
        db_column="VaultPassword"
    )  # Field name made lowercase.
    isvaultextended = models.BooleanField(
        db_column="IsVaultExtended"
    )  # Field name made lowercase.
    chatbanuntil = models.DateTimeField(
        db_column="ChatBanUntil", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Account"


class Accountcharacterclass(models.Model):
    accountid = models.OneToOneField(
        Account, models.DO_NOTHING, db_column="AccountId", primary_key=True
    )  # Field name made lowercase. The composite primary key (AccountId, CharacterClassId) found, that is not supported. The first column is selected.
    characterclassid = models.UUIDField(
        db_column="CharacterClassId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AccountCharacterClass"
        unique_together = (("accountid", "characterclassid"),)


class Appearancedata(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    characterclassid = models.UUIDField(
        db_column="CharacterClassId", blank=True, null=True
    )  # Field name made lowercase.
    pose = models.SmallIntegerField(db_column="Pose")  # Field name made lowercase.
    fullancientsetequipped = models.BooleanField(
        db_column="FullAncientSetEquipped"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AppearanceData"


class Character(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    characterclassid = models.UUIDField(
        db_column="CharacterClassId"
    )  # Field name made lowercase.
    currentmapid = models.UUIDField(
        db_column="CurrentMapId", blank=True, null=True
    )  # Field name made lowercase.
    inventoryid = models.OneToOneField(
        "Itemstorage", models.DO_NOTHING, db_column="InventoryId", blank=True, null=True
    )  # Field name made lowercase.
    accountid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column="AccountId", blank=True, null=True
    )  # Field name made lowercase.
    name = models.CharField(
        db_column="Name", unique=True, max_length=10
    )  # Field name made lowercase.
    characterslot = models.SmallIntegerField(
        db_column="CharacterSlot"
    )  # Field name made lowercase.
    createdate = models.DateTimeField(
        db_column="CreateDate"
    )  # Field name made lowercase.
    experience = models.BigIntegerField(
        db_column="Experience"
    )  # Field name made lowercase.
    masterexperience = models.BigIntegerField(
        db_column="MasterExperience"
    )  # Field name made lowercase.
    leveluppoints = models.IntegerField(
        db_column="LevelUpPoints"
    )  # Field name made lowercase.
    masterleveluppoints = models.IntegerField(
        db_column="MasterLevelUpPoints"
    )  # Field name made lowercase.
    positionx = models.SmallIntegerField(
        db_column="PositionX"
    )  # Field name made lowercase.
    positiony = models.SmallIntegerField(
        db_column="PositionY"
    )  # Field name made lowercase.
    playerkillcount = models.IntegerField(
        db_column="PlayerKillCount"
    )  # Field name made lowercase.
    stateremainingseconds = models.IntegerField(
        db_column="StateRemainingSeconds"
    )  # Field name made lowercase.
    state = models.IntegerField(db_column="State")  # Field name made lowercase.
    characterstatus = models.IntegerField(
        db_column="CharacterStatus"
    )  # Field name made lowercase.
    pose = models.SmallIntegerField(db_column="Pose")  # Field name made lowercase.
    usedfruitpoints = models.IntegerField(
        db_column="UsedFruitPoints"
    )  # Field name made lowercase.
    usednegfruitpoints = models.IntegerField(
        db_column="UsedNegFruitPoints"
    )  # Field name made lowercase.
    inventoryextensions = models.IntegerField(
        db_column="InventoryExtensions"
    )  # Field name made lowercase.
    keyconfiguration = models.BinaryField(
        db_column="KeyConfiguration", blank=True, null=True
    )  # Field name made lowercase.
    muhelperconfiguration = models.BinaryField(
        db_column="MuHelperConfiguration", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Character"


class Characterdropitemgroup(models.Model):
    characterid = models.OneToOneField(
        Character, models.DO_NOTHING, db_column="CharacterId", primary_key=True
    )  # Field name made lowercase. The composite primary key (CharacterId, DropItemGroupId) found, that is not supported. The first column is selected.
    dropitemgroupid = models.UUIDField(
        db_column="DropItemGroupId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CharacterDropItemGroup"
        unique_together = (("characterid", "dropitemgroupid"),)


class Characterqueststate(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    lastfinishedquestid = models.UUIDField(
        db_column="LastFinishedQuestId", blank=True, null=True
    )  # Field name made lowercase.
    activequestid = models.UUIDField(
        db_column="ActiveQuestId", blank=True, null=True
    )  # Field name made lowercase.
    characterid = models.ForeignKey(
        Character, models.DO_NOTHING, db_column="CharacterId", blank=True, null=True
    )  # Field name made lowercase.
    group = models.SmallIntegerField(db_column="Group")  # Field name made lowercase.
    clientactionperformed = models.BooleanField(
        db_column="ClientActionPerformed"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CharacterQuestState"


class Item(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemstorageid = models.ForeignKey(
        "Itemstorage",
        models.DO_NOTHING,
        db_column="ItemStorageId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    definitionid = models.UUIDField(
        db_column="DefinitionId", blank=True, null=True
    )  # Field name made lowercase.
    itemslot = models.SmallIntegerField(
        db_column="ItemSlot"
    )  # Field name made lowercase.
    durability = models.FloatField(db_column="Durability")  # Field name made lowercase.
    level = models.SmallIntegerField(db_column="Level")  # Field name made lowercase.
    hasskill = models.BooleanField(db_column="HasSkill")  # Field name made lowercase.
    socketcount = models.IntegerField(
        db_column="SocketCount"
    )  # Field name made lowercase.
    storeprice = models.IntegerField(
        db_column="StorePrice", blank=True, null=True
    )  # Field name made lowercase.
    petexperience = models.IntegerField(
        db_column="PetExperience"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Item"


class Itemappearance(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    definitionid = models.UUIDField(
        db_column="DefinitionId", blank=True, null=True
    )  # Field name made lowercase.
    appearancedataid = models.ForeignKey(
        Appearancedata,
        models.DO_NOTHING,
        db_column="AppearanceDataId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemslot = models.SmallIntegerField(
        db_column="ItemSlot"
    )  # Field name made lowercase.
    level = models.SmallIntegerField(db_column="Level")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemAppearance"


class Itemappearanceitemoptiontype(models.Model):
    itemappearanceid = models.OneToOneField(
        Itemappearance,
        models.DO_NOTHING,
        db_column="ItemAppearanceId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (ItemAppearanceId, ItemOptionTypeId) found, that is not supported. The first column is selected.
    itemoptiontypeid = models.UUIDField(
        db_column="ItemOptionTypeId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemAppearanceItemOptionType"
        unique_together = (("itemappearanceid", "itemoptiontypeid"),)


class Itemitemofitemset(models.Model):
    itemid = models.OneToOneField(
        Item, models.DO_NOTHING, db_column="ItemId", primary_key=True
    )  # Field name made lowercase. The composite primary key (ItemId, ItemOfItemSetId) found, that is not supported. The first column is selected.
    itemofitemsetid = models.UUIDField(
        db_column="ItemOfItemSetId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemItemOfItemSet"
        unique_together = (("itemid", "itemofitemsetid"),)


class Itemoptionlink(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemoptionid = models.UUIDField(
        db_column="ItemOptionId", blank=True, null=True
    )  # Field name made lowercase.
    itemid = models.ForeignKey(
        Item, models.DO_NOTHING, db_column="ItemId", blank=True, null=True
    )  # Field name made lowercase.
    level = models.IntegerField(db_column="Level")  # Field name made lowercase.
    index = models.IntegerField(db_column="Index")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemOptionLink"


class Itemstorage(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    money = models.IntegerField(db_column="Money")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemStorage"


class Letterbody(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    headerid = models.ForeignKey(
        "Letterheader", models.DO_NOTHING, db_column="HeaderId", blank=True, null=True
    )  # Field name made lowercase.
    senderappearanceid = models.OneToOneField(
        Appearancedata,
        models.DO_NOTHING,
        db_column="SenderAppearanceId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    message = models.TextField(db_column="Message")  # Field name made lowercase.
    rotation = models.SmallIntegerField(
        db_column="Rotation"
    )  # Field name made lowercase.
    animation = models.SmallIntegerField(
        db_column="Animation"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "LetterBody"


class Letterheader(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    receiverid = models.ForeignKey(
        Character, models.DO_NOTHING, db_column="ReceiverId"
    )  # Field name made lowercase.
    sendername = models.TextField(
        db_column="SenderName", blank=True, null=True
    )  # Field name made lowercase.
    subject = models.TextField(
        db_column="Subject", blank=True, null=True
    )  # Field name made lowercase.
    letterdate = models.DateTimeField(
        db_column="LetterDate"
    )  # Field name made lowercase.
    readflag = models.BooleanField(db_column="ReadFlag")  # Field name made lowercase.
    characterid = models.UUIDField(
        db_column="CharacterId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "LetterHeader"


class Minigamerankingentry(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    characterid = models.ForeignKey(
        Character, models.DO_NOTHING, db_column="CharacterId", blank=True, null=True
    )  # Field name made lowercase.
    minigameid = models.UUIDField(
        db_column="MiniGameId", blank=True, null=True
    )  # Field name made lowercase.
    gameinstanceid = models.UUIDField(
        db_column="GameInstanceId"
    )  # Field name made lowercase.
    timestamp = models.DateTimeField(
        db_column="Timestamp", blank=True, null=True
    )  # Field name made lowercase.
    score = models.IntegerField(db_column="Score")  # Field name made lowercase.
    rank = models.IntegerField(db_column="Rank")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MiniGameRankingEntry"


class Questmonsterkillrequirementstate(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    requirementid = models.UUIDField(
        db_column="RequirementId", blank=True, null=True
    )  # Field name made lowercase.
    characterqueststateid = models.ForeignKey(
        Characterqueststate,
        models.DO_NOTHING,
        db_column="CharacterQuestStateId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    killcount = models.IntegerField(db_column="KillCount")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "QuestMonsterKillRequirementState"


class Skillentry(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    skillid = models.UUIDField(
        db_column="SkillId", blank=True, null=True
    )  # Field name made lowercase.
    characterid = models.ForeignKey(
        Character, models.DO_NOTHING, db_column="CharacterId", blank=True, null=True
    )  # Field name made lowercase.
    level = models.IntegerField(db_column="Level")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SkillEntry"


class Statattribute(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    definitionid = models.UUIDField(
        db_column="DefinitionId", blank=True, null=True
    )  # Field name made lowercase.
    characterid = models.ForeignKey(
        Character, models.DO_NOTHING, db_column="CharacterId", blank=True, null=True
    )  # Field name made lowercase.
    value = models.FloatField(db_column="Value")  # Field name made lowercase.
    accountid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column="AccountId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "StatAttribute"
