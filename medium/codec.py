def encode(longUrl: str) -> str:
    """Encodes a URL to a shortened URL.
    """
    url_list = list(longUrl)
    for i in range(len(url_list)):
        url_list[i] = chr(ord(url_list[i]) + 5)
    return ''.join(url_list)


def decode(shortUrl: str) -> str:
    """Decodes a shortened URL to its original URL.
    """
    url_list = list(shortUrl)
    for i in range(len(url_list)):
        url_list[i] = chr(ord(url_list[i]) - 5)
    return ''.join(url_list)
