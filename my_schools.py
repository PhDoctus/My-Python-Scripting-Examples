#Create program that appends school name to list until user is complete


def SchoolName():

    my_schools = []

    while True:

            Name: str = input('Please provide the name of your university: ')
    
            my_schools.append(Name.title())

            return print(my_schools)
    



SchoolName()

# why can I not figure out how to insert/append an item to a list? why are int's not iterable?


'''ans = []

for item in  len(ans):

    num: int = int(input())

    abc = num ** 2

    ans.insert(0, abc)


print(ans)'''
