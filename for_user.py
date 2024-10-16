from library import Biblioteka 
from datetime import datetime, timedelta

def main():
    biblioteka = Biblioteka()

# knygu nuskaitymas
    biblioteka.nuskaityti_knygas()

    while True: 
        print("\nPasirinkite veiksma:")
        print("1. Perziureti visas knygas")
        print("2. Pasiimti knyga")
        print("3. Grazinti knyga")
        print("4. Perziureti veluojancias knygas")
        print("5. Iseiti")


        pasirinkimas = input("Iveskite veiksma (1-5): ")


        if pasirinkimas == "1":

            biblioteka.perziureti_visas_knygas()

        elif pasirinkimas == "2":
            pavadinimas = input("Iveskite knygos, kuria norite grazinti pavadinima: ")
            
            biblioteka.grazinti_knyga(pavadinimas)

        elif pasirinkimas == "4":

            biblioteka.perziureti_veluojancias_knygas()

        elif pasirinkimas == "5":

            biblioteka.issaugoti_knygas()
            print("Programa uzdaroma.")
            break
        else:
            print("Netinkamas pasirinkimas, pabandykite dar karta.")
 
if __name__ == "__main__":
    main()