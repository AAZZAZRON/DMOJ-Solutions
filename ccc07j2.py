txt_diction = {'CU': 'see you', ':-)': "I'm happy", ':-(': "I'm unhappy", ';-)': 'wink', ':-p': 'stick out my tongue',
               '(~.~)': 'sleepy', 'TA': 'totally awesome', 'CCC': 'Canadian Computing Competition', 'CUZ': 'because',
               'TY': 'thank-you', "YW": "you're welcome", 'TTYL': 'talk to you later'}

while True:
    x = input()
    if x in txt_diction.keys():
        print(txt_diction[x])
    else:
        print(x)
    if x == "TTYL":
        break
