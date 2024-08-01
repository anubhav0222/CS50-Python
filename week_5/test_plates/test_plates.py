from plates import is_valid

# “No periods, spaces, or punctuation marks are allowed.”
def test_spe_char():
    assert is_valid("CS50!") == False


# “All vanity plates must start with at least two letters.”
def test_start_two_letters():
    assert is_valid("AN") == True
    assert is_valid("20") == False
    assert is_valid("T5") == False
    assert is_valid("0") == False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_length():
    assert is_valid("CHECK1") == True
    assert is_valid("AB") == True
    assert is_valid("ANUBHAV") == False


# “Numbers cannot be used in the middle of a plate; they must come at the end.
#  For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False
