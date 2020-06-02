import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=138'

content = requests.get(url)

response = bs4.BeautifulSoup(content.text, "html.parser")

hasil = response.find("tr", "table_highlight")
semua = hasil.find_all("td")

shubuh = semua[1].contents[0]
dzuhur = semua[2].contents[0]
ashar = semua[3].contents[0]
maghrib = semua[4].contents[0]
isya = semua[5].contents[0]

print("JADWAL SHALAT MAJALENGKA")
print("=============")
print("SHUBUH :", shubuh)
print("DZUHUR :", dzuhur)
print("ASHAR :", ashar)
print("MAGHRIB :", maghrib)
print("ISYA :", isya)
print("=============")

