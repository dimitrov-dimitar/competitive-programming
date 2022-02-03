# https://codeforces.com/problemset/problem/405/A

n = int(input())
cubes = [int(x) for x in input().split()]

cubes.sort()
cubes = [str(x) for x in cubes]

print(" ".join(cubes))
