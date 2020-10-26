# Perry Bunn

import math


class List(list):
    def swap_ends(self):
        temp = self[0]
        self[0] = self[len(self) - 1]
        self[len(self) - 1] = temp
        return self

    def shift(self):
        temp = self.pop(len(self) - 1)
        self.insert(0, temp)
        return self

    def replace_even(self):
        for x in range(len(self) - 1):
            if self[x] % 2 == 0:
                self[x] = 0
        return self

    def replace_largest_neighbor(self):
        for x in range(len(self) - 1):
            if x == 0 or x == len(self) - 1:
                continue
            else:
                largest = max(self[x - 1], self[x + 1])
                self[x] = largest
        return self

    # If the length of the list is 2 or less then the resulting list will be empty
    def remove_middle(self):
        if len(self) % 2 == 0:
            self.pop(math.ceil(len(self) / 2))
            self.pop(math.floor(len(self) / 2))
        else:
            self.pop(math.floor(len(self) / 2))
        return self

    def even_front(self):
        index = 0
        for x in range(len(self)):
            if self[x] % 2 == 0:
                temp = self.pop(x)
                self.insert(index, temp)
                index += 1
        return self

    # if the list is length 1 then it will return None
    def second_largest(self):
        try:
            self.sort(reverse=True)
            return self[1]
        except LookupError:
            return None

    def is_sorted(self):
        ref = self
        ref.sort()
        return ref == self

    def dup_adjacent(self):
        for x in range(len(self) - 1):
            if self[x] == self[x + 1]:
                return True
        return False

    def dup_items(self):
        temp = set(self)
        return len(temp) < len(self)


def menu(first: bool=False) -> bool:
    if first:
        print("Menu: \n\thelp: ?\n\tadd student: a\n\tremove student: r\n\tmodify grades: m\n\tprint all: p")
    res = input("")
    if res == "?":
        print("Menu: \n\thelp: ?\n\tadd student: a\n\tremove student: r\n\tmodify grades: m\n\tprint all: p")
        return True
    elif res == "a":
        add_student()
        return True
    elif res == "r":
        remove_student()
        return True
    elif res == "m":
        modify()
        return True
    elif res == "p":
        print_grades()
        return False

cont = True
menu(True)
while cont:
    cont = menu()




