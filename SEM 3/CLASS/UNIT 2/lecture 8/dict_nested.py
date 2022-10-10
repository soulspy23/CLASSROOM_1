#30th July 2022

#nested dictionary

my_family = {
    "child-1":{
        "name": "John",
        "age": 5
    },
    "child-2":{
        "name": "Marry",
        "age": 7
    },
    "child-3":{
        "name": "Bob",
        "age": 3
    }
}

print("Information of child-1 :-",my_family["child-1"])
print("Name of child-2 :",my_family["child-2"]["name"])