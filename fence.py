def fence(p, k):
    fence = [[None] * len(p) for n in range(k)]
    rails = range(k - 1) + range(k - 1, 0, -1)
    for n, x in enumerate(p):
        fence[rails[n % len(rails)]][n] = x
    return [c for rail in fence for c in rail if c is not None]

def encrypt(p, k):
    return ''.join(fence(p, k))

def decrypt(c, k):
    rng = range(len(c))
    pos = fence(rng, k)
    return ''.join(c[pos.index(k)]for k in rng)

print encrypt("Aidan Devlin", 4)

print decrypt("ADi endnvial", 4)
