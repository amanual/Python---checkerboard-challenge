#Making and Reading from Dictionaries:
my_info = {"name: ":"Amanual","Country of birth: ":"Ethiopia","favorite language: ":"iOS"}
for var,data in my_info.iteritems():
    print var + data

#This also can be done as below:
def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)
dic = {"name: ":"Amanual","Country of birth: ":"Ethiopia","favorite language: ":"iOS"}
print_dictionary_values(dic)