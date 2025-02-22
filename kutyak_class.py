import random

class Kutya:
    def __init__(self, nev):
        self.nev = nev
        self.eletkor = random.randint(1, 15)  # Életkor 1 és 15 év között
        self.nem = random.choice(["Kan", "Szuka"])
    
    def __str__(self):
        return f"Név: {self.nev}, Életkor: {self.eletkor}, Nem: {self.nem}"

# Felhasználótól bekért kutyanevek listája
kutyak = []
while True:
    nev = input("Add meg a kutya nevét (vagy nyomj Entert a kilépéshez): ")
    if not nev:
        break
    kutyak.append(Kutya(nev))

# Kutyák adatainak kiírása
print("\nRögzített kutyák adatai:")
for kutya in kutyak:
    print(kutya)
