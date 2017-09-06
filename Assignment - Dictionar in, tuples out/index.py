#Dictionary in, tuples out
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
list_dict = []
for key,data in my_dict.iteritems():
    list_dict.append((key,data))
print list_dict