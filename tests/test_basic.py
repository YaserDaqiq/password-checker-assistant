from src.scoring import score_password


def test_very_weak_password():
    r = score_password("12345")
    assert r["category"] == "Schwach"


def test_common_word_is_weak():
    r = score_password("password")
    assert r["category"] == "Schwach"


def test_medium_password():
    r = score_password("Passwort123")
    assert r["category"] in ["Schwach", "Mittel"]


def test_strong_password():
    r = score_password("A7!kQ2@zP9xL")
    assert r["category"] == "Stark"


def test_repetition_is_weak():
    r = score_password("aaaaaaaaaaaa")
    assert r["category"] == "Schwach"


def test_admin_pattern():
    r = score_password("Admin123")
    assert r["category"] in ["Schwach", "Mittel"]


def test_hallo123_is_medium():
    r = score_password("Hallo123!")
    assert r["category"] == "Mittel"


def test_long_complex_password_is_strong():
    r = score_password("T3ko!Projekt2026#")
    assert r["category"] == "Stark"