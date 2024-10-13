from IshuXD.core.bot import Ishu
from IshuXD.core.dir import dirr
from IshuXD.core.git import git
from IshuXD.core.userbot import Userbot
from IshuXD.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Ishu()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
