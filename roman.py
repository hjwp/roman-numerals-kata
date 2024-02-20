
def add(a, b):
    total = a + b
    total = total.replace("IIIII", "V")
    total = total.replace("VV", "X")
    return ''.join(sorted(total, reverse=True))