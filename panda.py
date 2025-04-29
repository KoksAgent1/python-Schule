import pandas as pd  # Importiere die pandas-Bibliothek für Datenanalyse
import os            # Importiere os für Dateisystem-Funktionen

# Definiere den Pfad zur CSV-Datei. Das r vor dem String macht ihn zu einem "Raw String",
# damit Backslashes (\) nicht als Steuerzeichen interpretiert werden (z. B. \n, \t etc.)
csv_path = r'personen.csv'

# Überprüfe, ob die Datei existiert
if not os.path.exists(csv_path):
    # Wenn die Datei nicht gefunden wird, gib eine Fehlermeldung aus
    print(f"❌ Fehler: Die Datei wurde nicht gefunden unter: {csv_path}")
else:
    try:
        # Versuche, die CSV-Datei einzulesen und in einen DataFrame zu laden
        df = pd.read_csv(csv_path)

        # Zeige die eingelesenen Daten an
        print("📄 Eingelesene Daten:")
        print(df)

        # Überprüfe, ob die Spalte 'Alter' in den Daten vorhanden ist
        if 'Alter' not in df.columns:
            print("❌ Fehler: Die Spalte 'Alter' ist nicht in der Datei enthalten.")
        else:
            # Berechne den Durchschnitt aller Werte in der Spalte 'Alter'
            durchschnitt = df['Alter'].mean()

            # Gib das Ergebnis mit zwei Nachkommastellen aus
            print(f"\n📊 Durchschnittsalter: {durchschnitt:.2f} Jahre")

            # Filtere alle Personen, deren Alter größer als 24 ist
            aelter_als_24 = df[df['Alter'] > 24]

            # Zeige diese gefilterten Personen an
            print("\n👥 Personen älter als 24:")
            print(aelter_als_24)

            # Sortiere die Daten nach der Spalte 'Alter' in aufsteigender Reihenfolge
            sortiert = df.sort_values('Alter')

            # Gib den sortierten DataFrame aus
            print("\n🔢 Nach Alter sortiert:")
            print(sortiert)

    # Behandle spezifische Fehler beim Einlesen der Datei

    except pd.errors.EmptyDataError:
        # Fehler, wenn die Datei leer ist
        print("❌ Fehler: Die Datei ist leer.")

    except pd.errors.ParserError:
        # Fehler, wenn die Datei nicht korrekt formatiert ist (z. B. kaputte CSV-Struktur)
        print("❌ Fehler: Die Datei konnte nicht korrekt gelesen werden (möglicherweise fehlerhaftes CSV-Format).")

    except Exception as e:
        # Allgemeiner Fehler (z. B. Leserechte, unerwartete Fehler)
        print(f"❌ Ein unerwarteter Fehler ist aufgetreten: {e}")
