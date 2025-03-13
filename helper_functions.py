import secrets
import string

# Generate random strings
def string_gen(x=15):
    key = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for i in range(x))
    return key
