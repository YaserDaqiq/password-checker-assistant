def generate_suggestions(result: dict) -> list:
    suggestions = []

    reasons = result["reasons"]

    for reason in reasons:
        if "Zu kurz" in reason:
            suggestions.append("Verlängere das Passwort auf mindestens 12 Zeichen.")

        if "Keine Kleinbuchstaben" in reason:
            suggestions.append("Füge mindestens einen Kleinbuchstaben hinzu.")

        if "Keine Grossbuchstaben" in reason:
            suggestions.append("Füge mindestens einen Grossbuchstaben hinzu.")

        if "Keine Zahlen" in reason:
            suggestions.append("Füge mindestens eine Zahl hinzu.")

        if "Keine Sonderzeichen" in reason:
            suggestions.append("Verwende mindestens ein Sonderzeichen, z. B. ! oder @.")

        if "Wiederholungsmuster" in reason:
            suggestions.append("Vermeide Wiederholungen wie aaa oder 111.")

        if "Einfache Sequenzen" in reason:
            suggestions.append("Vermeide einfache Sequenzen wie abc oder 123.")

        if "Häufiges Muster/Wort" in reason:
            suggestions.append("Verwende keine häufigen Wörter wie password oder admin.")

        if "Niedrige Entropie" in reason:
            suggestions.append("Verwende mehr unterschiedliche Zeichen, damit das Passwort schwerer zu erraten ist.")

    if not suggestions:
        suggestions.append("Das Passwort ist bereits gut aufgebaut. Behalte trotzdem eine ausreichende Länge bei.")

    return suggestions