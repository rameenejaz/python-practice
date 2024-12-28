point=(10,20)
print(f"X: {point[0]}, Y: {point[1]}")
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)
numbers=(1,2,3,4,5)
stats=get_stats(numbers)
print(stats)
