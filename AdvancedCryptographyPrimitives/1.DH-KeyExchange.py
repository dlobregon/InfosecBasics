# Instrucctions
# implement a Toy Diffie-Hellman system by completing The diffie-hellman key exchange protocol:
# supply the "publish" and  "compute_secret" methods for both Alice and Bob


# Alice's "publish()" should return the message to be sent to Bob.
# Bob's "publish()" sould return the message to be sent to Alice. 
# Both their "compute_secret()" should, given the message from the other party, return the agreed-upon secret. 
import random

# here we define the prime number and the base that are public
p = 283
g = 47


class Alice:

    def __init__(self):
        self.a = random.randint(1, p)

    def publish(self):
        value= (g ** self.a) % p
        return value

    def compute_secret(self, gb):
        agreetment= (gb**self.a) % p
        return agreetment


class Bob:

    def __init__(self):
        self.b = random.randint(1, p)

    def publish(self):
        value = (g**self.b) % p
        return value

    def compute_secret(self, ga):
        agreetment= (ga ** self.b) % p
        return agreetment


alice = Alice()
bob = Bob()
print('Alice selected: %s' % alice.a)
print('Bob selected: %s' % bob.b)
ga = alice.publish()
gb = bob.publish()
print('Alice published: %s' % ga)
print('Bob published: %s' % gb)
sa = alice.compute_secret(gb)
sb = bob.compute_secret(ga)
print('Alice computed: %s' % sa)
print('Bob computed: %s' % sb)