from math import floor 

def base62_encoder(id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        r = id % base
        res = characters[r]
        q = floor(id / base)
        while q:
            r = q % base
            q = floor(q / base)
            res = characters[int(r)] + res
        return res
        # hash_str = ''
        # while id > 0:
        #     hash_str = characters[id % base] + hash_str
        #     id //= base
        # return hash_str

def base62_decoder(id):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    limit = len(id)
    res = 0
    for i in range(limit):
        res = base * res + characters.find(id[i])
    return res