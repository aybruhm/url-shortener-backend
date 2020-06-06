import string
import random


class Shortener:
    k = 5

    def __init__(self, k=None):
        self.k = k if k is not None else 5

    def shorten(self):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choices(letters) for i in range(self.k))

