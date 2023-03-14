n, k = map(int, input().split())
a = list(map(int, input().split()))

# Initialize an array of size k to store the frequency of remainders
remainder_count = [0] * k

# Count the frequency of each remainder
for i in range(n):
    remainder_count[a[i] % k] += 1

# Calculate the number of unordered pairs whose sum is divisible by k
pair_count = 0
for i in range(1, k//2+1):
    if i != k-i:
        pair_count += remainder_count[i] * remainder_count[k-i]
    else:
        pair_count += remainder_count[i] * (remainder_count[i]-1) // 2

# Add the count of pairs whose sum is divisible by k itself
pair_count += remainder_count[0] * (remainder_count[0]-1) // 2

print(pair_count)
