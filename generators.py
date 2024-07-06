


cart = ['apple', 'orange', 'mango']
i = iter(cart)
print(next(i)) # apple
print(next(i)) # orange
print(next(i)) # mango



def cart_items():
    yield 'apple'
    yield 'orange'
    yield 'mango'

i = cart_items()
print(next(i)) # apple
print(next(i)) # orange
print(next(i)) # mango


for item in cart_items():
    print(item)


from itertools import chain, cycle

for value in chain([1,2,3], [4, 5, 6]):
    print(value) # 1 2 3 4 5 6

turns = cycle(['Player', 'Dealer'])
print(next(turns)) # Player
print(next(turns)) # Dealer
print(next(turns)) # Player
print(next(turns)) # Dealer
print(next(turns)) # Player
print(next(turns)) # Dealer


