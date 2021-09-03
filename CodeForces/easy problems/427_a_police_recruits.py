# https://codeforces.com/problemset/problem/427/A

n = int(input())
events = [int(x) for x in input().split()]

counter = 0
free_officer = 0

for event in events:
    free_officer += event
    
    if free_officer < 0:
        counter += 1
        free_officer = 0

print(counter)
