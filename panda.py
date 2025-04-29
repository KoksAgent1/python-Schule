import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv('C:\\Users\\flori\\Desktop\\personen.csv')

# Inhalt anzeigen
print(df)

# Durchschnittsalter berechnen
durchschnitt = df['Alter'].mean()
print(f"Durchschnittsalter: {durchschnitt:.2f} Jahre")

# Alle Personen, die älter als 24 sind
aelter_als_24 = df[df['Alter'] > 24]
print("Personen älter als 24:")
print(aelter_als_24)

# Personen nach Alter sortieren
sortiert = df.sort_values('Alter')
print("Nach Alter sortiert:")
print(sortiert)
