# I couldn't solve it myself, so I looked up the answer and I wrote it down again without looking, this is the answer from chatGPT BTW
count = 0
def hanoi(a, b, c, n):
    global count

    if n == 0:
        return
    hanoi(a, c, b, n - 1)
    c.append(a.pop())
    print(f"\n\nA = {a}\nB = {b}\nC = {c}")
    count += 1
    hanoi(b, a, c, n - 1)

hanoi([3, 2, 1], [], [], 3)
print(count)

