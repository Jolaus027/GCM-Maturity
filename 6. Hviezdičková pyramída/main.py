def cela_pyramida(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

def pol_pyramida(n):
    for i in range(n+1):
        print("*" * i)

def pol_pyramida_naopak(n):
    for i in range(n, 0, -1):
        print("*" * i)

def pol_pyramida_cela(n):
    for i in range(n+1):
        print("*" * i)
    for i in range(n, 0, -1):
        print("*" * i)

# callovanie a printy
print("#1")
cela_pyramida(5)
print("\n")

print("#2")
pol_pyramida(5)
print("\n")

print("#3")
pol_pyramida_naopak(5)
print("\n")

print("#4")
pol_pyramida_cela(5)