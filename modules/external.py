# Install 3rd party modules via 'pip'.

from pyjokes import get_joke

joke = get_joke('en', 'neutral')
print(joke)
