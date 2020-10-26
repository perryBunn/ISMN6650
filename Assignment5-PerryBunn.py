import math


class List(list):
    def swap_ends(self):
        temp = self[0]
        self[0] = self[len(self) - 1]
        self[len(self) - 1] = temp
        return self

    def shift(self):
        temp = self.pop(len(self)-1)
        self.insert(0, temp)
        return self

    def replace_even(self):
        for x in range(len(self) - 1):
            if self[x] % 2 == 0:
                self[x] = 0
        return self

    def replace_largest_neighbor(self):
        for x in range(len(self) - 1):
            if x == 0 or x == len(self)-1:
                continue
            else:
                largest = max(self[x-1], self[x+1])
                self[x] = largest
        return self

    # If the length of the list is 2 or less then the resulting list will be empty
    def remove_middle(self):
        if len(self) % 2 == 0:
            self.pop(math.ceil(len(self)/2))
            self.pop(math.floor(len(self)/2))
        else:
            self.pop(math.floor(len(self)/2))
        return self


A = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B = List([1, 4, 8, 16, 25])
C = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
D = List([1,2,3,4,5])
E = List([1,4])
F = List([0])

if __name__ == '__main__':
    print(A.swap_ends())                    # swap ends
    print(B.shift())                        # shift right
    print(A.replace_even())                 # replace evens
    print(C.replace_largest_neighbor())     # replace with largest neighbor
    print(D.remove_middle())                # remove middle
    print(E.remove_middle())
    print(F.remove_middle())
