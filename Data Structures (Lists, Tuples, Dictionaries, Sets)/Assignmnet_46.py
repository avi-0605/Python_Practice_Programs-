#Dictionary: Keys and Values Create a dictionary and then print just its keys and just its values separately.
def display_dict_components():
    sample_dict = {
        'name': 'John',
        'age': 25,
        'city': 'New York',
        'occupation': 'Engineer',
        'hobby': 'Reading'
    }
    
    print("Dictionary:", sample_dict)
    print("\nKeys:", list(sample_dict.keys()))
    print("Values:", list(sample_dict.values()))
    display_dict_components()
