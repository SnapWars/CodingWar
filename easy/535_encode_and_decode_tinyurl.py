class Codec:
    _map = {}
    _counter = 0
    def encode(self, longUrl):
        self._map[self._counter] = longUrl
        counter = self._counter
        self._counter += 1
        return counter


    def decode(self, shortUrl):
        return self._map[shortUrl]
