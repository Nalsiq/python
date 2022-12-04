import webbrowser
import json
from urllib.request import urlopen

print("Poszukajmy strony")
site = input("Podaj adrtes URL strony: ")
era = input("Podaj rok miesiąc i dzien")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

try:
    old_site = data["archived_snapshots"] ["closest"] ["url"]
    print("Adres znalezionej kopi :", old_site)
    print("strona sie odpali w przeglodarce")
    webbrowser.open(old_site)
except:
    print("nie ma tej strony")
