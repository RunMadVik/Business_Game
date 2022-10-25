import secrets
import string


def generate_random_string(length: str = 10):
    res = "".join(
        secrets.choice(string.ascii_uppercase + string.digits) for i in range(length)
    )
    return str(res)
