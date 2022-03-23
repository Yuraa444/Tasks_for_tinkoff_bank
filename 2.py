symbols = ''
AsB = input()
AsC = input()
BsC = input()


if AsB == '<' and AsC == '<':
    if BsC == '>':
        symbols = 'acb'
    else:
        symbols == 'abc'
elif AsB == '>' and AsC == '>':
    if BsC == '>':
        symbols = 'cba'
    else:
        symbols = 'bca'
elif AsB == '<' and AsC == '>':
    symbols = 'cab'
elif AsB == '>' and AsC == '<':
    symbols = 'bac'
elif AsB == '=':
    if AsC == '>':
        symbols = 'cba\ncab'
    else:
        symbols = 'abc'

print(symbols)
