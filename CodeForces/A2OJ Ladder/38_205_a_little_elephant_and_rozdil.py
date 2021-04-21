# https://codeforces.com/problemset/problem/205/A

n = int(input())
cities = [int(x) for x in input().split()]

min_citie = min(cities)
if cities.count(min_citie) > 1:
    print("Still Rozdil")
else:
    print(cities.index(min(cities)) + 1)
