# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 5618399  # integer value, dont use ""
    API_HASH = "372f9b12937f0c2a9f0dcec966add011"
    TOKEN = "2028771505:AAHrhxSitTGraswkX-H5ZjhbuxBksRlr4p8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 412094015  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "mkspali"
    SUPPORT_CHAT = "BotMasterOfficial"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001594744091
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001515775622
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://pwdfmaewbdnpfg:ae1c844cc0769063709515dbc9a59a99faec0847676b06e1205cc523068b16ba@ec2-3-218-47-9.compute-1.amazonaws.com:5432/dc326anq31ratp"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "4tA8_mJUxa2s2wsffaN_xhzy1bDNFAFkVfvBLBCCfEAkS2VDeQhgadgo28RiAS6i"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "412094015"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "412094015"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "412094015"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "412094015"
    WOLVES = "412094015"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "OT6XX0IXFWMD9J9J"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "Key	M4RKSVS60811"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "hmmm"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "hmmm"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
