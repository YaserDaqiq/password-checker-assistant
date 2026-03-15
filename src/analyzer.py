def analyze_password(password: str) -> dict:
    analysis = {
        "length": len(password),
        "has_lower": any(c.islower() for c in password),
        "has_upper": any(c.isupper() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(not c.isalnum() for c in password),
    }

    return analysis