my_dict = {"name": "John", "age": 25, "city": "New York"}
print("Original Dictionary:", my_dict)
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
my_dict["country"] = "USA"
print("Updated Dictionary:", my_dict)
del my_dict["age"]
print("Dictionary after deletion:", my_dict)
print("Is 'name' in the dictionary?", "name" in my_dict)
print("Dictionary keys:", my_dict.keys())
print("Dictionary values:", my_dict.values())
print("Dictionary items:", my_dict.items())
print("Dictionary length:", len(my_dict))
list_from_dict = list(my_dict.items())
print("Dictionary converted to list of tuples:", list_from_dict)