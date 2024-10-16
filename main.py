from library import Biblioteka
from book import Knygos



biblioteka = Biblioteka()

biblioteka.prideti_knyga("'Karaliene Viktorija'", "Lucy Worsley", "2015", "drama")
biblioteka.prideti_knyga("'Drugeliu kambarys'", "Lucinda Riley", "2008", "romanas")
biblioteka.prideti_knyga("'Lizos butas'", "Vaiva Rykstaite", "2020", "romanas")
biblioteka.prideti_knyga("'Mes dedame taska'", "Colleen Hoover", "2024", "romanas")
biblioteka.prideti_knyga("'Svetimas'", "Albert Camus", "2024", "romanas")
biblioteka.prideti_knyga("'Jusu pasamones galia'", "Joseph Murphy", "2022", "saviugda")
biblioteka.prideti_knyga("'Alchemikas'", "Paulo Coelho", "1996", "romanas")
biblioteka.prideti_knyga("'Prancuziskas testamentas'", "Andrei Makine", "2022", "romanas")
biblioteka.prideti_knyga("'Viesnia'", "B.A. Paris", "2015", "romanas")
biblioteka.prideti_knyga("'Kaulu upe'", "JD Kirk", "2023", "trileris")

biblioteka.issaugoti_knygas()

biblioteka.pasalinti_knygas(1999)

biblioteka.prideti_knyga("'Rugiai'", "Antanas B", "1999", "romanas", )
biblioteka.knygos.append # isidesiu pavadinima veliau


biblioteka.nuskaityti_knygas("knygos.txt")

#knygu_paieska = input("Iveskite knygos pavadinima arba autoriu: ")
#biblioteka.ieskoti_knygu(knygu_paieska, pagal="pavadinimas")

biblioteka.issaugoti_knygas()




for knyga in biblioteka.knygos:
    if knyga.ar_veluoja():
        print(f"Knyga '{knyga.pavadinimas}' yra veluojanti.")
    else:
        print(f"Knyga '{knyga.pavadinimas}' dar nera veluojanti.")


biblioteka.nuskaityti_knygas()
biblioteka.perziureti_visas_knygas()

# veluojanciu knygu patikrinimas

pavadinimas = input("Iveskite knygos, kuria norite pasiimti pavadinima: ")
biblioteka.ieskoti_knygu(pavadinimas)
