# Walrus operator
text = 'helloooooooooo'

if len(text) > 10:
    print(f'too long {len(text)} elements')

if (n := len(text)) > 10:
    print(f'too long {n} elements')

while (n := len(text)) > 1:
    print(n)
    text = text[:-1]
