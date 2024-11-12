my_dict = {
    'name': 'Alice', 
    'age': 25 ,
    'city': 'Los Angeles',
    'hobbies': ['coding', 'playing guitar']
    }

another_dict = {
    'country': 'London', 
    'books': 'Thoughts',
    'movie': 'New York'
    }

new_dict = {**my_dict, **another_dict}

new_dict.clear()

print(new_dict)