identity = lambda x: x
sort_word = lambda x: ''.join(sorted(x))

def _is_valid(passphrase, word_fn):
  cache = set()
  for word in passphrase.split(' '):
    new_word = word_fn(word)
    if new_word in cache:
      return False
    cache.add(new_word)
  return True

def is_valid_identity(passphrase):
  return _is_valid(passphrase, identity)

def is_valid_anagram(passphrase):
  return _is_valid(passphrase, sort_word)

def count_valid_passphrases(passphrases, is_valid_fn):
  return sum([1 if is_valid_fn(phrase) else 0 for phrase in passphrases])

def count_valid_from_default_file(is_valid_fn):
  passphrases = []
  with open('passphrases') as f:
    passphrases += [row.strip() for row in f.readlines()]
  return count_valid_passphrases(passphrases, is_valid_fn)
