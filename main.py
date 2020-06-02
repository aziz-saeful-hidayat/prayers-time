import bs4
import requests
from datetime import datetime, timedelta

url = 'https://jadwalsholat.pkpu.or.id/?id=138'

content = requests.get(url)

response = bs4.BeautifulSoup(content.text, "html.parser")

hasil = response.find("tr", "table_highlight")
semua = hasil.find_all("td")


shubuh = semua[1].contents[0]
shubuhtime = datetime.strptime(shubuh, '%H:%M')
imsaktime = shubuhtime + timedelta(minutes= -10)
dzuhur = semua[2].contents[0]
ashar = semua[3].contents[0]
maghrib = semua[4].contents[0]
isya = semua[5].contents[0]

print("JADWAL SHALAT MAJALENGKA")
print("=============")
print("IMSAK : %s:%s" % (imsaktime.hour, imsaktime.minute))
print("SHUBUH :", shubuh)
print("DZUHUR :", dzuhur)
print("ASHAR :", ashar)
print("MAGHRIB :", maghrib)
print("ISYA :", isya)
print("=============")
