cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# this is the correct way that you add a item to the list if you += it will add each letter of the string as a letter.
cheese.append('Oke')
# this is to add to the list with more then one item so making it a seperate list then extending that onto it.
extraCheese = ['Bree', 'Camanbert']
cheese.extend(extraCheese)


print(cheese)