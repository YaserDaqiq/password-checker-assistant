from scoring import score_password
from assistant import generate_suggestions


def main():
    password = input("Bitte gib ein Passwort ein: ")

    result = score_password(password)
    suggestions = generate_suggestions(result)

    print("\n--- Ergebnis ---")
    print(f"Passwortlänge: {result['password_length']}")
    print(f"Entropie: {result['entropy_bits']:.1f} bits")
    print(f"Score: {result['score']}/100")
    print(f"Kategorie: {result['category']}")

    print("\nBegründungen:")
    for reason in result["reasons"]:
        print(f"- {reason}")

    print("\nVerbesserungsvorschläge:")
    for suggestion in suggestions:
        print(f"- {suggestion}")


if __name__ == "__main__":
    main()