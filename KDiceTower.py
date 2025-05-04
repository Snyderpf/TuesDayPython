def diceTower(n, top_first):
    sides = []
    for _ in range(n):
        a, b = map(int, input().split())
        sides.append((a, b))

    for a, b in sides:
        if a == top_first or a == 7 - top_first or b == top_first or b == 7 - top_first:
            print("NO")
            return

    print("YES")


n = int(input())
x = int(input())
diceTower(n, x)