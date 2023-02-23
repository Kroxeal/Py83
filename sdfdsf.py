# 3

v = input()


def check_variable(v):
    symbols = "!@#%^&*?"
    if v[0].isalpha():
        print(v[0])
        print(v[0].isalpha())
        print("Можно использовать")
    else:
        print("Нельзя использовать")


# Поработали, и хватит
while v != "Поработали, и хватит":
    check_variable(v)
    v = input()

print(v[0])
print(v[0].isalpha())
