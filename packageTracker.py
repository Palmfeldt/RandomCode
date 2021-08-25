#This was a package notifier test script. It works, but much like everything it could be improved - Palmfeldt 20-04-01
import requests, time, difflib
from bs4 import BeautifulSoup
from plyer.utils import platform
from plyer import notification


startadr = "https://hm.delivery-status.com/se/sv/?orderNo="
ordernum = "24554444"
url = startadr+ordernum
startpage = requests.get(url)
scrapedstart = BeautifulSoup(startpage.content, 'html.parser') #sorts with bs4

while True:
  time.sleep(1200)
  currentpage = requests.get(url)
  scrapedcurrent = BeautifulSoup(currentpage.content, 'html.parser') #sorts with bs4

  ##output_list = [li for li in difflib.ndiff(scrapedstart, scrapedcurrent) if li[0] != ' ']
  if scrapedstart != scrapedcurrent:
    print("UPDATE!!!")
    notification.notify(
    title='UPDATE!!!',
    message='THERE HAS BEEN A PACKAGE UPDATE',
    app_name='lol no',
    )
    break
  else:
    print("Shit is the same")
