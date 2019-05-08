from random import randint


# Big enough prime
INTEGER_QUOTIENT = 179426549


def generate_shares(x):
    share_a = randint(0, INTEGER_QUOTIENT)
    share_b = randint(0, INTEGER_QUOTIENT)
    share_c = (x - share_a - share_b) % INTEGER_QUOTIENT
    return share_a, share_b, share_c


secret_number1 = 1
secret_number2 = 0 
secret_number3 = 1 

shares1 = generate_shares(secret_number1)
shares2 = generate_shares(secret_number2)
shares3 = generate_shares(secret_number3)

server1 = shares1[0] + shares2[0] + shares3[0] % INTEGER_QUOTIENT
server2 = shares1[1] + shares2[1] + shares3[1] % INTEGER_QUOTIENT
server3 = shares1[2] + shares2[2] + shares3[2] % INTEGER_QUOTIENT


# Privately calculate aggregate of client data
result = sum([server1, server2, server3]) % INTEGER_QUOTIENT
print(result)

