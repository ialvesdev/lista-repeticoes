n = int(input())

for _ in range(n):
    v1, v2, v3 = map(float, input().split())
    media = (v1 * 2) + (v2 * 3) + (v3 * 5)
    media = media / 10
    print(f"{media:.1f}")
    