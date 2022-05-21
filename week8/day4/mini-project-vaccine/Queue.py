class Queue:
    def __init__(self, queue_list):
        self.queue_list = queue_list

    # add human to our queue list
    def add_person(self, person):
        if person.age > 60:
            self.queue_list.insert(0, person.age)
        else:
            self.queue_list.append(person.age)

    # find the index inside our queue list
    def find_in_queue(self, person):
        return self.queue_list.index(person)

    # swaps person1 with person 2
    def swap(self, person1, person2):
        self.queue_list[self.find_in_queue(person1)] = person2

    def get_next(self):
        return self.queue_list[0]

    def get_next_blood_type(self, blood_type):
        i = 0
        for x in queue:
            if x.blood_type == blood_type:
                return x.blood_type

                

    def sort_by_age(self):
        pass
