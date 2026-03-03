import re
import math

# kleine Liste typischer Muster/Wörter (für Mustererkennung)
COMMON_PATTERNS = ["1234", "abcd", "qwert", "password", "admin", "welcome", "passwort"]


def has_upper(s: str) -> bool:
    return any(c.isupper() for c in s)


def has_lower(s: str) -> bool:
    return any(c.islower() for c in s)


def has_digit(s: str) -> bool:
    return any(c.isdigit() for c in s)


def has_special(s: str) -> bool:
    return any(not c.isalnum() for c in s)


def has_repetition(s: str) -> bool:
    # erkennt 3 gleiche Zeichen hintereinander, z.B. "aaa", "111"
    return bool(re.search(r"(.)\1\1", s))


def has_sequence(s: str) -> bool:
    # erkennt einfache Sequenzen wie abc oder 123 (3 Zeichen in Folge)
    s_lower = s.lower()
    for i in range(len(s_lower) - 2):
        a, b, c = s_lower[i], s_lower[i + 1], s_lower[i + 2]
        if a.isalnum() and b.isalnum() and c.isalnum():
            if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
                return True
    return False


def contains_common_pattern(s: str) -> bool:
    s_lower = s.lower()
    return any(p in s_lower for p in COMMON_PATTERNS)


def estimate_entropy_bits(s: str) -> float:
    # vereinfachtes Modell:
    # entropy ≈ length * log2(charset_size)
    charset = 0
    if has_lower(s):
        charset += 26
    if has_upper(s):
        charset += 26
    if has_digit(s):
        charset += 10
    if has_special(s):
        charset += 32  # grobe Annahme

    if charset == 0:
        return 0.0

    return len(s) * math.log2(charset)


def score_password(pw: str) -> dict:
    """
    Bewertet ein Passwort und gibt ein Resultat-Dictionary zurück:
    - score (0..100)
    - category: Schwach/Mittel/Stark
    - entropy_bits
    - reasons (Liste von Begründungen)
    """
    reasons = []
    score = 0

    # 1) Länge
    length = len(pw)
    if length < 8:
        score -= 20
        reasons.append("Zu kurz (< 8 Zeichen).")
    elif length < 12:
        score += 10
        reasons.append("Länge okay (8–11 Zeichen).")
    else:
        score += 20
        reasons.append("Gute Länge (≥ 12 Zeichen).")

    # 2) Zeichentypen
    if has_lower(pw):
        score += 10
    else:
        reasons.append("Keine Kleinbuchstaben.")

    if has_upper(pw):
        score += 10
    else:
        reasons.append("Keine Grossbuchstaben.")

    if has_digit(pw):
        score += 10
    else:
        reasons.append("Keine Zahlen.")

    if has_special(pw):
        score += 10
    else:
        reasons.append("Keine Sonderzeichen.")

    # 3) Schwächen / Muster
    if has_repetition(pw):
        score -= 15
        reasons.append("Wiederholungsmuster erkannt (z.B. 'aaa' oder '111').")

    if has_sequence(pw):
        score -= 15
        reasons.append("Einfache Sequenzen erkannt (z.B. 'abc' oder '123').")

    if contains_common_pattern(pw):
        score -= 20
        reasons.append("Häufiges Muster/Wort erkannt (z.B. 'password', 'admin').")

    # 4) Entropie
    entropy = estimate_entropy_bits(pw)
    if entropy < 35:
        score -= 10
        reasons.append(f"Niedrige Entropie (~{entropy:.1f} bits).")
    elif entropy < 60:
        score += 5
        reasons.append(f"Mittlere Entropie (~{entropy:.1f} bits).")
    else:
        score += 10
        reasons.append(f"Hohe Entropie (~{entropy:.1f} bits).")

    # Score normalisieren
    if score < 0:
        score = 0
    if score > 100:
        score = 100

    # Kategorie
    if score < 40:
        category = "Schwach"
    elif score < 70:
        category = "Mittel"
    else:
        category = "Stark"

    return {
        "password_length": length,
        "entropy_bits": entropy,
        "score": score,
        "category": category,
        "reasons": reasons,
    }