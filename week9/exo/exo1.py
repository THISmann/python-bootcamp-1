#################################################################################################################################
# defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter
import itertools
import collections
from collections import namedtuple
from collections import defaultdict
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
nums['three'] = 3
print(nums['four'])

#################################################################################################################################
# Counter
list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1, 2, 2]
answer = Counter()
answer = Counter(list)
print(answer[2])

#################################################################################################################################
# deque
# initialization
list = ["a", "b", "c"]
deq = deque(list)
print(deq)

# insertion
deq.append("z")
deq.appendleft("g")
print(deq)
# removal
deq.pop()
deq.popleft()
print(deq)

#################################################################################################################################
# namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('Peter', 'James', '13')
print(s1.fname)

#################################################################################################################################
# ChainMap

dictionary1 = {'a': 1, 'b': 2}
dictionary2 = {'c': 3, 'b': 4}
chain_Map = collections.ChainMap(dictionary1, dictionary2)
print(chain_Map.maps)

# OrderedDict
order = OrderedDict()
order['a'] = 1
order['b'] = 2
order['c'] = 3
print(order)

# unordered dictionary
unordered = dict()
unordered['a'] = 1
unordered['b'] = 2
unordered['c'] = 3
print("Default dictionary", unordered)


# print the first four even numbers

result = itertools.count(start=0, step=2)

for number in result:
    # termination condition
    if number < 8:
        print(number)
    else:
        break


# print 2 three times

result = itertools.cycle('12345')
counter = 0

for number in result:
    # termination condition
    if counter < 10:
        print(number)
        counter = counter + 1
    else:
        break


# print hello two times

result = itertools.repeat('hello', times=2)

for word in result:
    print(word)


# iterate over three lists

list_one = ['a', 'b', 'c']
list_two = ['d', 'e', 'f']
list_three = ['1', '2', '3']

result = itertools.chain(list_one, list_two, list_three)

for element in result:
    print(element)


# find the names of people who have the flu

names = ['Alice', 'James', 'Matt']
have_flu = [True, True, False]

result = itertools.compress(names, have_flu)

for element in result:
    print(element)

# dropwhile

my_list = [0, 0, 1, 2, 0]

result = itertools.dropwhile(lambda x: x == 0, my_list)

for elements in result:
    print(elements)
