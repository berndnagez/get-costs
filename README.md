# Nutzung
## Voraussetzung
1) die Lohnjournal-xlsx-Datei von S&P für den auszuwertenden Monat muss vorhanden sein
2) die Datei muss am Anfang ihres Dateinamens das entsprechende Jahr und den Monat haben (bspw. 24_01 ...)
3) sie muss in "1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal/2024/- 01 Lohnjournale" liegen (Jahreszahl kann varrieren)
4) Die Rohdaten in "- 01 Rohdaten Zur Auswertung" müssen aktuell sein, d. h. für den zu verarbeitenden Monat muss ein jeweils ein Tabellenblatt mit dem Namen des Monats (bspw. 24_01 ...) geben

## Drei Nutzungsoptionen
### Auswertung eines einzelnen Journals
<code>main.py -i "24_03_21 Lohnjournal März 2024.xlsx"</code>

### Auswertung eines Projekts
<code>main.py -p 0026</code>

### Auswerung eines Journals für ein Projekt
<code>main.py -i "24_03_21 Lohnjournal März 2024.xlsx" -p 0026</code>

## Ausführung - VERALTET
sind die Voraussetzung (s.o.) erfüllt, müssen folgende Schritte gemacht werden:
1) im Ordner "2000 Finanzverwaltung/- 97 Automatische Lohn- und Nebenkosten Auswertung (Finanztabelle)" rechtsklick auf eine freie Stelle und "Im Terminal öffnen" auswählen
2) im Terminal eingeben: ./get_projects_costs.py (nach get einfach die Tab-Taste drücken) und dann mit -i das gewünschte Lohnjournal spezifizieren

Bsp.: ./get_projects_costs.py -i "24_01_24 Lohnjournal Januar 2024.xlsx"

Dann wird die Befehlszeile mit "Enter" gestätigt.

Es kann sein, dass Infos, Warnungen oder Fehlermeldungen im Terminal ausgegeben werden.

Das Ergebnis landet dann im Ordner "- 02 Ergebnisse der Auswertung (Monatsweise)"

## Bekannte Problem
Wenn die "-p"-Option genutzt wird und die Tabellenblätter für Buchhaltung und für Reinigung keine Daten enthalten, liegt es daran, dass Birthe und Paul laut employee_data keine Stunden in dem Projekt haben. Ein Workaround ist, die lokale employee_data-Datei (nicht die auf Seafile) so zu modifizieren, dass Birthe und Paul in dem Projekt haben.

# Formeln neu berechnen
wenn auf anderen Rechnern überall 0,00 Euro sind:

Extras -> Optionen -> LibreOffice Calc -> Formeln -> Neuberechnung beim Laden der Datei: "Immer neu berechnen"

# dependencies
```
sudo apt install python3-pip
pip install xlsxwriter
pip install pandas
pip install openpyxl
```