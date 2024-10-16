from datetime import datetime, timedelta 


class Knygos:
    def __init__(self, pavadinimas, autorius, metai, zanras, kiekis=2, isdavimo_data= None):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai 
        self.zanras = zanras
        self.kiekis = kiekis
        self.isdavimo_data = isdavimo_data # numatytasis None 

    def __repr__(self):
        return f"'{self.pavadinimas}', {self.autorius}, {self.metai}, {self.zanras}, Kiekis: {self.kiekis} {self.isdavimo_data}"
    

    def isduoti_knyga(self):
        if self.kiekis > 0:
            self.kiekis -= 1 
            self.isdavimo_data = datetime.now()
            return True
        return False
    
    def grazinti_knyga(self):
        if self.isdavimo_data:
            self.kiekis += 1 # grazinant knyga atstatomas kiekis
            self.isdavimo_data = None # nustatau, kad knyga nebeisduota
            return True 
        return False 
    
    def ar_veluoja(self, grazinimo_laikas_dienomis=30):
        if self.isdavimo_data:
            grazinimo_terminas = self.isdavimo_data + timedelta(days=grazinimo_laikas_dienomis)
            if datetime.now() > grazinimo_terminas:
                return datetime.now() > grazinimo_terminas
            return False
 
    

