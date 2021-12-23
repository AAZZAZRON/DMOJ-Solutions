one = "          |\n       \  |  /\n        \ | /\n         \|/\n       XXXXXXX\n      X       X\n     X  O   O  X\n    X     V     X\nW   X  X     X  X\n \   X  XXXXX  X\n  \   X       X\n   \   XXXXXXX\n    \ X       X---\n     X    O    X  \\\n    X           X  \\\n     XXXXXXXXXXX    \\\n      OOOO OOOO      M\n      OOOO OOOO"
two = "          |\n       \  |  /\n        \ | /\n         \|/\n       XXXXXXX\n      X       X\n     X  O   O  X\n    X     V     X\nW   X  X     X  X\n \   X  XXXXX  X\n  \   X       X\n   \   XXXXXXX\n    \ X       X---\n     X    O    X  \\\n    X           X  \\\n     XXXXXXXXXXX    \\\n     X         X     M\n    X     O     X\n   X      O      X\n  X               X\n   XXXXXXXXXXXXXXX\n      OOOO OOOO\n      OOOO OOOO"
body = [
"          |",
"       \  |  /",
"        \ | /",
"         \|/",
"       XXXXXXX",
"      X       X",
"     X  O   O  X",
"    X     V     X",
"W   X  X     X  X",
" \   X  XXXXX  X",
"  \   X       X",
"   \   XXXXXXX",
"    \ X       X---",
"     X    O    X  \\",
"    X           X  \\",
"     XXXXXXXXXXX    \\",
"     X         X     M",
"    X     O     X",
"   X      O      X",
"  X               X",
"   XXXXXXXXXXXXXXX"
]

for q in range(5):
    num = int(input())
    if num == 1:
        print(one)
    elif num == 2:
        print(two)
    else:
        index = num * (num + 1) // 2 - 5
        align = num * (num + 1) // 2 - 2
        middle = 6
        buttons = 3
        for i in body: # torso up to size 2
            print(" " * index + i)
        for _ in range(num - 2):
            print(" " * align + "X" + " " * middle + " " + " " * middle + "X")
            for _ in range(buttons):
                align -= 1
                middle += 1
                print(" " * align + "X" + " " * middle + "O" + " " * middle + "X")
            buttons += 1
            align -= 1
            middle += 1
            print(" " * align + "X" + " " * middle + " " + " " * middle + "X")
            align += 1
            middle -= 1
            print(" " * align + "X" * (2 * middle + 3))
        for _ in range(2): # feet
            print(" " * index + "      OOOO OOOO")
    if q != 4:
        print("")
