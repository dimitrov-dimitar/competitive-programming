# https://codeforces.com/problemset/problem/785/A

n = int(input())

sum_faces = 0

for _ in range(n):
    polyhedrons = input()
    if polyhedrons == 'Tetrahedron':
        sum_faces += 4
    elif polyhedrons == 'Cube':
        sum_faces += 6
    elif polyhedrons == 'Octahedron':
        sum_faces += 8
    elif polyhedrons == 'Dodecahedron':
        sum_faces += 12
    else:
        sum_faces += 20

print(sum_faces)
