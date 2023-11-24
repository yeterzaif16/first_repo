# title(): Her kelimenin ilk harfini büyük yapar.
metin = "python uygulamaları kursu"

print(metin.title())

#upper()
buyuk_metin = metin.upper()
print(buyuk_metin)

#lower()
print(buyuk_metin.lower())

# capitalize()
buyuk_metin.capitalize()

# startswith(), endswith()
metin =" python uygulamaları kursu"

metin.startswith("python")
metin.endswith("kursu")
metin.endswith("su")

# find()
metin.find("t")    # 2.indeks
metin.find("u")    # 7.indeks

metin.find("uygulamaları")
metin.find("thon")
metin.find("p")    # -1 döndürür

# index()
metin.index("thon")
metin.index("p")    # ValueError: substring not found

# replace()
metin = "python uygulamaları kursu"
  yeni_metin = metin.replace("kursu", "eğitimi")
  print(yeni_metin)


# count(): belirtilen substringin kaç defa geçtiğini döndürür
e_mail = "salim@gmail.com, yeter@gmail.com"
e_mail.count("mail.com")

# swapcase(): büyük ve küçüklüğü terse çevir
metin = "BilgeAdam"
metin.swapcase()

# Join()
isim_listesi = ["Ali","Veli","Emel"]
", ".join(isim_listesi)

# Strings Methods Demo
website = "http://www.bilgeadam.com"
website[11:20]
website.split(".")[1]