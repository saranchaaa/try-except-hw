result = []


def divider(a, b):
    a = int(a)
    b = int(b)

    if a < b:
        raise ValueError("a needs to be > or == b")
    if b > 100:
        raise IndexError("b needs to be < or == to 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 's': 15, 8: 4}

for i in data:
    try:
        res = divider(i, data[i])
        result.append(res)
    except (ValueError, IndexError) as e:
        print(f"Exception: {e}")

print(result)
