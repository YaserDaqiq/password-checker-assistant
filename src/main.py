# main.py
# Einstiegspunkt des Programms.
# Diese Datei liest ein Passwort ein, ruft die Bewertung auf
# und zeigt das Ergebnis sowie Verbesserungsvorschläge an.

from scoring import score_password
from assistant import generate_suggestions


def main():
    # Fragt den Benutzer nach einem Passwort.
    password = input("Bitte gib ein Passwort ein: ")

    # Bewertet das eingegebene Passwort.
    result = score_password(password)

    # Erzeugt passende Verbesserungsvorschläge
    # basierend auf dem Bewertungsergebnis.
    suggestions = generate_suggestions(result)

    # Gibt die wichtigsten Resultate übersichtlich im Terminal aus.
    print("\n--- Ergebnis ---")
    print(f"Passwortlänge: {result['password_length']}")
    print(f"Entropie: {result['entropy_bits']:.1f} bits")
    print(f"Score: {result['score']}/100")
    print(f"Kategorie: {result['category']}")

    # Gibt die Gründe aus, warum das Passwort so bewertet wurde.
    print("\nBegründungen:")
    for reason in result["reasons"]:
        print(f"- {reason}")

    # Gibt konkrete Tipps zur Verbesserung des Passworts aus.
    print("\nVerbesserungsvorschläge:")
    for suggestion in suggestions:
        print(f"- {suggestion}")


# Startet das Programm nur dann,
# wenn diese Datei direkt ausgeführt wird.
if __name__ == "__main__":
    main()