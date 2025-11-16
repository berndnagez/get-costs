# Nutzung
## Voraussetzung
1) die Lohnjournal-xlsx-Datei von S&P für den auszuwertenden Monat muss vorhanden sein
2) die Datei muss am Anfang ihres Dateinamens das entsprechende Jahr und den Monat haben (bspw. 24_01 ...)
3) sie muss in "1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal/2025/- 01 Lohnjournale" liegen (Jahreszahl kann variieren)
4) Die Rohdaten in "- 01 Rohdaten Zur Auswertung" müssen aktuell sein, d. h. für den zu verarbeitenden Monat muss ein jeweils ein Tabellenblatt mit dem Namen des Monats (bspw. 24_01 ...) geben

## Ausführung
sind die Voraussetzung (s.o.) erfüllt, müssen folgende Schritte gemacht werden:
1) im Ordner "2000 Finanzverwaltung/- 97 Automatische Lohn- und Nebenkosten Auswertung (Finanztabelle)" rechtsklick auf eine freie Stelle und "Im Terminal öffnen" auswählen
2) im Terminal eingeben: get-costs (nach "get-c" einfach die Tab-Taste drücken) und dann mit -i das gewünschte Lohnjournal spezifizieren

Bsp.: get-costs -i "25_10_23 Lohnjournal Oktober 2025.xlsx"

Dann wird die Befehlszeile mit "Enter" gestätigt.

Es kann sein, dass Infos, Warnungen oder Fehlermeldungen im Terminal ausgegeben werden.

Das Ergebnis landet dann im Ordner "- 02 Ergebnisse der Auswertung (Monatsweise)"

# Formeln neu berechnen
wenn auf anderen Rechnern überall 0,00 Euro sind:

Extras -> Optionen -> LibreOffice Calc -> Formeln -> Neuberechnung beim Laden der Datei: "Immer neu berechnen"

# dependencies
```
sudo apt install python3-pip
sudo apt install python3-xlsxwriter
sudo apt install python3-pandas
sudo apt install python3-openpyxl
```
