# 🔐 Password Checker & Assistant

Python CLI-Tool zur Bewertung von Passwortstärke mit konkreten Verbesserungsvorschlägen.
Projektarbeit HF – TEKO Luzern (LAP)

---

## Was macht das Programm?

- Bewertet Passwortstärke mit Score 0–100
- Kategorie: Schwach / Mittel / Stark
- Erkennt Schwächen: Wiederholungen, Sequenzen, häufige Wörter
- Berechnet Entropie (Unvorhersehbarkeit in Bits)
- Gibt konkrete Verbesserungsvorschläge aus

---

## Projektstruktur
```
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
```

---

## Voraussetzungen

- Python 3.x

---

## Installation
```bash
git clone https://github.com/YaserDaqiq/password-checker-assistant
cd password-checker-assistant
pip install -r requirements.txt
```

---

## Programm starten
```bash
python3 src/main.py
```

---

## Tests ausführen
```bash
python3 -m pytest -q
```

---

## Autor

Yaser Daqiq – TEKO Schweizerische Fachschule, Luzern
Klasse: TIP-25-Di-1
```

---