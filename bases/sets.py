
"""Intersection of the sets"""
print("\nIntersection of the sets:\n".upper())

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6, 7}

print(set_A & set_B) #shows intersections of sets
print(set_A)
print(set_B)
print('='*30)

inter = set_A & set_B
print(inter)
print('='*30)

set_A &= set_B # change initial set_A to the new value
print(set_A)
print(set_B) # set_B is not changed
print('='*30)

set_B &= set_A # change initial set_B to the new value
print(set_A)
print(set_B)
print('='*30)

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6, 7}

intersect = set_A.intersection(set_B) # create new set with result not mutating set_A and set_B
print(intersect)
print(set_A)
print(set_B)
print('='*30)

set_A.intersection_update(set_B) # the same operation as set_A &= set_B -> will mutate the initial set_A

"""Joining the sets"""
print("Joining the sets:\n".upper())

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6, 7}

print(set_A | set_B) # joins elements between 2 sets
print(set_A)
print(set_B)
print('='*30)

set_A |= set_B # joins elements between 2 sets mutating set_A
print(set_A)
print(set_B)
print('='*30)

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6, 7}

united = set_A.union(set_B) #return new united set of set_A and set_B
print(united)
print(set_A)
print(set_B)
print('='*30)


"""Deduction of the sets"""
print("Deduction the sets:\n".upper())

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6, 7}

print(set_A - set_B) # display set of elements of set_A which are not duplicated in set_B
print(set_B - set_A) # display set of elements of set_B which are not duplicated in set_A
print(set_A)
print(set_B)
print('='*30)


set_A -= set_B # deduct set_B from set_A and mutate the set_A

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6, 7}

difference = set_A.difference(set_B)

"""Symmetrical difference - set with elements which are not repeated in initial 2 sets"""
print("Symmetrical difference the sets:\n".upper())

print(set_A ^ set_B) # display new set with elements which contains only in set_A and only in set_B
print('='*30)


"""Comparing sets"""
print("COMPARING SETS")

set_A = {1, 2, 3}
set_B = {3, 1, 2}
print(set_A == set_B) # True
print(set_B != set_A) # False
print('='*30)

set_A = {1, 2, 3}
set_B = {3, 1, 2, 4, 5}

print(set_B > set_A) # True, because set_A is subset of set_B
print(set_B < set_A) # False
print('='*30)


set_A.add(22) # now set_A is {1, 2, 3, 22} and set_B is {3, 1, 2, 4, 5}

print(set_A > set_B) # false - set_B is not the subset of set_A
print(set_A < set_B) # false - set_A is not the subset of set_B
print('='*30)

set_A = {1, 2, 3}
set_B = {3, 1, 2}

print(set_A > set_B) # False - when sets are equal no one is subset of another
print(set_A >= set_B) # True - equal or more will return True to equal between sets
