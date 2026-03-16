from logic_utils import check_guess


# ── Basic outcome tests ──────────────────────────────────────────────

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# ── Hint-direction bug (messages were swapped) ───────────────────────

def test_too_high_hint_says_lower():
    """Bug fix: a too-high guess must tell the player to go LOWER."""
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint, got: {message}"


def test_too_low_hint_says_higher():
    """Bug fix: a too-low guess must tell the player to go HIGHER."""
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint, got: {message}"


# ── Type-coercion bug (secret sometimes passed as str) ───────────────

def test_check_guess_with_string_secret():
    """Bug fix: app.py passes secret as str on even attempts."""
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"


def test_check_guess_with_string_guess():
    """Ensure string guess is also handled gracefully."""
    outcome, _ = check_guess("50", 50)
    assert outcome == "Win"


def test_too_high_with_string_secret():
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"


def test_too_low_with_string_secret():
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"
