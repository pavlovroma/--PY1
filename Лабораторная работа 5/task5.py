import random
import  string
chis = string.ascii_letters and string.hexdigits
def get_random_password(chis, k = 8):
    return "" .join(random.sample(chis, k))

print(get_random_password(chis))

