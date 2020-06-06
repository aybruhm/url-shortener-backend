from string import ascii_letters, digits
from random import choices

class Shortener:

    def __init__(self, k=None):
        self.k = k if k is not None else 5

    def shorten(self):
        return ''.join(choices(ascii_letters+digits*2, k=5))

# shortener = Shortener()
# print(shortener.shorten())