sleeping_rating = 5
ice_cream_rating = 6
first_name = 'Pit'
last_name = 'Christodoulou'
my_name = first_name + ' ' + last_name

happiness_rating = (sleeping_rating + ice_cream_rating) / 2


print("happiness_rating variable type is ", type(happiness_rating), '\n',
      "my_name variable type is ", type(my_name), '\n',
      "ice_cream_rating variable type is ", type(ice_cream_rating), '\n')


print('My name is ' + first_name + ' and I give eating ice cream a score of ' + str(ice_cream_rating) + ' out of 10!')
print('I am ' + my_name + ' and my sleeping enjoyment rating is ' + str(sleeping_rating) + ' / 10!')
print('Based on the factors above, my happiness rating is ' + str(happiness_rating) + ' out of 10, or 85.0 %!')

