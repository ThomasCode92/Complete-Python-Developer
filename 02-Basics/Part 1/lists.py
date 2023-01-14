# lists
li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[1])

# list slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[0:2])
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[1:3]
new_cart[0] = 'gum'
print(amazon_cart)
print(new_cart)

# list methods
basket = [1, 2, 3, 4, 5]
print(len(basket))

new_list = basket[:]
new_list.append(100)
print(new_list)

new_list = basket[:]
new_list.insert(4, 100)
print(new_list)

new_list = basket[:]
new_list.extend([100, 101])
print(new_list)

removed_item = new_list.pop()
new_list.pop(4)
print(new_list, removed_item)

new_list.remove(4)
print(new_list)

new_list.clear()
print(new_list)

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d'))
print('d' in basket)
print(basket.count('d'))

new_basked = sorted(basket)
basket.sort()
new_basked.reverse()
print(basket)
print(new_basked)

print(list(range(100)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)

# list unpacking
basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, c, *other, d = basket
print(a, b, c, d)
print(other)
