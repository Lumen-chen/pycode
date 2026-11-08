ch = input().strip()
n = ord(ch) - ord('A')
for i in range(0, n + 1):
    left = [chr(ord('A' ) + j) for j in range(0, i + 1)]
    right = [chr(ord('A') + j) for j in range(i - 1, -1, -1)]
    print(" " * (n - i) + "".join(left) + "".join(right))

