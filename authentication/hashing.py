import hashlib

# We need to encode the unicode so that we can pass them in to the
# hashlib hashing functions we can do this by putting a b in front
# of them it doesn't matter what you do as long as you always do the
# same thing

my_password = b"password123"
salt = b"STEMCentre"

print("Built in hash", hash(my_password))
print("Built in hash and salt", hash(salt + my_password))

print("Using SHA512", hashlib.sha512(my_password).hexdigest())
print("Using SHA512 and salt", hashlib.sha512(my_password + salt).hexdigest())

