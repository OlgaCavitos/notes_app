import string
def is_valid_email(email):
    parts=email.split('@')
    if len(parts) != 2:
        return False
    allowed=set(string.ascii_letters +string.digits + ' .-_')
    # print('allowed:', allowed)
    # print(parts)
    for part in parts:
            if not set(part) <= allowed:
                return False
    return True


def test_is_valid_email():

    assert is_valid_email('test@example.org')  # True
    assert is_valid_email('user123@subdomain.example.org')  # True
    assert is_valid_email('john.doe@email.example.org')  # True
    assert not is_valid_email('not valid@example.org')  # False
    assert not is_valid_email('john.doe')  # False
    assert not is_valid_email('john,doe@example.org')  # False

