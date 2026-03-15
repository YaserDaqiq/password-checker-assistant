# 🔐 Password Checker & Assistant

Python CLI-Tool zur Bewertung von Passwortstärke 
mit konkreten Verbesserungsvorschlägen.
Projektarbeit HF – TEKO Luzern (LAP)

---

## Was macht das Programm?

- Bewertet Passwortstärke mit Score 0–100
- Kategorie: Schwach / Mittel / Stark
- Erkennt Schwächen: Wiederholungen, Sequenzen, häufige Wörter
- Berechnet Entropie (Unvorhersehbarkeit in Bits)
- Gibt konkrete Verbesserungsvorschläge aus
- Prüft ob Passwort in Datenlecks vorkam (HaveIBeenPwned API)

---

## Projektstruktur

password-checker-assistant/
├── src/
│   ├── main.py        → Einstiegspunkt (CLI)
│   ├── scoring.py     → Bewertungslogik (Score 0–100)
│   ├── assistant.py   → Verbesserungsvorschläge
│   └── analyzer.py    → Passwort-Analyse
├── tests/
│   └── test_basic.py  → Automatisierte Tests (pytest)
├── requirements.txt
└── README.md

---

## Voraussetzungen

- Python 3.x
- pip

---

## Installation

# Repository klonen
git clone https://github.com/YaserDaqiq/password-checker-assistant

# In den Ordner wechseln
cd password-checker-assistant

# Abhängigkeiten installieren
pip install -r requirements.txt

---

## Programm starten

python3 src/main.py

---

## Tests ausführen

python3 -m pytest -q

---

## Beispiel-Ausgabe

Bitte gib ein Passwort ein: Hallo123!

--- Ergebnis ---
Passwortlänge: 9
Entropie: 59.0 bits
Score: 40/100
Kategorie: Mittel

Begründungen:
- Länge okay (8–11 Zeichen)
- Einfache Sequenzen erkannt

Verbesserungsvorschläge:
- Vermeide Sequenzen wie abc oder 123
- Verwende mindestens 12 Zeichen

---

## Autor

Yaser Daqiq – TEKO Schweizerische Fachschule, Luzern
Klasse: TIP-25-Di-1