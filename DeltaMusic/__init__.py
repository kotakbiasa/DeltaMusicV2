from DeltaMusic.core.bot import Hotty
from DeltaMusic.core.dir import dirr
from DeltaMusic.core.git import git
from DeltaMusic.core.userbot import Userbot
from DeltaMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()

BOT_USERNAME = "DeltaStreamBot"  # Replace with the actual bot username

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "BRANDED_KUDI_BOT"  # connect music api key "Dont change it"

