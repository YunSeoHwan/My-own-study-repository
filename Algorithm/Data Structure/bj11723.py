import sys
n = int(input())
a = set()
for i in range(n):
    op = sys.stdin.readline()
    
    if op[0:3] == 'add':
        a.add(int(op[4:]))

    elif op[0:5] == 'check':
        if int(op[6:]) in a:
            print(1)
        else:
            print(0)

    elif op[0:6] == 'remove':
        if int(op[7:]) in a:
            a.remove(int(op[7:]))
    
    elif op[0:6] == 'toggle':
        if int(op[7:]) in a:
            a.remove(int(op[7:]))
        else:
            a.add(int(op[7:]))
    
    elif op[0:3] == 'all':
        a = set([i for i in range(1, 21, 1)])

    elif op[0:5] == 'empty':
        a = set([])