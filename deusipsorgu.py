
#coded by DeusLorenzo
import requests, json

#Sorgu sonucu listelenecek başlıklar:
print ("IP","Ülke","İl","İlçe","Enlem","Boylam")

#Sorgulanacak ip lere ait liste:
ip = ["176.55.55.252","176.55.55.252","88.230.177.68","88.230.177.68"]
APIKEY = ""
#ip listesinin teker teker web servis üzerinden sorgulanması:
for x in ip:
  #Bu kısımda yer alan API_KEY'i https://ipstack.com/ adresine üye olarak temin edebilirsiniz.
  serviceURL = "http://api.ipapi.com/"+x+"?access_key="+APIKEY+"&output=json"  
  r = requests.get(serviceURL)
  y = json.loads(r.text)
  print(y["ip"],y["country_name"],y["region_name"],y["city"],y["latitude"],y["longitude"])  