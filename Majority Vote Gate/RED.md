# Ensemble Majority Voting

## 📌 Problem Overview

This program simulates an ensemble of mini-models where each model votes either **YES** or **NO** to admit a user.

The program counts the total number of **YES** and **NO** votes. If the number of **YES** votes is greater than or equal to the number of **NO** votes, the final decision is **ACCEPT**. Otherwise, the decision is **REJECT**.

This demonstrates the concept of **Ensemble Majority Voting**, where multiple weak decisions are combined to produce one stronger final decision.

---

## 📝 Input Format

The input consists of:

* An integer `N` representing the number of votes.
* The next `N` lines each contain either:

  * `YES`
  * `NO`

Example:

```text
5
YES
NO
YES
YES
NO
```

---

## 📤 Output Format

Print exactly one word:

* `ACCEPT` — if `YES_count >= NO_count`
* `REJECT` — otherwise

---

## 💡 Algorithm

1. Read the number of votes (`N`).
2. Initialize two counters:

   * `yes_count = 0`
   * `no_count = 0`
3. Read each vote one by one.
4. If the vote is `"YES"`, increase `yes_count`.
5. Otherwise, increase `no_count`.
6. Compare the two counters.
7. Print `ACCEPT` if `yes_count >= no_count`; otherwise print `REJECT`.

---

## 🐍 Python Solution

```python
N = int(input())

yes_count = 0
no_count = 0

for i in range(N):
    vote = input()

    if vote == "YES":
        yes_count += 1
    else:
        no_count += 1

if yes_count >= no_count:
    print("ACCEPT")
else:
    print("REJECT")
```

---

## 🧠 Concepts Used

* Input and Output
* Variables
* `for` Loop
* Conditional Statements (`if/else`)
* Counters
* Majority Voting Logic

---

## ⏱️ Time Complexity

**O(N)**

The program processes each vote exactly once.

---

## 💾 Space Complexity

**O(1)**

Only two counter variables are used regardless of the number of votes.

---

## 📖 Example

### Input

```text
5
YES
NO
YES
YES
NO
```

### Processing

* YES = 3
* NO = 2

Since:

```text
3 >= 2
```

Output:

```text
ACCEPT
```

---

## 🎯 Learning Outcome

This project demonstrates how to:

* Read multiple inputs using a loop.
* Count occurrences of different values.
* Make decisions using conditional statements.
* Implement the **Ensemble Majority Voting** technique, a simple concept commonly used in Machine Learning to combine predictions from multiple models.
