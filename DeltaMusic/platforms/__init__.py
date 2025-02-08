from .AnimeZey import AnimeZey
from .Apple import AppleAPI
from .Carbon import CarbonAPI
from .Resso import RessoAPI
from .Soundcloud import SoundAPI
from .Spotify import SpotifyAPI
from .Telegram import TeleAPI
from .Youtube import YouTubeAPI

class PlaTForms:
    def __init__(self):
        self.animezey = AnimeZey()
        self.apple = Apple()
        self.carbon = Carbon()
        self.saavn = Saavn()
        self.resso = Resso()
        self.soundcloud = SoundCloud()
        self.spotify = Spotify()
        self.telegram = Telegram()
        self.youtube = YouTube()