# Aufgaben zu [symmetrischen Verschlüsselungsverfahren](../Symmetrisch_Aufgaben.pdf)
## 1.
### a)

`Klartext`= "VORABITUR"
`Schlüssel` = "G"
`Umschreibtabelle`:
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
GHIJKLMNOPQRSTUVWXYZABCDEF
```
(Hier wird `A -> G; B -> H; ...`)\
`Geheimtext` = "BUXGHOZAX"

### b)
[symm1.cwm - Datei](symm1.cwm)
```
häufigster Buchstabe Geheimtext:            Y
häufigster Buchstabe der deutschen Sprache: E

E -> Y:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
UVWXYZABCDEFGHIJKLMNOPQRST
Also: A -> U
```
Der verwendete Schlüssel ist "U"

## 2.
### a)
Verschiebungstabelle:
```
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
T:  TUVWXYZABCDEFGHIJKLMNOPQRS
O:  OPQRSTUVWXYZABCDEFGHIJKLMN
L:  LMNOPQRSTUVWXYZABCDEFGHIJK
L:  LMNOPQRSTUVWXYZABCDEFGHIJK
```
Verschlüsselung von "WINTERFERIEN" = "PWYEXFQPKWPY"
### b)
Koinzidenzindex ist der Durchschnitt aller Wahrscheinlichkeiten aller Buchstaben.\
In dem Beispiel haben alle Buchstaben die gleiche Wahrscheinlichket `P = 1/42`, also ist `P = "Koinzidenzindex"`, also ca. `0,0238`.
### c)
Berechnung des Koinzidenzindex mit den Werten von [v293_buchstabenhaeufigkeit-station.pdf](../v293_buchstabenhaeufigkeit-station.pdf):
<!-- pythonlist:
[0.0651, 0.0189, 0.0306, 0.0508, 0.174, 0.0166, 0.0301, 0.0476, 0.0755, 0.0027, 0.0121, 0.0344, 0.0253, 0.0978, 0.0251, 0.0079, 0.0002, 0.07, 0.0727, 0.0615, 0.0435, 0.0067, 0.0189, 0.0003, 0.0004, 0.0113]
-->
|Buchstabe|Wahrscheinlichkeit|
|-|-|
|A|0.0651|
|B|0.0189|
|C|0.0306|
|D|0.0508|
|E|0.174|
|F|0.0166|
|G|0.0301|
|H|0.0476|
|I|0.0755|
|J|0.0027|
|K|0.0121|
|L|0.0344|
|M|0.0253|
|N|0.0978|
|O|0.0251|
|P|0.0079|
|Q|0.0002|
|R|0.07|
|S|0.0727|
|T|0.0615|
|U|0.0435|
|V|0.0067|
|W|0.0189|
|X|0.0003|
|Y|0.0004|
|Z|0.0113|

Die quadratische Summe aller Wahrscheinlichkeiten ist `0.07616008` ([berechnet mit python](koinzidenzindex.py)) oder rund **`0.0762`**, daher ist die Annahme aus [v02_doku.pdf](../v02_doku.pdf) annäherungsweise richtig.
### 3.
Caesar und Abwandlungen wie Vigenère sind für heutige Standarts sehr simple und unsichere Verschlüsselungsverfahren, da über z.B. entweder durch Berechnung mittels Buchstabenwahrscheinlichkeit oder durch Brute-Force der Geheimtext auch ohne Schlüssel schnell lösbar ist. So kann man Caesar of sogar von Hand lösen. Auch Vigenère ist mittels moderner Computer oft in wenigen Sekunden geknackt. Da Sicherheit eigentlich langwierig garantiert sein sol (nicht nur für 10 Sekunden) sind die hier bearbeiteten Verschlüsselungsalgorithmen nicht mehr sicher.
### 4.
Lösung der Aufgabe in [bmw.py](bmw.py)\
Schwierigkeitsgrad: mutig <!-- TODO: auf "waghalsig" verbessern -->\
Art der Anwendung von Vigenère: Wiederholung des Schlüssels über den ganzen Text, nicht nur über verschlüsselbare Zeichen.\
Die `vig()` Funktion ist die im Programm verwendete, allerdings ist an das wohl des Lehrers gedacht und somit eine aufgedröselte (in dem `'''...'''` Kommentar unter `vig()`), sowie eine umgeschriebene Version (`vigB()`) vorhanden.
