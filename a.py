class Rekins():
    def __init__(self,klients,veltijums,izmers,materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials
        self.aprekins()

    def izdrukat(self):
        print("Klients:",self.klients)
        print("Veltījums:",self.veltijums)
        print("Izmērs:", self.izmers)
        print("Materiāls:",self.materials)
        print("apmaksas summa",self.aprekins())

    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = (len(self.veltijums)) * 1.2 + (self.izmers[0]/100 * self.izmers[1]/100 * self.izmers[2]/100)/ 3 * self.materials
        PVN_summa = (produkta_cena + darba_samaksa)*PVN/100 
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        return rekina_summa


klints = input("ievadi vārdu:")
veltijums = input("ievadi vēlejumu?")
izmers = input ("Īevadi izmēru (platums,garums,augstums): ")
terminals = input("ievadi materiāla cen EUR/m2: ")

pirmais = Rekins("Anna","Lai izdodas!",[20,20,20],3.5)
pirmais.izdrukat()