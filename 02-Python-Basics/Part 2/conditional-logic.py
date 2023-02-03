# Conditional Logic
is_old = False
is_licenced = True

if is_old and is_licenced:
    print('You are old enough to drive, and you have a licence!')
elif is_licenced:
    print('You can drive now!')
else:
    print('You are not of age!')

print('Okay')

# Truthy vs Falsey
username = 'johnny'
password = '123'

if username and password:
    print('Username and password are ok!')
else:
    print('Invalid credentials')
