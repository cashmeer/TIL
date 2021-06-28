import string
import random

def gen_rand_text(num):
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(num))

def get_mid(s):
    return "change of problem with answer needed"

print(get_mid(gen_rand_text(10)))
print(get_mid(gen_rand_text(9)))
print(get_mid(gen_rand_text(8)))
print(get_mid(gen_rand_text(7)))
print(get_mid(gen_rand_text(100)))



