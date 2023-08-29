import json
from collections import Counter

MODELI_CEVLJEV = [
    "Air Jordan 1",
    "Nike Air Max 90",
    "Adidas Ultra Boost",
    # ... (dodajte druge modele čevljev tukaj)
]

VELIKOSTI_CEVLJEV = [
    36, 36.5, 37, 37.5, 38, 38.5, 39, 39.5, 40, 40.5,
    41, 41.5, 42, 42.5, 43, 43.5, 44, 44.5, 45, 46
    # ... (dodajte druge velikosti po potrebi)
]


IME_DATOTEKE = 'C:\\Matevz\\Projects\\Underground.stockX\\zaloga.json'


def nalozi_zalogo():
    try:
        with open(IME_DATOTEKE, 'r') as datoteka:
            return json.load(datoteka)
    except FileNotFoundError:
        return {}

def shrani_zalogo(zaloga):
    with open(IME_DATOTEKE, 'w') as datoteka:
        json.dump(zaloga, datoteka)

zaloga = nalozi_zalogo()

def prikazi_zalogo():
    print("zaloga:")
    for model, podatki in sorted(zaloga.items()):
        razvrscene_stevilke = sorted(podatki['stevilke'], key=float)
        print(f"Model: {model} - Število parov: {podatki['kolicina']}, Številke: {razvrscene_stevilke}")


def dodaj_v_zalogo():
    # Izberi model čevlja
    print("Izberi model čevlja:")
    for indeks, model in enumerate(MODELI_CEVLJEV, 1):
        print(f"{indeks}. {model}")

    izbira = int(input("Vpiši številko izbire: "))
    if 1 <= izbira <= len(MODELI_CEVLJEV):
        model = MODELI_CEVLJEV[izbira - 1].lower()
    else:
        print("Napačna izbira!")
        return

    stevilke = []
    while True:
        print("Izberi velikost čevlja:")
        for indeks, velikost in enumerate(VELIKOSTI_CEVLJEV, 1):
            print(f"{indeks}. {velikost}")

        izbira_velikosti = int(input(f"Vpiši številko izbire za dodajanje ali 0 za zaključek: "))
        if izbira_velikosti == 0:
            break
        if 1 <= izbira_velikosti <= len(VELIKOSTI_CEVLJEV):
            stevilke.append(VELIKOSTI_CEVLJEV[izbira_velikosti - 1])
        else:
            print("Napačna izbira velikosti. Poskusi znova.")

    kolicina = len(stevilke)

    if model in zaloga:
        zaloga[model]['kolicina'] += kolicina
        zaloga[model]['stevilke'].extend(stevilke)
    else:
        zaloga[model] = {'kolicina': kolicina, 'stevilke': stevilke}

    shrani_zalogo(zaloga)
    print("Dodano v zalogo!")





from collections import Counter

def odpisi_z_zaloge():
    # Izberi model čevlja
    print("Izberi model čevlja, ki ga želiš odpisati:")
    for indeks, model in enumerate(MODELI_CEVLJEV, 1):
        print(f"{indeks}. {model}")

    izbira = int(input("Vpiši številko izbire: "))
    if 1 <= izbira <= len(MODELI_CEVLJEV):
        model = MODELI_CEVLJEV[izbira - 1].lower()
    else:
        print("Napačna izbira!")
        return

    if model not in zaloga:
        print("Ta model ni v zalogi!")
        return

    # Izberi številke za odpis
    stevilke_za_odpis = []
    print("Izberi številke čevlja za odpis:")
    for indeks, velikost in enumerate(VELIKOSTI_CEVLJEV, 1):
        print(f"{indeks}. {velikost}")
    
    while True:
        izbira_velikosti = int(input(f"Vpiši številko izbire za odpis ali 0 za zaključek: "))
        if izbira_velikosti == 0:
            break
        if 1 <= izbira_velikosti <= len(VELIKOSTI_CEVLJEV):
            stevilke_za_odpis.append(VELIKOSTI_CEVLJEV[izbira_velikosti - 1])
        else:
            print("Napačna izbira velikosti. Poskusi znova.")

    odstranjene_stevilke = []

    # Odpis številk iz zaloge
    for stev in stevilke_za_odpis:
        if stev in zaloga[model]['stevilke']:
            zaloga[model]['stevilke'].remove(stev)
            zaloga[model]['kolicina'] -= 1
            odstranjene_stevilke.append(stev)

    # Prikaži, katere številke in kolikokrat so bile odstranjene
    odstranjene_stevilke_counter = Counter(odstranjene_stevilke)
    izpis = ", ".join(f"{stev} (x{krat})" for stev, krat in odstranjene_stevilke_counter.items())
    print(f"Odstranjene številke iz zaloge za model {model}: {izpis}")

    # Če so vse številke odstranjene, odstranimo tudi model iz zaloge
    if not zaloga[model]['stevilke']:
        del zaloga[model]
        print(f"Model {model} je bil odstranjen iz zaloge, ker ni več nobenih številk na voljo.")

    shrani_zalogo(zaloga)  # Shrani zalogo po odpisu

    

while True:
    print("\nIzberi možnost:")
    print("1. Prikaz zaloge")
    print("2. Dodaj v zalogo")
    print("3. Odpiši z zaloge")
    print("4. Izhod")
    izbira = input()

    if izbira == "1":
        prikazi_zalogo()
    elif izbira == "2":
        dodaj_v_zalogo()
    elif izbira == "3":
        odpisi_z_zaloge()
    elif izbira == "4":
        shrani_zalogo(zaloga)
        print("Ajcau!")
        break
