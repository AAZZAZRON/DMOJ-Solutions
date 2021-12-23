HHVV = '''
1 2
3 4'''

HV = '''
4 3
2 1'''

V = '''
2 1
4 3'''

H = '''
3 4
1 2'''

flips = input()
h_count = flips.count('H')
v_count = flips.count('V')

if h_count % 2 == 0 and v_count % 2 == 0:
    print(HHVV)
elif h_count % 2 == 1 and v_count % 2 == 1:
    print(HV)
elif h_count % 2 == 0 and v_count % 2 == 1:
    print(V)
else:
    print(H)
