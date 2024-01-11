import string

BASE62_CHARS = string.digits + string.ascii_letters


def base62_encode(num: int) -> str:
    if num == 0:
        return BASE62_CHARS[0]

    encoded = ""
    while num > 0:
        num, remainder = divmod(num, 62)
        encoded = BASE62_CHARS[remainder] + encoded

    return encoded
