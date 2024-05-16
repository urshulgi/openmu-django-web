# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attributedefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        "Gameconfiguration",
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    designation = models.TextField(
        db_column="Designation", blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AttributeDefinition"


class Attributerelationship(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    targetattributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="TargetAttributeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    inputattributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="InputAttributeId",
        related_name="attributerelationship_inputattributeid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    characterclassid = models.ForeignKey(
        "Characterclass",
        models.DO_NOTHING,
        db_column="CharacterClassId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    powerupdefinitionvalueid = models.ForeignKey(
        "Powerupdefinitionvalue",
        models.DO_NOTHING,
        db_column="PowerUpDefinitionValueId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    inputoperator = models.IntegerField(
        db_column="InputOperator"
    )  # Field name made lowercase.
    inputoperand = models.FloatField(
        db_column="InputOperand"
    )  # Field name made lowercase.
    operandattributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="OperandAttributeId",
        related_name="attributerelationship_operandattributeid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AttributeRelationship"


class Attributerequirement(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    attributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="AttributeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gamemapdefinitionid = models.ForeignKey(
        "Gamemapdefinition",
        models.DO_NOTHING,
        db_column="GameMapDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemdefinitionid = models.ForeignKey(
        "Itemdefinition",
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    skillid = models.ForeignKey(
        "Skill", models.DO_NOTHING, db_column="SkillId", blank=True, null=True
    )  # Field name made lowercase.
    skillid1 = models.ForeignKey(
        "Skill",
        models.DO_NOTHING,
        db_column="SkillId1",
        related_name="attributerequirement_skillid1_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    minimumvalue = models.IntegerField(
        db_column="MinimumValue"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AttributeRequirement"


class Battlezonedefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    groundid = models.OneToOneField(
        "Rectangle", models.DO_NOTHING, db_column="GroundId", blank=True, null=True
    )  # Field name made lowercase.
    leftgoalid = models.OneToOneField(
        "Rectangle",
        models.DO_NOTHING,
        db_column="LeftGoalId",
        related_name="battlezonedefinition_leftgoalid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    rightgoalid = models.OneToOneField(
        "Rectangle",
        models.DO_NOTHING,
        db_column="RightGoalId",
        related_name="battlezonedefinition_rightgoalid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    type = models.IntegerField(db_column="Type")  # Field name made lowercase.
    leftteamspawnpointx = models.SmallIntegerField(
        db_column="LeftTeamSpawnPointX", blank=True, null=True
    )  # Field name made lowercase.
    leftteamspawnpointy = models.SmallIntegerField(
        db_column="LeftTeamSpawnPointY"
    )  # Field name made lowercase.
    rightteamspawnpointx = models.SmallIntegerField(
        db_column="RightTeamSpawnPointX", blank=True, null=True
    )  # Field name made lowercase.
    rightteamspawnpointy = models.SmallIntegerField(
        db_column="RightTeamSpawnPointY"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "BattleZoneDefinition"


class Characterclass(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    nextgenerationclassid = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        db_column="NextGenerationClassId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    homemapid = models.ForeignKey(
        "Gamemapdefinition",
        models.DO_NOTHING,
        db_column="HomeMapId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        "Gameconfiguration",
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    cangetcreated = models.BooleanField(
        db_column="CanGetCreated"
    )  # Field name made lowercase.
    levelrequirementbycreation = models.SmallIntegerField(
        db_column="LevelRequirementByCreation"
    )  # Field name made lowercase.
    creationallowedflag = models.SmallIntegerField(
        db_column="CreationAllowedFlag"
    )  # Field name made lowercase.
    ismasterclass = models.BooleanField(
        db_column="IsMasterClass"
    )  # Field name made lowercase.
    levelwarprequirementreductionpercent = models.IntegerField(
        db_column="LevelWarpRequirementReductionPercent"
    )  # Field name made lowercase.
    fruitcalculation = models.IntegerField(
        db_column="FruitCalculation"
    )  # Field name made lowercase.
    combodefinitionid = models.OneToOneField(
        "Skillcombodefinition",
        models.DO_NOTHING,
        db_column="ComboDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CharacterClass"


class Chatserverdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    serverid = models.SmallIntegerField(
        db_column="ServerId"
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    maximumconnections = models.IntegerField(
        db_column="MaximumConnections"
    )  # Field name made lowercase.
    clienttimeout = models.DurationField(
        db_column="ClientTimeout"
    )  # Field name made lowercase.
    clientcleanupinterval = models.DurationField(
        db_column="ClientCleanUpInterval"
    )  # Field name made lowercase.
    roomcleanupinterval = models.DurationField(
        db_column="RoomCleanUpInterval"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ChatServerDefinition"


class Chatserverendpoint(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    clientid = models.ForeignKey(
        "Gameclientdefinition",
        models.DO_NOTHING,
        db_column="ClientId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    chatserverdefinitionid = models.ForeignKey(
        Chatserverdefinition,
        models.DO_NOTHING,
        db_column="ChatServerDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    networkport = models.IntegerField(
        db_column="NetworkPort"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ChatServerEndpoint"


class Combinationbonusrequirement(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    optiontypeid = models.ForeignKey(
        "Itemoptiontype",
        models.DO_NOTHING,
        db_column="OptionTypeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemoptioncombinationbonusid = models.ForeignKey(
        "Itemoptioncombinationbonus",
        models.DO_NOTHING,
        db_column="ItemOptionCombinationBonusId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    suboptiontype = models.IntegerField(
        db_column="SubOptionType"
    )  # Field name made lowercase.
    minimumcount = models.IntegerField(
        db_column="MinimumCount"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CombinationBonusRequirement"


class Configurationupdate(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    version = models.IntegerField(db_column="Version")  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description", blank=True, null=True
    )  # Field name made lowercase.
    createdat = models.DateTimeField(
        db_column="CreatedAt", blank=True, null=True
    )  # Field name made lowercase.
    installedat = models.DateTimeField(
        db_column="InstalledAt", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ConfigurationUpdate"


class Configurationupdatestate(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    initializationkey = models.TextField(
        db_column="InitializationKey", blank=True, null=True
    )  # Field name made lowercase.
    currentinstalledversion = models.IntegerField(
        db_column="CurrentInstalledVersion"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ConfigurationUpdateState"


class Connectserverdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    clientid = models.ForeignKey(
        "Gameclientdefinition",
        models.DO_NOTHING,
        db_column="ClientId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    serverid = models.SmallIntegerField(
        db_column="ServerId"
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    disconnectonunknownpacket = models.BooleanField(
        db_column="DisconnectOnUnknownPacket"
    )  # Field name made lowercase.
    maximumreceivesize = models.SmallIntegerField(
        db_column="MaximumReceiveSize"
    )  # Field name made lowercase.
    clientlistenerport = models.IntegerField(
        db_column="ClientListenerPort"
    )  # Field name made lowercase.
    timeout = models.DurationField(db_column="Timeout")  # Field name made lowercase.
    currentpatchversion = models.BinaryField(
        db_column="CurrentPatchVersion", blank=True, null=True
    )  # Field name made lowercase.
    patchaddress = models.TextField(
        db_column="PatchAddress"
    )  # Field name made lowercase.
    maxconnectionsperaddress = models.IntegerField(
        db_column="MaxConnectionsPerAddress"
    )  # Field name made lowercase.
    checkmaxconnectionsperaddress = models.BooleanField(
        db_column="CheckMaxConnectionsPerAddress"
    )  # Field name made lowercase.
    maxconnections = models.IntegerField(
        db_column="MaxConnections"
    )  # Field name made lowercase.
    listenerbacklog = models.IntegerField(
        db_column="ListenerBacklog"
    )  # Field name made lowercase.
    maxftprequests = models.IntegerField(
        db_column="MaxFtpRequests"
    )  # Field name made lowercase.
    maxiprequests = models.IntegerField(
        db_column="MaxIpRequests"
    )  # Field name made lowercase.
    maxserverlistrequests = models.IntegerField(
        db_column="MaxServerListRequests"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ConnectServerDefinition"


class Constvalueattribute(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    definitionid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="DefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    characterclassid = models.ForeignKey(
        Characterclass, models.DO_NOTHING, db_column="CharacterClassId"
    )  # Field name made lowercase.
    value = models.FloatField(db_column="Value")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ConstValueAttribute"


class Dropitemgroup(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    monsterid = models.ForeignKey(
        "Monsterdefinition",
        models.DO_NOTHING,
        db_column="MonsterId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        "Gameconfiguration",
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    chance = models.FloatField(db_column="Chance")  # Field name made lowercase.
    minimummonsterlevel = models.SmallIntegerField(
        db_column="MinimumMonsterLevel", blank=True, null=True
    )  # Field name made lowercase.
    maximummonsterlevel = models.SmallIntegerField(
        db_column="MaximumMonsterLevel", blank=True, null=True
    )  # Field name made lowercase.
    itemlevel = models.SmallIntegerField(
        db_column="ItemLevel", blank=True, null=True
    )  # Field name made lowercase.
    itemtype = models.IntegerField(db_column="ItemType")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "DropItemGroup"


class Dropitemgroupitemdefinition(models.Model):
    dropitemgroupid = models.OneToOneField(
        Dropitemgroup, models.DO_NOTHING, db_column="DropItemGroupId", primary_key=True
    )  # Field name made lowercase. The composite primary key (DropItemGroupId, ItemDefinitionId) found, that is not supported. The first column is selected.
    itemdefinitionid = models.ForeignKey(
        "Itemdefinition", models.DO_NOTHING, db_column="ItemDefinitionId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "DropItemGroupItemDefinition"
        unique_together = (("dropitemgroupid", "itemdefinitionid"),)


class Entergate(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    targetgateid = models.ForeignKey(
        "Exitgate", models.DO_NOTHING, db_column="TargetGateId", blank=True, null=True
    )  # Field name made lowercase.
    gamemapdefinitionid = models.ForeignKey(
        "Gamemapdefinition",
        models.DO_NOTHING,
        db_column="GameMapDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    x1 = models.SmallIntegerField(db_column="X1")  # Field name made lowercase.
    y1 = models.SmallIntegerField(db_column="Y1")  # Field name made lowercase.
    x2 = models.SmallIntegerField(db_column="X2")  # Field name made lowercase.
    y2 = models.SmallIntegerField(db_column="Y2")  # Field name made lowercase.
    levelrequirement = models.SmallIntegerField(
        db_column="LevelRequirement"
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "EnterGate"


class Exitgate(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    mapid = models.ForeignKey(
        "Gamemapdefinition", models.DO_NOTHING, db_column="MapId", blank=True, null=True
    )  # Field name made lowercase.
    x1 = models.SmallIntegerField(db_column="X1")  # Field name made lowercase.
    y1 = models.SmallIntegerField(db_column="Y1")  # Field name made lowercase.
    x2 = models.SmallIntegerField(db_column="X2")  # Field name made lowercase.
    y2 = models.SmallIntegerField(db_column="Y2")  # Field name made lowercase.
    direction = models.IntegerField(db_column="Direction")  # Field name made lowercase.
    isspawngate = models.BooleanField(
        db_column="IsSpawnGate"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ExitGate"


class Gameclientdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    season = models.SmallIntegerField(db_column="Season")  # Field name made lowercase.
    episode = models.SmallIntegerField(
        db_column="Episode"
    )  # Field name made lowercase.
    language = models.IntegerField(db_column="Language")  # Field name made lowercase.
    version = models.BinaryField(
        db_column="Version", blank=True, null=True
    )  # Field name made lowercase.
    serial = models.BinaryField(
        db_column="Serial", blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameClientDefinition"


class Gameconfiguration(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    maximumlevel = models.SmallIntegerField(
        db_column="MaximumLevel"
    )  # Field name made lowercase.
    maximummasterlevel = models.SmallIntegerField(
        db_column="MaximumMasterLevel"
    )  # Field name made lowercase.
    experiencerate = models.FloatField(
        db_column="ExperienceRate"
    )  # Field name made lowercase.
    minimummonsterlevelformasterexperience = models.SmallIntegerField(
        db_column="MinimumMonsterLevelForMasterExperience"
    )  # Field name made lowercase.
    inforange = models.SmallIntegerField(
        db_column="InfoRange"
    )  # Field name made lowercase.
    areaskillhitsplayer = models.BooleanField(
        db_column="AreaSkillHitsPlayer"
    )  # Field name made lowercase.
    maximuminventorymoney = models.IntegerField(
        db_column="MaximumInventoryMoney"
    )  # Field name made lowercase.
    maximumvaultmoney = models.IntegerField(
        db_column="MaximumVaultMoney"
    )  # Field name made lowercase.
    recoveryinterval = models.IntegerField(
        db_column="RecoveryInterval"
    )  # Field name made lowercase.
    maximumletters = models.IntegerField(
        db_column="MaximumLetters"
    )  # Field name made lowercase.
    lettersendprice = models.IntegerField(
        db_column="LetterSendPrice"
    )  # Field name made lowercase.
    maximumcharactersperaccount = models.SmallIntegerField(
        db_column="MaximumCharactersPerAccount"
    )  # Field name made lowercase.
    characternameregex = models.TextField(
        db_column="CharacterNameRegex", blank=True, null=True
    )  # Field name made lowercase.
    maximumpasswordlength = models.IntegerField(
        db_column="MaximumPasswordLength"
    )  # Field name made lowercase.
    maximumpartysize = models.SmallIntegerField(
        db_column="MaximumPartySize"
    )  # Field name made lowercase.
    shoulddropmoney = models.BooleanField(
        db_column="ShouldDropMoney"
    )  # Field name made lowercase.
    damageperoneitemdurability = models.FloatField(
        db_column="DamagePerOneItemDurability"
    )  # Field name made lowercase.
    damageperonepetdurability = models.FloatField(
        db_column="DamagePerOnePetDurability"
    )  # Field name made lowercase.
    hitsperoneitemdurability = models.FloatField(
        db_column="HitsPerOneItemDurability"
    )  # Field name made lowercase.
    itemdropduration = models.DurationField(
        db_column="ItemDropDuration"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameConfiguration"


class Gamemapdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    safezonemapid = models.ForeignKey(
        "self", models.DO_NOTHING, db_column="SafezoneMapId", blank=True, null=True
    )  # Field name made lowercase.
    battlezoneid = models.OneToOneField(
        Battlezonedefinition,
        models.DO_NOTHING,
        db_column="BattleZoneId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    terraindata = models.BinaryField(
        db_column="TerrainData", blank=True, null=True
    )  # Field name made lowercase.
    expmultiplier = models.FloatField(
        db_column="ExpMultiplier"
    )  # Field name made lowercase.
    discriminator = models.IntegerField(
        db_column="Discriminator"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameMapDefinition"


class Gamemapdefinitiondropitemgroup(models.Model):
    gamemapdefinitionid = models.OneToOneField(
        Gamemapdefinition,
        models.DO_NOTHING,
        db_column="GameMapDefinitionId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (GameMapDefinitionId, DropItemGroupId) found, that is not supported. The first column is selected.
    dropitemgroupid = models.ForeignKey(
        Dropitemgroup, models.DO_NOTHING, db_column="DropItemGroupId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameMapDefinitionDropItemGroup"
        unique_together = (("gamemapdefinitionid", "dropitemgroupid"),)


class Gameserverconfiguration(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    maximumplayers = models.SmallIntegerField(
        db_column="MaximumPlayers"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameServerConfiguration"


class Gameserverconfigurationgamemapdefinition(models.Model):
    gameserverconfigurationid = models.OneToOneField(
        Gameserverconfiguration,
        models.DO_NOTHING,
        db_column="GameServerConfigurationId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (GameServerConfigurationId, GameMapDefinitionId) found, that is not supported. The first column is selected.
    gamemapdefinitionid = models.ForeignKey(
        Gamemapdefinition, models.DO_NOTHING, db_column="GameMapDefinitionId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameServerConfigurationGameMapDefinition"
        unique_together = (("gameserverconfigurationid", "gamemapdefinitionid"),)


class Gameserverdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    serverconfigurationid = models.ForeignKey(
        Gameserverconfiguration,
        models.DO_NOTHING,
        db_column="ServerConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    serverid = models.SmallIntegerField(
        db_column="ServerID"
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    experiencerate = models.FloatField(
        db_column="ExperienceRate"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameServerDefinition"


class Gameserverendpoint(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    clientid = models.ForeignKey(
        Gameclientdefinition,
        models.DO_NOTHING,
        db_column="ClientId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameserverdefinitionid = models.ForeignKey(
        Gameserverdefinition,
        models.DO_NOTHING,
        db_column="GameServerDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    networkport = models.IntegerField(
        db_column="NetworkPort"
    )  # Field name made lowercase.
    alternativepublishedport = models.IntegerField(
        db_column="AlternativePublishedPort"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "GameServerEndpoint"


class Increasableitemoption(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    optiontypeid = models.ForeignKey(
        "Itemoptiontype",
        models.DO_NOTHING,
        db_column="OptionTypeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    powerupdefinitionid = models.OneToOneField(
        "Powerupdefinition",
        models.DO_NOTHING,
        db_column="PowerUpDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemoptiondefinitionid = models.ForeignKey(
        "Itemoptiondefinition",
        models.DO_NOTHING,
        db_column="ItemOptionDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemsetgroupid = models.ForeignKey(
        "Itemsetgroup",
        models.DO_NOTHING,
        db_column="ItemSetGroupId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.IntegerField(db_column="Number")  # Field name made lowercase.
    suboptiontype = models.IntegerField(
        db_column="SubOptionType"
    )  # Field name made lowercase.
    leveltype = models.IntegerField(db_column="LevelType")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "IncreasableItemOption"


class Itembasepowerupdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    targetattributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="TargetAttributeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    bonusperleveltableid = models.ForeignKey(
        "Itemlevelbonustable",
        models.DO_NOTHING,
        db_column="BonusPerLevelTableId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemdefinitionid = models.ForeignKey(
        "Itemdefinition",
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    basevalue = models.FloatField(db_column="BaseValue")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemBasePowerUpDefinition"


class Itemcrafting(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    simplecraftingsettingsid = models.OneToOneField(
        "Simplecraftingsettings",
        models.DO_NOTHING,
        db_column="SimpleCraftingSettingsId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    monsterdefinitionid = models.ForeignKey(
        "Monsterdefinition",
        models.DO_NOTHING,
        db_column="MonsterDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    itemcraftinghandlerclassname = models.TextField(
        db_column="ItemCraftingHandlerClassName"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemCrafting"


class Itemcraftingrequireditem(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    simplecraftingsettingsid = models.ForeignKey(
        "Simplecraftingsettings",
        models.DO_NOTHING,
        db_column="SimpleCraftingSettingsId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    minimumitemlevel = models.SmallIntegerField(
        db_column="MinimumItemLevel"
    )  # Field name made lowercase.
    maximumitemlevel = models.SmallIntegerField(
        db_column="MaximumItemLevel"
    )  # Field name made lowercase.
    minimumamount = models.SmallIntegerField(
        db_column="MinimumAmount"
    )  # Field name made lowercase.
    maximumamount = models.SmallIntegerField(
        db_column="MaximumAmount"
    )  # Field name made lowercase.
    successresult = models.IntegerField(
        db_column="SuccessResult"
    )  # Field name made lowercase.
    failresult = models.IntegerField(
        db_column="FailResult"
    )  # Field name made lowercase.
    npcpricedivisor = models.IntegerField(
        db_column="NpcPriceDivisor"
    )  # Field name made lowercase.
    addpercentage = models.SmallIntegerField(
        db_column="AddPercentage"
    )  # Field name made lowercase.
    reference = models.SmallIntegerField(
        db_column="Reference"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemCraftingRequiredItem"


class Itemcraftingrequireditemitemdefinition(models.Model):
    itemcraftingrequireditemid = models.OneToOneField(
        Itemcraftingrequireditem,
        models.DO_NOTHING,
        db_column="ItemCraftingRequiredItemId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (ItemCraftingRequiredItemId, ItemDefinitionId) found, that is not supported. The first column is selected.
    itemdefinitionid = models.ForeignKey(
        "Itemdefinition", models.DO_NOTHING, db_column="ItemDefinitionId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemCraftingRequiredItemItemDefinition"
        unique_together = (("itemcraftingrequireditemid", "itemdefinitionid"),)


class Itemcraftingrequireditemitemoptiontype(models.Model):
    itemcraftingrequireditemid = models.OneToOneField(
        Itemcraftingrequireditem,
        models.DO_NOTHING,
        db_column="ItemCraftingRequiredItemId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (ItemCraftingRequiredItemId, ItemOptionTypeId) found, that is not supported. The first column is selected.
    itemoptiontypeid = models.ForeignKey(
        "Itemoptiontype", models.DO_NOTHING, db_column="ItemOptionTypeId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemCraftingRequiredItemItemOptionType"
        unique_together = (("itemcraftingrequireditemid", "itemoptiontypeid"),)


class Itemcraftingresultitem(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemdefinitionid = models.ForeignKey(
        "Itemdefinition",
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    simplecraftingsettingsid = models.ForeignKey(
        "Simplecraftingsettings",
        models.DO_NOTHING,
        db_column="SimpleCraftingSettingsId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    randomminimumlevel = models.SmallIntegerField(
        db_column="RandomMinimumLevel"
    )  # Field name made lowercase.
    randommaximumlevel = models.SmallIntegerField(
        db_column="RandomMaximumLevel"
    )  # Field name made lowercase.
    durability = models.SmallIntegerField(
        db_column="Durability", blank=True, null=True
    )  # Field name made lowercase.
    reference = models.SmallIntegerField(
        db_column="Reference"
    )  # Field name made lowercase.
    addlevel = models.SmallIntegerField(
        db_column="AddLevel"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemCraftingResultItem"


class Itemdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemslotid = models.ForeignKey(
        "Itemslottype", models.DO_NOTHING, db_column="ItemSlotId", blank=True, null=True
    )  # Field name made lowercase.
    consumeeffectid = models.ForeignKey(
        "Magiceffectdefinition",
        models.DO_NOTHING,
        db_column="ConsumeEffectId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    skillid = models.ForeignKey(
        "Skill", models.DO_NOTHING, db_column="SkillId", blank=True, null=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    width = models.SmallIntegerField(db_column="Width")  # Field name made lowercase.
    height = models.SmallIntegerField(db_column="Height")  # Field name made lowercase.
    dropsfrommonsters = models.BooleanField(
        db_column="DropsFromMonsters"
    )  # Field name made lowercase.
    isammunition = models.BooleanField(
        db_column="IsAmmunition"
    )  # Field name made lowercase.
    isboundtocharacter = models.BooleanField(
        db_column="IsBoundToCharacter"
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    droplevel = models.SmallIntegerField(
        db_column="DropLevel"
    )  # Field name made lowercase.
    maximumitemlevel = models.SmallIntegerField(
        db_column="MaximumItemLevel"
    )  # Field name made lowercase.
    durability = models.SmallIntegerField(
        db_column="Durability"
    )  # Field name made lowercase.
    group = models.SmallIntegerField(db_column="Group")  # Field name made lowercase.
    value = models.IntegerField(db_column="Value")  # Field name made lowercase.
    maximumsockets = models.IntegerField(
        db_column="MaximumSockets"
    )  # Field name made lowercase.
    petexperienceformula = models.TextField(
        db_column="PetExperienceFormula", blank=True, null=True
    )  # Field name made lowercase.
    storagelimitpercharacter = models.IntegerField(
        db_column="StorageLimitPerCharacter"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemDefinition"


class Itemdefinitioncharacterclass(models.Model):
    itemdefinitionid = models.OneToOneField(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (ItemDefinitionId, CharacterClassId) found, that is not supported. The first column is selected.
    characterclassid = models.ForeignKey(
        Characterclass, models.DO_NOTHING, db_column="CharacterClassId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemDefinitionCharacterClass"
        unique_together = (("itemdefinitionid", "characterclassid"),)


class Itemdefinitionitemoptiondefinition(models.Model):
    itemdefinitionid = models.OneToOneField(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (ItemDefinitionId, ItemOptionDefinitionId) found, that is not supported. The first column is selected.
    itemoptiondefinitionid = models.ForeignKey(
        "Itemoptiondefinition", models.DO_NOTHING, db_column="ItemOptionDefinitionId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemDefinitionItemOptionDefinition"
        unique_together = (("itemdefinitionid", "itemoptiondefinitionid"),)


class Itemdefinitionitemsetgroup(models.Model):
    itemdefinitionid = models.OneToOneField(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (ItemDefinitionId, ItemSetGroupId) found, that is not supported. The first column is selected.
    itemsetgroupid = models.ForeignKey(
        "Itemsetgroup", models.DO_NOTHING, db_column="ItemSetGroupId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemDefinitionItemSetGroup"
        unique_together = (("itemdefinitionid", "itemsetgroupid"),)


class Itemdropitemgroup(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    monsterid = models.ForeignKey(
        "Monsterdefinition",
        models.DO_NOTHING,
        db_column="MonsterId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemdefinitionid = models.ForeignKey(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    chance = models.FloatField(db_column="Chance")  # Field name made lowercase.
    minimummonsterlevel = models.SmallIntegerField(
        db_column="MinimumMonsterLevel", blank=True, null=True
    )  # Field name made lowercase.
    maximummonsterlevel = models.SmallIntegerField(
        db_column="MaximumMonsterLevel", blank=True, null=True
    )  # Field name made lowercase.
    itemlevel = models.SmallIntegerField(
        db_column="ItemLevel", blank=True, null=True
    )  # Field name made lowercase.
    itemtype = models.IntegerField(db_column="ItemType")  # Field name made lowercase.
    sourceitemlevel = models.SmallIntegerField(
        db_column="SourceItemLevel"
    )  # Field name made lowercase.
    moneyamount = models.IntegerField(
        db_column="MoneyAmount"
    )  # Field name made lowercase.
    minimumlevel = models.SmallIntegerField(
        db_column="MinimumLevel"
    )  # Field name made lowercase.
    maximumlevel = models.SmallIntegerField(
        db_column="MaximumLevel"
    )  # Field name made lowercase.
    requiredcharacterlevel = models.SmallIntegerField(
        db_column="RequiredCharacterLevel"
    )  # Field name made lowercase.
    dropeffect = models.IntegerField(
        db_column="DropEffect"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemDropItemGroup"


class Itemdropitemgroupitemdefinition(models.Model):
    itemdropitemgroupid = models.OneToOneField(
        Itemdropitemgroup,
        models.DO_NOTHING,
        db_column="ItemDropItemGroupId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (ItemDropItemGroupId, ItemDefinitionId) found, that is not supported. The first column is selected.
    itemdefinitionid = models.ForeignKey(
        Itemdefinition, models.DO_NOTHING, db_column="ItemDefinitionId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemDropItemGroupItemDefinition"
        unique_together = (("itemdropitemgroupid", "itemdefinitionid"),)


class Itemlevelbonustable(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemLevelBonusTable"


class Itemofitemset(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemsetgroupid = models.ForeignKey(
        "Itemsetgroup",
        models.DO_NOTHING,
        db_column="ItemSetGroupId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    itemdefinitionid = models.ForeignKey(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="ItemDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    bonusoptionid = models.ForeignKey(
        Increasableitemoption,
        models.DO_NOTHING,
        db_column="BonusOptionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ancientsetdiscriminator = models.IntegerField(
        db_column="AncientSetDiscriminator"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemOfItemSet"


class Itemoption(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    optiontypeid = models.ForeignKey(
        "Itemoptiontype",
        models.DO_NOTHING,
        db_column="OptionTypeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    powerupdefinitionid = models.OneToOneField(
        "Powerupdefinition",
        models.DO_NOTHING,
        db_column="PowerUpDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.IntegerField(db_column="Number")  # Field name made lowercase.
    suboptiontype = models.IntegerField(
        db_column="SubOptionType"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemOption"


class Itemoptioncombinationbonus(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    bonusid = models.OneToOneField(
        "Powerupdefinition",
        models.DO_NOTHING,
        db_column="BonusId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    number = models.IntegerField(db_column="Number")  # Field name made lowercase.
    appliesmultipletimes = models.BooleanField(
        db_column="AppliesMultipleTimes"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemOptionCombinationBonus"


class Itemoptiondefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    addsrandomly = models.BooleanField(
        db_column="AddsRandomly"
    )  # Field name made lowercase.
    addchance = models.FloatField(db_column="AddChance")  # Field name made lowercase.
    maximumoptionsperitem = models.IntegerField(
        db_column="MaximumOptionsPerItem"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemOptionDefinition"


class Itemoptionoflevel(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    powerupdefinitionid = models.OneToOneField(
        "Powerupdefinition",
        models.DO_NOTHING,
        db_column="PowerUpDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    increasableitemoptionid = models.ForeignKey(
        Increasableitemoption,
        models.DO_NOTHING,
        db_column="IncreasableItemOptionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    level = models.IntegerField(db_column="Level")  # Field name made lowercase.
    requireditemlevel = models.IntegerField(
        db_column="RequiredItemLevel"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemOptionOfLevel"


class Itemoptiontype(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    isvisible = models.BooleanField(db_column="IsVisible")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemOptionType"


class Itemsetgroup(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    alwaysapplies = models.BooleanField(
        db_column="AlwaysApplies"
    )  # Field name made lowercase.
    countdistinct = models.BooleanField(
        db_column="CountDistinct"
    )  # Field name made lowercase.
    minimumitemcount = models.IntegerField(
        db_column="MinimumItemCount"
    )  # Field name made lowercase.
    setlevel = models.IntegerField(db_column="SetLevel")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemSetGroup"


class Itemslottype(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemslots = models.TextField(
        db_column="ItemSlots", blank=True, null=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ItemSlotType"


class Jewelmix(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    singlejewelid = models.ForeignKey(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="SingleJewelId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    mixedjewelid = models.ForeignKey(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="MixedJewelId",
        related_name="jewelmix_mixedjewelid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "JewelMix"


class Levelbonus(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemlevelbonustableid = models.ForeignKey(
        Itemlevelbonustable,
        models.DO_NOTHING,
        db_column="ItemLevelBonusTableId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    level = models.IntegerField(db_column="Level")  # Field name made lowercase.
    additionalvalue = models.FloatField(
        db_column="AdditionalValue"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "LevelBonus"


class Magiceffectdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    durationid = models.OneToOneField(
        "Powerupdefinitionvalue",
        models.DO_NOTHING,
        db_column="DurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    subtype = models.SmallIntegerField(
        db_column="SubType"
    )  # Field name made lowercase.
    informobservers = models.BooleanField(
        db_column="InformObservers"
    )  # Field name made lowercase.
    stopbydeath = models.BooleanField(
        db_column="StopByDeath"
    )  # Field name made lowercase.
    sendduration = models.BooleanField(
        db_column="SendDuration"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MagicEffectDefinition"


class Masterskilldefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    rootid = models.ForeignKey(
        "Masterskillroot", models.DO_NOTHING, db_column="RootId", blank=True, null=True
    )  # Field name made lowercase.
    targetattributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="TargetAttributeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    replacedskillid = models.ForeignKey(
        "Skill", models.DO_NOTHING, db_column="ReplacedSkillId", blank=True, null=True
    )  # Field name made lowercase.
    rank = models.SmallIntegerField(db_column="Rank")  # Field name made lowercase.
    maximumlevel = models.SmallIntegerField(
        db_column="MaximumLevel"
    )  # Field name made lowercase.
    minimumlevel = models.SmallIntegerField(
        db_column="MinimumLevel"
    )  # Field name made lowercase.
    valueformula = models.TextField(
        db_column="ValueFormula"
    )  # Field name made lowercase.
    displayvalueformula = models.TextField(
        db_column="DisplayValueFormula"
    )  # Field name made lowercase.
    aggregation = models.IntegerField(
        db_column="Aggregation"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MasterSkillDefinition"


class Masterskilldefinitionskill(models.Model):
    masterskilldefinitionid = models.OneToOneField(
        Masterskilldefinition,
        models.DO_NOTHING,
        db_column="MasterSkillDefinitionId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (MasterSkillDefinitionId, SkillId) found, that is not supported. The first column is selected.
    skillid = models.ForeignKey(
        "Skill", models.DO_NOTHING, db_column="SkillId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MasterSkillDefinitionSkill"
        unique_together = (("masterskilldefinitionid", "skillid"),)


class Masterskillroot(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MasterSkillRoot"


class Minigamechangeevent(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    targetdefinitionid = models.ForeignKey(
        "Monsterdefinition",
        models.DO_NOTHING,
        db_column="TargetDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    spawnareaid = models.OneToOneField(
        "Monsterspawnarea",
        models.DO_NOTHING,
        db_column="SpawnAreaId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    minigamedefinitionid = models.ForeignKey(
        "Minigamedefinition",
        models.DO_NOTHING,
        db_column="MiniGameDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    index = models.IntegerField(db_column="Index")  # Field name made lowercase.
    description = models.TextField(
        db_column="Description", blank=True, null=True
    )  # Field name made lowercase.
    message = models.TextField(
        db_column="Message", blank=True, null=True
    )  # Field name made lowercase.
    target = models.IntegerField(db_column="Target")  # Field name made lowercase.
    minimumtargetlevel = models.SmallIntegerField(
        db_column="MinimumTargetLevel", blank=True, null=True
    )  # Field name made lowercase.
    numberofkills = models.SmallIntegerField(
        db_column="NumberOfKills"
    )  # Field name made lowercase.
    multiplykillsbyplayers = models.BooleanField(
        db_column="MultiplyKillsByPlayers"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MiniGameChangeEvent"


class Minigamedefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    entranceid = models.ForeignKey(
        Exitgate, models.DO_NOTHING, db_column="EntranceId", blank=True, null=True
    )  # Field name made lowercase.
    ticketitemid = models.ForeignKey(
        Itemdefinition,
        models.DO_NOTHING,
        db_column="TicketItemId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    type = models.IntegerField(db_column="Type")  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    description = models.TextField(
        db_column="Description"
    )  # Field name made lowercase.
    gamelevel = models.SmallIntegerField(
        db_column="GameLevel"
    )  # Field name made lowercase.
    mapcreationpolicy = models.IntegerField(
        db_column="MapCreationPolicy"
    )  # Field name made lowercase.
    enterduration = models.DurationField(
        db_column="EnterDuration"
    )  # Field name made lowercase.
    gameduration = models.DurationField(
        db_column="GameDuration"
    )  # Field name made lowercase.
    exitduration = models.DurationField(
        db_column="ExitDuration"
    )  # Field name made lowercase.
    maximumplayercount = models.IntegerField(
        db_column="MaximumPlayerCount"
    )  # Field name made lowercase.
    saverankingstatistics = models.BooleanField(
        db_column="SaveRankingStatistics"
    )  # Field name made lowercase.
    requiresmasterclass = models.BooleanField(
        db_column="RequiresMasterClass"
    )  # Field name made lowercase.
    minimumcharacterlevel = models.IntegerField(
        db_column="MinimumCharacterLevel"
    )  # Field name made lowercase.
    maximumcharacterlevel = models.IntegerField(
        db_column="MaximumCharacterLevel"
    )  # Field name made lowercase.
    minimumspecialcharacterlevel = models.IntegerField(
        db_column="MinimumSpecialCharacterLevel"
    )  # Field name made lowercase.
    maximumspecialcharacterlevel = models.IntegerField(
        db_column="MaximumSpecialCharacterLevel"
    )  # Field name made lowercase.
    ticketitemlevel = models.IntegerField(
        db_column="TicketItemLevel"
    )  # Field name made lowercase.
    allowparty = models.BooleanField(
        db_column="AllowParty"
    )  # Field name made lowercase.
    areplayerkillersallowedtoenter = models.BooleanField(
        db_column="ArePlayerKillersAllowedToEnter"
    )  # Field name made lowercase.
    entrancefee = models.IntegerField(
        db_column="EntranceFee"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MiniGameDefinition"


class Minigamereward(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemrewardid = models.ForeignKey(
        Dropitemgroup,
        models.DO_NOTHING,
        db_column="ItemRewardId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    requiredkillid = models.ForeignKey(
        "Monsterdefinition",
        models.DO_NOTHING,
        db_column="RequiredKillId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    minigamedefinitionid = models.ForeignKey(
        Minigamedefinition,
        models.DO_NOTHING,
        db_column="MiniGameDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    rank = models.IntegerField(
        db_column="Rank", blank=True, null=True
    )  # Field name made lowercase.
    rewardtype = models.IntegerField(
        db_column="RewardType"
    )  # Field name made lowercase.
    rewardamount = models.IntegerField(
        db_column="RewardAmount"
    )  # Field name made lowercase.
    requiredsuccess = models.IntegerField(
        db_column="RequiredSuccess"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MiniGameReward"


class Minigamespawnwave(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    minigamedefinitionid = models.ForeignKey(
        Minigamedefinition,
        models.DO_NOTHING,
        db_column="MiniGameDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    wavenumber = models.SmallIntegerField(
        db_column="WaveNumber"
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description", blank=True, null=True
    )  # Field name made lowercase.
    message = models.TextField(
        db_column="Message", blank=True, null=True
    )  # Field name made lowercase.
    starttime = models.DurationField(
        db_column="StartTime"
    )  # Field name made lowercase.
    endtime = models.DurationField(db_column="EndTime")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MiniGameSpawnWave"


class Minigameterrainchange(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    minigamechangeeventid = models.ForeignKey(
        Minigamechangeevent,
        models.DO_NOTHING,
        db_column="MiniGameChangeEventId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    terrainattribute = models.IntegerField(
        db_column="TerrainAttribute"
    )  # Field name made lowercase.
    setterrainattribute = models.BooleanField(
        db_column="SetTerrainAttribute"
    )  # Field name made lowercase.
    startx = models.SmallIntegerField(db_column="StartX")  # Field name made lowercase.
    starty = models.SmallIntegerField(db_column="StartY")  # Field name made lowercase.
    endx = models.SmallIntegerField(db_column="EndX")  # Field name made lowercase.
    endy = models.SmallIntegerField(db_column="EndY")  # Field name made lowercase.
    isclientupdaterequired = models.BooleanField(
        db_column="IsClientUpdateRequired"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MiniGameTerrainChange"


class Monsterattribute(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    attributedefinitionid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="AttributeDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    monsterdefinitionid = models.ForeignKey(
        "Monsterdefinition",
        models.DO_NOTHING,
        db_column="MonsterDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    value = models.FloatField(db_column="Value")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MonsterAttribute"


class Monsterdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    attackskillid = models.ForeignKey(
        "Skill", models.DO_NOTHING, db_column="AttackSkillId", blank=True, null=True
    )  # Field name made lowercase.
    merchantstoreid = models.UUIDField(
        db_column="MerchantStoreId", unique=True, blank=True, null=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    designation = models.TextField(
        db_column="Designation"
    )  # Field name made lowercase.
    moverange = models.SmallIntegerField(
        db_column="MoveRange"
    )  # Field name made lowercase.
    attackrange = models.SmallIntegerField(
        db_column="AttackRange"
    )  # Field name made lowercase.
    viewrange = models.SmallIntegerField(
        db_column="ViewRange"
    )  # Field name made lowercase.
    movedelay = models.DurationField(
        db_column="MoveDelay"
    )  # Field name made lowercase.
    attackdelay = models.DurationField(
        db_column="AttackDelay"
    )  # Field name made lowercase.
    respawndelay = models.DurationField(
        db_column="RespawnDelay"
    )  # Field name made lowercase.
    attribute = models.SmallIntegerField(
        db_column="Attribute"
    )  # Field name made lowercase.
    numberofmaximumitemdrops = models.IntegerField(
        db_column="NumberOfMaximumItemDrops"
    )  # Field name made lowercase.
    npcwindow = models.IntegerField(db_column="NpcWindow")  # Field name made lowercase.
    objectkind = models.IntegerField(
        db_column="ObjectKind"
    )  # Field name made lowercase.
    intelligencetypename = models.TextField(
        db_column="IntelligenceTypeName", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MonsterDefinition"


class Monsterdefinitiondropitemgroup(models.Model):
    monsterdefinitionid = models.OneToOneField(
        Monsterdefinition,
        models.DO_NOTHING,
        db_column="MonsterDefinitionId",
        primary_key=True,
    )  # Field name made lowercase. The composite primary key (MonsterDefinitionId, DropItemGroupId) found, that is not supported. The first column is selected.
    dropitemgroupid = models.ForeignKey(
        Dropitemgroup, models.DO_NOTHING, db_column="DropItemGroupId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MonsterDefinitionDropItemGroup"
        unique_together = (("monsterdefinitionid", "dropitemgroupid"),)


class Monsterspawnarea(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    monsterdefinitionid = models.ForeignKey(
        Monsterdefinition,
        models.DO_NOTHING,
        db_column="MonsterDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gamemapid = models.ForeignKey(
        Gamemapdefinition,
        models.DO_NOTHING,
        db_column="GameMapId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    x1 = models.SmallIntegerField(db_column="X1")  # Field name made lowercase.
    y1 = models.SmallIntegerField(db_column="Y1")  # Field name made lowercase.
    x2 = models.SmallIntegerField(db_column="X2")  # Field name made lowercase.
    y2 = models.SmallIntegerField(db_column="Y2")  # Field name made lowercase.
    direction = models.IntegerField(db_column="Direction")  # Field name made lowercase.
    quantity = models.SmallIntegerField(
        db_column="Quantity"
    )  # Field name made lowercase.
    spawntrigger = models.IntegerField(
        db_column="SpawnTrigger"
    )  # Field name made lowercase.
    wavenumber = models.SmallIntegerField(
        db_column="WaveNumber"
    )  # Field name made lowercase.
    maximumhealthoverride = models.IntegerField(
        db_column="MaximumHealthOverride", blank=True, null=True
    )  # Field name made lowercase.
    gamemapdefinitionid = models.ForeignKey(
        Gamemapdefinition,
        models.DO_NOTHING,
        db_column="GameMapDefinitionId",
        related_name="monsterspawnarea_gamemapdefinitionid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "MonsterSpawnArea"


class Pluginconfiguration(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    typeid = models.UUIDField(db_column="TypeId")  # Field name made lowercase.
    isactive = models.BooleanField(db_column="IsActive")  # Field name made lowercase.
    custompluginsource = models.TextField(
        db_column="CustomPlugInSource", blank=True, null=True
    )  # Field name made lowercase.
    externalassemblyname = models.TextField(
        db_column="ExternalAssemblyName", blank=True, null=True
    )  # Field name made lowercase.
    customconfiguration = models.TextField(
        db_column="CustomConfiguration", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "PlugInConfiguration"


class Powerupdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    targetattributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="TargetAttributeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    boostid = models.OneToOneField(
        "Powerupdefinitionvalue",
        models.DO_NOTHING,
        db_column="BoostId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    magiceffectdefinitionid = models.ForeignKey(
        Magiceffectdefinition,
        models.DO_NOTHING,
        db_column="MagicEffectDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gamemapdefinitionid = models.ForeignKey(
        Gamemapdefinition,
        models.DO_NOTHING,
        db_column="GameMapDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "PowerUpDefinition"


class Powerupdefinitionvalue(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    value = models.FloatField(db_column="Value")  # Field name made lowercase.
    aggregatetype = models.IntegerField(
        db_column="AggregateType"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "PowerUpDefinitionValue"


class Questdefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    questgiverid = models.ForeignKey(
        Monsterdefinition,
        models.DO_NOTHING,
        db_column="QuestGiverId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    qualifiedcharacterid = models.ForeignKey(
        Characterclass,
        models.DO_NOTHING,
        db_column="QualifiedCharacterId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    monsterdefinitionid = models.ForeignKey(
        Monsterdefinition,
        models.DO_NOTHING,
        db_column="MonsterDefinitionId",
        related_name="questdefinition_monsterdefinitionid_set",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    group = models.SmallIntegerField(db_column="Group")  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    startingnumber = models.SmallIntegerField(
        db_column="StartingNumber"
    )  # Field name made lowercase.
    refusenumber = models.SmallIntegerField(
        db_column="RefuseNumber"
    )  # Field name made lowercase.
    repeatable = models.BooleanField(
        db_column="Repeatable"
    )  # Field name made lowercase.
    requiresclientaction = models.BooleanField(
        db_column="RequiresClientAction"
    )  # Field name made lowercase.
    requiredstartmoney = models.IntegerField(
        db_column="RequiredStartMoney"
    )  # Field name made lowercase.
    minimumcharacterlevel = models.IntegerField(
        db_column="MinimumCharacterLevel"
    )  # Field name made lowercase.
    maximumcharacterlevel = models.IntegerField(
        db_column="MaximumCharacterLevel"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "QuestDefinition"


class Questitemrequirement(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemid = models.ForeignKey(
        Itemdefinition, models.DO_NOTHING, db_column="ItemId", blank=True, null=True
    )  # Field name made lowercase.
    dropitemgroupid = models.ForeignKey(
        Dropitemgroup,
        models.DO_NOTHING,
        db_column="DropItemGroupId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    questdefinitionid = models.ForeignKey(
        Questdefinition,
        models.DO_NOTHING,
        db_column="QuestDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    minimumnumber = models.IntegerField(
        db_column="MinimumNumber"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "QuestItemRequirement"


class Questmonsterkillrequirement(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    monsterid = models.ForeignKey(
        Monsterdefinition,
        models.DO_NOTHING,
        db_column="MonsterId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    questdefinitionid = models.ForeignKey(
        Questdefinition,
        models.DO_NOTHING,
        db_column="QuestDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    minimumnumber = models.IntegerField(
        db_column="MinimumNumber"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "QuestMonsterKillRequirement"


class Questreward(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    itemrewardid = models.UUIDField(
        db_column="ItemRewardId", unique=True, blank=True, null=True
    )  # Field name made lowercase.
    attributerewardid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="AttributeRewardId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    skillrewardid = models.ForeignKey(
        "Skill", models.DO_NOTHING, db_column="SkillRewardId", blank=True, null=True
    )  # Field name made lowercase.
    questdefinitionid = models.ForeignKey(
        Questdefinition,
        models.DO_NOTHING,
        db_column="QuestDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    rewardtype = models.IntegerField(
        db_column="RewardType"
    )  # Field name made lowercase.
    value = models.IntegerField(db_column="Value")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "QuestReward"


class Rectangle(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    x1 = models.SmallIntegerField(db_column="X1")  # Field name made lowercase.
    y1 = models.SmallIntegerField(db_column="Y1")  # Field name made lowercase.
    x2 = models.SmallIntegerField(db_column="X2")  # Field name made lowercase.
    y2 = models.SmallIntegerField(db_column="Y2")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Rectangle"


class Simplecraftingsettings(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    money = models.IntegerField(db_column="Money")  # Field name made lowercase.
    moneyperfinalsuccesspercentage = models.IntegerField(
        db_column="MoneyPerFinalSuccessPercentage"
    )  # Field name made lowercase.
    successpercent = models.SmallIntegerField(
        db_column="SuccessPercent"
    )  # Field name made lowercase.
    maximumsuccesspercent = models.SmallIntegerField(
        db_column="MaximumSuccessPercent"
    )  # Field name made lowercase.
    multipleallowed = models.BooleanField(
        db_column="MultipleAllowed"
    )  # Field name made lowercase.
    resultitemselect = models.IntegerField(
        db_column="ResultItemSelect"
    )  # Field name made lowercase.
    successpercentageadditionforluck = models.IntegerField(
        db_column="SuccessPercentageAdditionForLuck"
    )  # Field name made lowercase.
    successpercentageadditionforexcellentitem = models.IntegerField(
        db_column="SuccessPercentageAdditionForExcellentItem"
    )  # Field name made lowercase.
    successpercentageadditionforancientitem = models.IntegerField(
        db_column="SuccessPercentageAdditionForAncientItem"
    )  # Field name made lowercase.
    successpercentageadditionforsocketitem = models.IntegerField(
        db_column="SuccessPercentageAdditionForSocketItem"
    )  # Field name made lowercase.
    resultitemluckoptionchance = models.SmallIntegerField(
        db_column="ResultItemLuckOptionChance"
    )  # Field name made lowercase.
    resultitemskillchance = models.SmallIntegerField(
        db_column="ResultItemSkillChance"
    )  # Field name made lowercase.
    resultitemexcellentoptionchance = models.SmallIntegerField(
        db_column="ResultItemExcellentOptionChance"
    )  # Field name made lowercase.
    resultitemmaxexcoptioncount = models.SmallIntegerField(
        db_column="ResultItemMaxExcOptionCount"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SimpleCraftingSettings"


class Skill(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    elementalmodifiertargetid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="ElementalModifierTargetId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    magiceffectdefid = models.ForeignKey(
        Magiceffectdefinition,
        models.DO_NOTHING,
        db_column="MagicEffectDefId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    masterdefinitionid = models.OneToOneField(
        Masterskilldefinition,
        models.DO_NOTHING,
        db_column="MasterDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    number = models.SmallIntegerField(db_column="Number")  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    range = models.SmallIntegerField(db_column="Range")  # Field name made lowercase.
    damagetype = models.IntegerField(
        db_column="DamageType"
    )  # Field name made lowercase.
    skilltype = models.IntegerField(db_column="SkillType")  # Field name made lowercase.
    target = models.IntegerField(db_column="Target")  # Field name made lowercase.
    implicittargetrange = models.SmallIntegerField(
        db_column="ImplicitTargetRange"
    )  # Field name made lowercase.
    targetrestriction = models.IntegerField(
        db_column="TargetRestriction"
    )  # Field name made lowercase.
    movestotarget = models.BooleanField(
        db_column="MovesToTarget"
    )  # Field name made lowercase.
    movestarget = models.BooleanField(
        db_column="MovesTarget"
    )  # Field name made lowercase.
    attackdamage = models.IntegerField(
        db_column="AttackDamage"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Skill"


class Skillcharacterclass(models.Model):
    skillid = models.OneToOneField(
        Skill, models.DO_NOTHING, db_column="SkillId", primary_key=True
    )  # Field name made lowercase. The composite primary key (SkillId, CharacterClassId) found, that is not supported. The first column is selected.
    characterclassid = models.ForeignKey(
        Characterclass, models.DO_NOTHING, db_column="CharacterClassId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SkillCharacterClass"
        unique_together = (("skillid", "characterclassid"),)


class Skillcombodefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    maximumcompletiontime = models.DurationField(
        db_column="MaximumCompletionTime"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SkillComboDefinition"


class Skillcombostep(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    skillid = models.ForeignKey(
        Skill, models.DO_NOTHING, db_column="SkillId", blank=True, null=True
    )  # Field name made lowercase.
    skillcombodefinitionid = models.ForeignKey(
        Skillcombodefinition,
        models.DO_NOTHING,
        db_column="SkillComboDefinitionId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    order = models.IntegerField(db_column="Order")  # Field name made lowercase.
    isfinalstep = models.BooleanField(
        db_column="IsFinalStep"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SkillComboStep"


class Statattributedefinition(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    attributeid = models.ForeignKey(
        Attributedefinition,
        models.DO_NOTHING,
        db_column="AttributeId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    characterclassid = models.ForeignKey(
        Characterclass,
        models.DO_NOTHING,
        db_column="CharacterClassId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    basevalue = models.FloatField(db_column="BaseValue")  # Field name made lowercase.
    increasablebyplayer = models.BooleanField(
        db_column="IncreasableByPlayer"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "StatAttributeDefinition"


class Systemconfiguration(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    ipresolver = models.IntegerField(
        db_column="IpResolver"
    )  # Field name made lowercase.
    ipresolverparameter = models.TextField(
        db_column="IpResolverParameter", blank=True, null=True
    )  # Field name made lowercase.
    autostart = models.BooleanField(db_column="AutoStart")  # Field name made lowercase.
    autoupdateschema = models.BooleanField(
        db_column="AutoUpdateSchema"
    )  # Field name made lowercase.
    readconsoleinput = models.BooleanField(
        db_column="ReadConsoleInput"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "SystemConfiguration"


class Warpinfo(models.Model):
    id = models.UUIDField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    gateid = models.ForeignKey(
        Exitgate, models.DO_NOTHING, db_column="GateId", blank=True, null=True
    )  # Field name made lowercase.
    gameconfigurationid = models.ForeignKey(
        Gameconfiguration,
        models.DO_NOTHING,
        db_column="GameConfigurationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    index = models.IntegerField(db_column="Index")  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    costs = models.IntegerField(db_column="Costs")  # Field name made lowercase.
    levelrequirement = models.IntegerField(
        db_column="LevelRequirement"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "WarpInfo"
