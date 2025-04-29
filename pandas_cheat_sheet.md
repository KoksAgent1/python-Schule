
# 🐼 Pandas Cheat Sheet - Schnellübersicht

---

## Grundlagen

```python
import pandas as pd
```

## Haupt-Datenstrukturen

- **Series**: 1D-Array mit Labels (Index)
- **DataFrame**: 2D-Tabelle (Zeilen und Spalten)

```python
# Series
s = pd.Series([1, 2, 3])

# DataFrame
data = {'Name': ['Anna', 'Ben'], 'Alter': [23, 25]}
df = pd.DataFrame(data)
```

## CSV-Dateien

```python
# Lesen
pd.read_csv('datei.csv')

# Schreiben
df.to_csv('datei.csv', index=False)
```

## Erste Schritte

```python
df.head()       # Erste 5 Zeilen
df.tail()       # Letzte 5 Zeilen
df.info()       # Infos zu Datentypen und Null-Werten
df.describe()   # Statistiken
```

## Auswahl von Daten

```python
# Einzelne Spalte
df['Alter']

# Mehrere Spalten
df[['Name', 'Alter']]

# Zeilen über Index
df.iloc[0]     

# Zeilen über Bedingung
df[df['Alter'] >= 25]

# Zeile + Spalte
df.at[0, 'Name']
```

## Bearbeiten von Daten

```python
# Neue Spalte
df['Jahrgang'] = 2025 - df['Alter']

# Spalte überschreiben
df['Alter'] = df['Alter'] + 1

# Drop (Löschen)
df.drop(columns=['Jahrgang'], inplace=True)
```

## Sortieren und Filtern

```python
# Nach Alter sortieren
df.sort_values('Alter')

# Nach mehreren Spalten
df.sort_values(['Stadt', 'Alter'])

# Bestimmte Einträge
df[df['Stadt'] == 'Berlin']
```

## Fehlende Daten

```python
# Finden
df.isnull()

# Entfernen
df.dropna()

# Auffüllen
df.fillna('Unbekannt')
```

## Gruppieren und Aggregieren

```python
# Gruppieren
df.groupby('Stadt')

# Aggregieren
df.groupby('Stadt')['Alter'].mean()
df.groupby('Stadt').size()
```

## Zusammenführen (Merge/Join)

```python
# Zwei DataFrames verbinden
pd.merge(df1, df2, on='gemeinsame_spalte')

# Alternativ (concat)
pd.concat([df1, df2])
```

## Exportieren von Daten

```python
# Excel
df.to_excel('datei.xlsx', index=False)

# JSON
df.to_json('datei.json')
```

## Tipps

- **copy()** verwenden, um Originaldaten zu schützen.
- **inplace=True** spart Zuweisungen.
- **axis=0** = Zeilenweise, **axis=1** = Spaltenweise.
