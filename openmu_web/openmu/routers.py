from openmu.models.config import *
from openmu.models.data import *
from openmu.models.friend import *
from openmu.models.guild import *

CONFIG_ROUTED_MODELS = [
    Attributedefinition,
    Attributerelationship,
    Attributerequirement,
    Battlezonedefinition,
    Characterclass,
    Chatserverdefinition,
    Chatserverendpoint,
    Combinationbonusrequirement,
    Configurationupdate,
    Configurationupdatestate,
    Connectserverdefinition,
    Constvalueattribute,
    Dropitemgroup,
    Dropitemgroupitemdefinition,
    Entergate,
    Exitgate,
    Gameclientdefinition,
    Gameconfiguration,
    Gamemapdefinition,
    Gamemapdefinitiondropitemgroup,
    Gameserverconfiguration,
    Gameserverconfigurationgamemapdefinition,
    Gameserverdefinition,
    Gameserverendpoint,
    Increasableitemoption,
    Itembasepowerupdefinition,
    Itemcrafting,
    Itemcraftingrequireditem,
    Itemcraftingrequireditemitemdefinition,
    Itemcraftingrequireditemitemoptiontype,
    Itemcraftingresultitem,
    Itemdefinition,
    Itemdefinitioncharacterclass,
    Itemdefinitionitemoptiondefinition,
    Itemdefinitionitemsetgroup,
    Itemdropitemgroup,
    Itemdropitemgroupitemdefinition,
    Itemlevelbonustable,
    Itemofitemset,
    Itemoption,
    Itemoptioncombinationbonus,
    Itemoptiondefinition,
    Itemoptionoflevel,
    Itemoptiontype,
    Itemsetgroup,
    Itemslottype,
    Jewelmix,
    Levelbonus,
    Magiceffectdefinition,
    Masterskilldefinition,
    Masterskilldefinitionskill,
    Masterskillroot,
    Minigamechangeevent,
    Minigamedefinition,
    Minigamereward,
    Minigamespawnwave,
    Minigameterrainchange,
    Monsterattribute,
    Monsterdefinition,
    Monsterdefinitiondropitemgroup,
    Monsterspawnarea,
    Pluginconfiguration,
    Powerupdefinition,
    Powerupdefinitionvalue,
    Questdefinition,
    Questitemrequirement,
    Questmonsterkillrequirement,
    Questreward,
    Rectangle,
    Simplecraftingsettings,
    Skill,
    Skillcharacterclass,
    Skillcombodefinition,
    Skillcombostep,
    Statattributedefinition,
    Systemconfiguration,
    Warpinfo,
]

DATA_ROUTED_MODELS = [
    Account,
    Accountcharacterclass,
    Appearancedata,
    Character,
    Characterdropitemgroup,
    Characterqueststate,
    Item,
    Itemappearance,
    Itemappearanceitemoptiontype,
    Itemitemofitemset,
    Itemoptionlink,
    Itemstorage,
    Letterbody,
    Letterheader,
    Minigamerankingentry,
    Questmonsterkillrequirementstate,
    Skillentry,
    Statattribute,
]

FRIEND_ROUTED_MODELS = [
    Friend,
]

GUILD_ROUTED_MODELS = [
    Guild,
    Guildmember,
]


class DBConfigRouter(object):

    def db_for_read(self, model, **hints):
        if model in CONFIG_ROUTED_MODELS:
            return "config"
        return None

    def db_for_write(self, model, **hints):
        if model in CONFIG_ROUTED_MODELS:
            return "config"
        return None


class DBDataRouter(object):

    def db_for_read(self, model, **hints):
        if model in DATA_ROUTED_MODELS:
            return "data"
        return None

    def db_for_write(self, model, **hints):
        if model in DATA_ROUTED_MODELS:
            return "data"
        return None


class DBFriendRouter(object):

    def db_for_read(self, model, **hints):
        if model in FRIEND_ROUTED_MODELS:
            return "friend"
        return None

    def db_for_write(self, model, **hints):
        if model in FRIEND_ROUTED_MODELS:
            return "friend"
        return None


class DBGuildRouter(object):

    def db_for_read(self, model, **hints):
        if model in GUILD_ROUTED_MODELS:
            return "guild"
        return None

    def db_for_write(self, model, **hints):
        if model in GUILD_ROUTED_MODELS:
            return "guild"
        return None
