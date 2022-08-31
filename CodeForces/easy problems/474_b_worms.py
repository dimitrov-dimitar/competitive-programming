# https://codeforces.com/problemset/problem/474/B


def binary_search(piles, j, low, high):
    while True:
        mid = (low + high) // 2
        if piles[mid][1] <= j <= piles[mid][2]:
            return piles[mid][0]
        elif piles[mid][1] < j:
            low = mid + 1
        else:
            high = mid - 1


n = int(input())
n_arr = [int(x) for x in input().split()]
m = int(input())
m_arr = [int(x) for x in input().split()]

piles = []
start = 1
for i in range(1, n + 1):
    end = n_arr[i - 1] + start - 1
    # piles[i] = [start, end]
    piles.append([i, start, end])
    # piles[i] = [int(x) for x in range(start, end + 1)]
    start = end + 1
# print(piles)

for j in m_arr:
    print(binary_search(piles, j, piles[0][0], piles[-1][0]))
