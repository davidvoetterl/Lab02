# Nr 2_1
list1 = [x for x in range(1, 21)]
print(list1)
list2 = [x ** 2 for x in range(1, 21)]
print(list2)
list3 = [x for x in list1 if x % 2 == 0]
print(list3)


# Nr 2_2
# Sorting:
# 1 :create your own datatype (class) -
#   you may want to read ahead and do something
#   that relates to your example for part 3.
# 2 :make it sortable, put it in a list
#   and sort the list.

class Boat:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def __repr__(self):
        return repr((self.name, self.speed, self.color))

    def ride(self):
        print(f"{self.name} is riding at a speed of {self.speed}")

    def __lt__(self, other):
        return self.speed < other.speed


list4 = [Boat("Frank", 14, "green"),
         Boat("Steve", 20, "blue"),
         Boat("Mark", 10, "purple")]

print(list4)
print(list4.sort(key=lambda boat: boat.speed))
print(sorted(list4))
