import random
import statistics

numbers = [random.randint(100, 150) for _ in range(100)]


mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)


print("Numbers:", numbers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
