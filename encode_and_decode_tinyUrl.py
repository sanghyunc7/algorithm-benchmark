import random
import string


class Codec:
    chars = string.digits + string.ascii_letters
    codes = {}  # tinyurl -> longurl
    urls = {}  # longurl -> tinyurl
    tinyurl = "http://tinyurl.com/"

    def create_code(self):
        code = ""

        for c in range(6):
            code += random.choice(self.chars)

        return code

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.urls:
            return self.urls[longUrl]

        code = self.create_code()
        # to avoid hash collision
        while self.tinyurl + code in self.codes:
            code = self.create_code()

        self.codes[self.tinyurl + code] = longUrl
        self.urls[longUrl] = self.tinyurl + code
        return self.urls[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.codes[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
