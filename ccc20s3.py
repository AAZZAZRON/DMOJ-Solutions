import sys
input = lambda: sys.stdin.readline()[:-1]


find = input()
full = input()
l = len(find)
if l > len(full):
    print(0)
    sys.exit()
EXP1 = 31
MOD1 = 1610612741
EXP2 = 37
MOD2 = 805306457
DIV1 = 1
DIV2 = 1
final = set()
hash1, slide1 = 0, 0
hash2, slide2 = 0, 0
real1, real2 = 0, 0
powers1, powers2 = [0] * 26, [0] * 26
powers1[0] = 1
powers2[0] = 1
for i in range(1, 26):
    powers1[i] = (powers1[i - 1] * EXP1) % MOD1
    powers2[i] = (powers2[i - 1] * EXP2) % MOD2

for i in range(l):
    hash1 = (hash1 + powers1[ord('z') - ord(find[i])]) % MOD1
    slide1 = (slide1 + powers1[ord('z') - ord(full[i])]) % MOD1

    hash2 = (hash2 + powers2[ord('z') - ord(find[i])]) % MOD2
    slide2 = (slide2 + powers2[ord('z') - ord(full[i])]) % MOD2

    real1 = (real1 * EXP1 + ord(full[i])) % MOD1
    real2 = (real2 * EXP2 + ord(full[i])) % MOD2

    if i:
        DIV1 = (DIV1 * EXP1) % MOD1
        DIV2 = (DIV2 * EXP2) % MOD2


if slide1 == hash1 and slide2 == hash2:
    final.add((real1, real2))
for i in range(l, len(full)):
    slide1 = (slide1 - powers1[ord('z') - ord(full[i - l])]) % MOD1
    slide1 = (slide1 % MOD1 + MOD1) % MOD1
    slide1 = (slide1 + powers1[ord('z') - ord(full[i])]) % MOD1

    slide2 = (slide2 - powers2[ord('z') - ord(full[i - l])]) % MOD2
    slide2 = (slide2 % MOD2 + MOD2) % MOD2
    slide2 = (slide2 + powers2[ord('z') - ord(full[i])]) % MOD2

    real1 = (real1 - ord(full[i - l]) * DIV1) % MOD1
    real1 = (real1 % MOD1 + MOD1) % MOD1
    real1 = (real1 * EXP1 + ord(full[i])) % MOD1

    real2 = (real2 - ord(full[i - l]) * DIV2) % MOD2
    real2 = (real2 % MOD2 + MOD2) % MOD2
    real2 = (real2 * EXP2 + ord(full[i])) % MOD2

    if slide1 == hash1 and slide2 == hash2:
        final.add((real1, real2))
print(len(final))
