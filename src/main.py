from scoring import score_password


def main():
    # 1) Benutzer gibt ein Passwort ein
    password = input("Bitte gib ein Passwort ein: ")

    # 2) Algorithmus aus scoring.py aufrufen
    result = score_password(password)

    # 3) Resultat ausgeben
    print("\n--- Ergebnis ---")
    print(f"Passwortlänge: {result['password_length']}")
    print(f"Entropie: {result['entropy_bits']:.1f} bits")
    print(f"Score: {result['score']}/100")
    print(f"Kategorie: {result['category']}")

    print("\nBegründungen:")
    for reason in result["reasons"]:
        print(f"- {reason}")


if __name__ == "__main__":
    main()