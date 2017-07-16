from papirus import Papirus
from papirus import PapirusImage
from papirus import PapirusText
from papirus import PapirusTextPos
import time
from twython import TwythonStreamer

screen = Papirus()
image = PapirusImage()
text = PapirusTextPos()

TERMS = '#alembic'

#login codes

APP_KEY = 'xCR6gEUjadgEAuYH5Oh2ehvhT'
APP_SECRET = 'PyhW6JM0EfqUS1l6sER8O8pSmoJxM2vmfJ2pQgOblHO2fx0Bjr'
OAUTH_TOKEN = '20427648-xL2sPwZRpi2V7jxuLFYHxqsOw8FytIgi9KA0e1K9v'
OAUTH_TOKEN_SECRET = 'Xho6kqVa38S4kJ742mNi9pDALM4jqXEvZTeE5lUziWnrT'

#setup callback from twython streamer

class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        text.AddText("#alembic", 60, 20, Id="Start", invert=True)
                        time.sleep(5.0)
                        image.write('/home/pi/papirus/epapertrump.bmp')
#screen.update()

#time.sleep(5.0)




