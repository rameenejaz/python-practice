original={"a":1, "b":[2,3]}
copy=original.copy()
copy["b"].append(4)
print(original)
print(copy)
