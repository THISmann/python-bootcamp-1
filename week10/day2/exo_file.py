# with open("secrets.txt", 'w',  encoding='utf-8') as f:
#     f.write("salut etienne ")

f = open('output.txt', 'w')
for i in range(10):
    f.write("this is line: %i\n" % i)
    f.read()
f.close()

# Same as
with open('output.txt', 'w') as f:
    for i in range(10):
        f.write("this is line: %i\n" % i)
