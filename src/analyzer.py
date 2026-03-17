# analyzer.py
# Führt eine Grundanalyse des Passworts durch.
# Die Funktion prüft Länge sowie verschiedene Zeichentypen
# und gibt die Ergebnisse als Dictionary zurück.

def analyze_password(password: str) -> dict:
    # Erstellt ein Dictionary mit den wichtigsten Merkmalen des Passworts.
    analysis = {
        "length": len(password),  # Anzahl Zeichen im Passwort
        "has_lower": any(c.islower() for c in password),  # mind. ein Kleinbuchstabe
        "has_upper": any(c.isupper() for c in password),  # mind. ein Grossbuchstabe
        "has_digit": any(c.isdigit() for c in password),  # mind. eine Zahl
        "has_special": any(not c.isalnum() for c in password),  # mind. ein Sonderzeichen
    }

    # Gibt die gesammelten Analyseergebnisse zurück.
    return analysis