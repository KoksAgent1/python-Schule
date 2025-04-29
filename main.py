# Fingerübung 1: Der Listen-Detektiv (Ergibt Buchstaben 1)
wort_liste = ["Banane", "Apfel", "Pflaume", "Python-Skript", "Orange"]
buchstabe1 = None

# --- DEIN CODE HIER ---
for wort in wort_liste:
    if wort.startswith('P'):
        buchstabe1 = wort[0]
        break
# --- ENDE DEINES CODES ---

print(f"Ergebnis 1: {buchstabe1}")

# Fingerübung 2: Das Tupel-Summen-Rätsel (Ergibt Buchstaben 2)
zahlen_tupel = (8, 4, 10, 3)
code_map = {15: 'X', 25: 'Y', 30: 'A', 42: 'Z'}
buchstabe2 = None

# --- DEIN CODE HIER ---
summe = sum(zahlen_tupel)
buchstabe2 = code_map.get(summe)
# --- ENDE DEINES CODES ---

print(f"Ergebnis 2: {buchstabe2}")

# Fingerübung 3: Der Dictionary-Champion (Ergibt Buchstaben 3)
inventar = {"Stift": 15, "Block": 5, "Tasse": 18, "Maus": 2}
buchstabe3 = None

# --- DEIN CODE HIER ---
max_produkt = max(inventar, key=inventar.get)
buchstabe3 = max_produkt[0]
# --- ENDE DEINES CODES ---

print(f"Ergebnis 3: {buchstabe3}")

# Fingerübung 4: Der Tupel-Filter (Ergibt Buchstaben 4)
mixed_tupel = (10, "Hallo", 3.14, "Welt", True, "Hier", None, "Haus")
buchstabe4 = None

# --- DEIN CODE HIER ---
nur_strings = [x for x in mixed_tupel if isinstance(x, str)]
buchstabe4 = nur_strings[2][0]
# --- ENDE DEINES CODES ---

print(f"Ergebnis 4: {buchstabe4}")

# Fingerübung 5: Die Set-Schnittmenge (Ergibt Buchstaben 5)
set_a = {'Q', 'W', 'O', 'R', 'T', 'A'}
set_b = {'P', 'O', 'I', 'U', 'A', 'S'}
buchstabe5 = None

# --- DEIN CODE HIER ---
gemeinsam = sorted(set_a & set_b)
buchstabe5 = gemeinsam[-1]
# --- ENDE DEINES CODES ---

print(f"Ergebnis 5: {buchstabe5}")

# Fingerübung 6: Der Listen-Modulo-Trick (Ergibt Buchstaben 6)
zahlen_reihe = [2, 9, 5, 12, 8, 6]
quell_string = "ZYXWVNEUT"
buchstabe6 = None

# --- DEIN CODE HIER ---
summe_durch_3 = sum(x for x in zahlen_reihe if x % 3 == 0)
index = summe_durch_3 % len(zahlen_reihe)
buchstabe6 = quell_string[index]
# --- ENDE DEINES CODES ---

print(f"Ergebnis 6: {buchstabe6}")
