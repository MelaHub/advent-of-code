def is_valid(passphrase):
  cache = set()
  for word in passphrase.split(' '):
    if word in cache:
      return False
    cache.add(word)
  return True

def count_valid_passphrases(passphrases):
  return sum([1 if is_valid(phrase) else 0 for phrase in passphrases])

def count_valid_from_default_file():
  passphrases = []
  with open('passphrases') as f:
    passphrases += [row.strip() for row in f.readlines()]
  return count_valid_passphrases(passphrases)
