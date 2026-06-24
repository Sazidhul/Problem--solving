N = int(input())
target = float(input())

total = 0

for i in range(N):
    loss = float(input())
    total += loss

average = total / N

if average <= target:
    print("PASS")
else:
    print("RETRY")