from book import Knygos


class Biblioteka: 
    def __init__(self):
        self.knygos = []

# knygos pridejimas 
    def prideti_knyga(self, pavadinimas, autorius, metai, zanras, kiekis=2):
        nauja_knyga = Knygos(pavadinimas, autorius, metai, zanras, kiekis=2)
        self.knygos.append(nauja_knyga)
        print(f"Knyga '{pavadinimas}' prideta i biblioteka")
        self.issaugoti_knygas()



# knygos pridejimas vartotojui 
    def prideti_knyga_vartotojui(self):
        pavadinimas = input("Iveskite knygos pavadinima: ")
        autorius = input("Iveskite knygos autoriu: ")
        metai = input("Iveskite knygos isleidimo metus: ")
        zanras = input("Iveskite knygos zanra: ")

        self.prideti_knyga(pavadinimas, autorius, metai, zanras)

# senu knygu pasalinimas pagal metus
    def pasalinti_knygas(self, metai_riba, knygu_failas="knygos.txt"):
        naujas_sarasas = [knyga for knyga in self.knygos if int(knyga.metai) > int(metai_riba)]
        pasalintos_knygos = len(self.knygos) - len(naujas_sarasas)
        self.knygos = naujas_sarasas
        print(f"Pasalinta {pasalintos_knygos} senesnes nei {metai_riba}.")
        self.issaugoti_knygas(knygu_failas)

# susikuriam tekstini failiuka ir issaugom knygas 
    def issaugoti_knygas(self, knygu_failas="knygos.txt"):
        with open(knygu_failas, "w", encoding="utf-8") as f:
            for knyga in self.knygos:
                print(f"Knyga {knyga.pavadinimas} issaugota")
                f.write(f"{knyga.pavadinimas}, {knyga.autorius}, {knyga.metai}, {knyga.zanras}, {knyga.kiekis}\n")

    def pasiimti_knyga(self, pavadinimas):
        if self.patikrinti_ar_knyga_veluojanti():
            print("Negalite pasiimti naujos knygos.")
            return False
        
        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas:
                if knyga.kiekis > 0: 
                    knyga.kiekis -= 1
                    print(f"Knyga {pavadinimas} isduota.")
                else:
                    print(f"Knygos {pavadinimas} siuo metu nera")


    def grazinti_knyga(self, pavadinimas):
        for knyga in self.biblioteka.knygos:
            if knyga.pavadinimas == pavadinimas:
                if knyga.grazinti_knyga():
                    print(f"Knyga '{pavadinimas}' grazinta.")
                else: 
                    print(f"Knyga '{pavadinimas}' nebuvo isduota.")
                return
            print(f"Knyga '{pavadinimas}' bibliotekoje nerasta.")



# panaudoti lower ivesciai
    def ieskoti_knygu(self, knygu_paieska = "", pagal= "pavadinimas"):
        if not self.knygos:
            print("Knygos nera")
            return
        rezultatai = []
        for knyga in self.knygos:
            if pagal == "pavadinimas" and knygu_paieska.lower() in knyga.pavadinimas.lower():
                rezultatai.append(knyga)
            elif pagal == "autorius" and knygu_paieska.lower() in knyga.autorius.lower():
                rezultatai.append(knyga)

        if rezultatai: 
            print ("Knyga rasta:")
            for knyga in rezultatai: 
                print(knyga)
        else: 
            print("Pagal sia paieska knygu nera")


# pakeisto saraso issaugojimas txt
    def nuskaityti_knygas(self, knygu_failas="knygos.txt"):
        try:
          with open(knygu_failas, "r", encoding="utf-8") as f:
              for eilute in f:
                  pavadinimas, autorius, metai, zanras, kiekis = eilute.strip().split(",")
                  self.knygos.append(Knygos(pavadinimas, autorius, metai, zanras, int(kiekis)))
        except FileNotFoundError: 
            print("Tokios knygos nera")


    def perziureti_visas_knygas(self):
        if not self.knygos:
            print("Knygu bibliotekoje nera.")
        else: 
            print("Visu knygu sarasas:")
            for knyga in self.knygos:
                print(knyga)

    def perziureti_veluojancias_knygas(self):
        veluojancios_knygos = [knyga for knyga in self.knygos if knyga.ar_veluoja()]
        
        if veluojancios_knygos:
            print("Veluojancios knygos:")
            for knyga in veluojancios_knygos:
                print(f"Knyga {knyga.pavadinimas} veluojama grazinti.")
        else:
            print("Nera veluojanciu knygu.")

    def patikrinti_ar_knyga_veluojanti(self):
        for knyga in self.knygos:
            if knyga.ar_veluoja():
                return True
            return False
        
    







        



    






