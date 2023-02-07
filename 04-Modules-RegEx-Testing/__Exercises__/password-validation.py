# Password Validation

# Password requirements:
#   - 8 char long
#   - contain any sort of letters, numbers & $%#@
#   - has to end with a number

import re

regex = r"[A-Za-z0-9$%#@]{8,}\d"
pattern = re.compile(regex)

password = 'supersecret$%#@9'

check = pattern.fullmatch(password)

print(check)
