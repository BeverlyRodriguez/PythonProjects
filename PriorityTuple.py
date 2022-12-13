
# Python’s tuple comparison, which takes into account the tuple’s 
# components, looking from left to right until the outcome is known.

person1 = ("Beverly", "Brown", 55)
person2 = ("Beverly", "Doe", 30)
person3 = ("Beverly", "Doe", 20)
person4 = ("Beverly", "Castro", 45)
person5 = ("Beverly", "Zamora", 50)

#These are the printing statements.
print("\nThese are the results: \n")
print("\tPERSON 1 < PERSON 3 is:  ", person1 < person2)
print("\tPERSON 2 < PERSON 3 is:  ", person2 < person3)
print("\tPERSON 1 < PERSON 4 is:  ", person1 < person4)
print("\tPERSON 3 < PERSON 4 is:  ", person3 < person4)
print("\tPERSON 2 < PERSON 5 is:  ", person2 < person5)