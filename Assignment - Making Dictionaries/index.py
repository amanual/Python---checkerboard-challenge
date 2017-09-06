#Making Dictionaries
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "Aman"]

def make_dict(arr1, arr2):
    if len(arr1) >= len(arr2):
        zipped = zip(arr1, arr2)
        name_fav_dict = dict(zipped)
        return name_fav_dict        
    else:
        zipped = zip(arr2, arr1)
        name_fav_dict = dict(zipped)       
        return name_fav_dict

#Sample test:
arr1 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
arr2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "Aman"]
print make_dict(arr1, arr2)