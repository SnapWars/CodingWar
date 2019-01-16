def anagram_count(l):
    d = {}
    result = 0
    for w in l:
        f = freq(w)
        fs = frozenset(f.items())
        d[fs] = 1 if fs not in d else d[fs] + 1

    for w in l:
        f = freq(w)
        fs = frozenset(f.items())
        if fs in d and d[fs] > 1:
            result += 1
    return result

def anagram_words(l):
    d = {}
    result = []
    for w in l:
        f = freq(w)
        fs = frozenset(f.items())
        d[fs] = 1 if fs not in d else d[fs] + 1

    for w in l:
        f = freq(w)
        fs = frozenset(f.items())
        if fs in d and d[fs] > 1:
            result.append(w)
    return result

def freq(s):
    d = {}
    for c in s:
        d[c] = 1 if c not in d else d[c] + 1
    return d

def main():
    print anagram_words(
        ['star', 'rats', 'pasta', 'astap']
    )

if __name__ == '__main__':
    main()
