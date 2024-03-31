result = []
try:
    def divider(a, b):
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b


    data = {10: 2, 2: 5, "123": 4, 18: 0, '': 15, 8: 4}
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except ValueError:
    print([10/2, 8/4])

except IndexError:
    print([2/5, "123"/4, 18/0, ''/15])
    