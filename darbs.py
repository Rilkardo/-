import a
from a import Rekins

def datuIevade():
    klients = input("Ievadi vārdu: ")
    veltijums = input("Ievadi veltījumu: ")
    izmers = input("Ievadi izmēru (platums,garums,augstums): ")
    materials = input("Ievadi materiāla cenu EUR/m2: ")
    print('\n')
    dati = Rekins(klients,veltijums,izmers,materials)
    dati.saglabat()
    dati.izdrukat()

    print('\nApmaksas summa!\n')
while True:
    print('1 - Datu Ievade | 2 - Iziet')
    Izvele = input('Izvelaties darbibu: ')

    if Izvele == '1':
        datuIevade()
    elif Izvele == '2':
        break
    else:
        print('ievadiet velomo darbibas numuru!')
        continue

    