arr = [3, 1, 9, 12, 17, 33, 5]
print("1.min =",min(arr))
def arg(f):
    s = 0
    for el in f:
        s += el
    return s / len(f)
print("2.cred_arifm =", arg(arr))
