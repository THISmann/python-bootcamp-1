# with open("secrets.txt", 'w',  encoding='utf-8') as f:
# #     f.write("salut etienne ")

# f = open('output.txt', 'w')
# for i in range(10):
#     f.write("this is line: %i\n" % i)
# f.close()

# # Same as
# with open('output.txt', 'w') as f:
#     for i in range(10):
#         f.write("this is line: %i\n" % i)

import json

my_family = {
    "parents": ['Beth', 'Jerry'],
    "children": ['Summer', 'Morty']
}

json_file = "file.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent=2)
   #json.dump(obj2save , destination_file)
