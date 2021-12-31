values = ["1", "one", "un", "一",
    "2", "two", "deux", "二",
    "3", "three", "trois", "三",
    "4", "four", "quatre", "四",
    "5", "five", "cinq", "五",
    "6", "six", "six", "六",
    "7", "seven", "sept", "七",
    "8", "eight", "huit", "八",
    "9", "nine", "neuf", "九",
    "10", "ten", "dix", "十",
]

n = int(input())
for _ in range(n):
    one, two = input().split()
    print(values.index(one) // 4 + values.index(two) // 4 + 2)
