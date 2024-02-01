# Lösung der [Aufgaben](../Asymmetrisch_Aufgaben.pdf)
## 1.
Verschlüsselungsverfahren unterscheiden sich unteranderem in symmetrische und asymmetrische Verfahren. Der unterschied besteht darin, dass bei symmetrischen Verfahren ein einziger Schlüssel zum Ver- & Entschlüsseln verwendet wird. Dafür muss also der Schlüssel komplett übertragen werden. Bei asymmetrischen Verschlüsselungsverfahren ist das anders. Dort kann der Text mit einem Schlüssel ver-, und mit einem anderen entschlüsselt werden. Dabei gibt es in der Regel einen geheimen und einen öffentlichen Schlüssel.
## 2.
symmetrische Verfahren:
- Caesar/Vigenère
- DES
- AES

asymmetrische Verfahren:
- RSA
- Diffie-Hellman-Verfahren
- DSA
<!-- Quelle für DSA: "https://www.elektronik-kompendium.de/sites/net/1910111.htm" -->

## 3.
### a)
Whitfield Diffie\
Martin Hellman
### b)
Das Verfahren ist eine Lösung für das "Schlüsseltauschproblem". Man versucht, einen Schlüssel für ein symmetrisches Verschlüsselungsverfahren so zu übertragen, dass man diesen nicht einfach rekonstruieren/abhören/lesen kann.
### c)
Output bei ausführen von [3c.py](3c.py):
```
primitivwurzel**1  % primzahl = 6
primitivwurzel**2  % primzahl = 3
primitivwurzel**3  % primzahl = 7
primitivwurzel**4  % primzahl = 9
primitivwurzel**5  % primzahl = 10
primitivwurzel**6  % primzahl = 5
primitivwurzel**7  % primzahl = 8
primitivwurzel**8  % primzahl = 4
primitivwurzel**9  % primzahl = 2
primitivwurzel**10 % primzahl = 1
True
```
-> 6 ist Primitivwurzel von 11
### d)
```
p = 11
pw = 6
d = 7
t = 6

D = pw**d %p = 6**7 %11 = 8
T = pw**t %p = 6**6 %11 = 5

T**d %p = 5**7 %11 = 3
D**t %p = 8**6 %11 = 3
```
-> das Ergebnis ist `3`
## 4.
### a)
Ronald Linn Rivest\
Adi Shamir\
Leonard Adleman
### b)
Das RSA Verfahren kann verwendet werden, um unter Verwendung eines öffentlichen und eines Privaten Schlüssels (öffentlicher ist eigentlich ein Zahlenpaar, aber trotzdem wird dieser als *ein* Schlüssel bezeichnet) eine Zahl ver- & entschlüsselt werden kann. Dabei kann man den Text nicht entschlüsseln, wenn man nicht den jeweils anderen Schlüssel besitzt. Da man also einen "Text" nicht mit dem gleichen Schlüssel ver- & endschlüsseln kann, ist dieses Verfahren asymmetrisch.
### c)
p, q = 17, 233 (gelöst durch brute-force mittels <!-- PROGRAMM VON HANDY EINFÜGEN-->)\
*φ* (N) = 16*232 = 3712\
