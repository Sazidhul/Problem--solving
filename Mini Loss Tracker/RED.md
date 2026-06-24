# Average Loss Checker

## Problem Description

A tiny trainer reports a stream of loss values. The program reads the number of losses, a target loss value, and then the loss values themselves.

The average loss is calculated as:

average_loss = total_loss / N

The program prints:

* `PASS` if the average loss is less than or equal to the target.
* `RETRY` otherwise.

---

## Input Format

N
target
loss_1
loss_2
...
loss_N

Where:

* `N` = Number of loss values
* `target` = Target loss threshold
* `loss_i` = Individual loss values

---

## Output Format

Print exactly one word:

* `PASS`
* `RETRY`

---

## Example

### Input

3
0.35
0.20
0.30
0.40

### Output

PASS

---

## Solution Approach

1. Read the number of loss values (`N`).
2. Read the target loss value.
3. Use a loop to read all loss values and calculate their sum.
4. Compute the average loss.
5. Compare the average with the target.
6. Print `PASS` if average ≤ target, otherwise print `RETRY`.

---

## Python Solution

```python
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
```

## Concepts Used

* Input/Output
* Variables
* Arithmetic Operations
* For Loop
* Conditional Statements (`if/else`)
* Average Calculation

## Time Complexity

O(N)

## Space Complexity

O(1)
