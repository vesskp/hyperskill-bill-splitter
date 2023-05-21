import random
# write your code here
people = {}

print("Enter the number of friends joining (including you):")
n = int(input())

if n > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(n):
        name = input()
        people[name] = 0
    print("Enter the total bill value:")
    total = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    ans = input().lower()
    if ans == "yes":
        lucky_name = random.choice(list(people))
        print(f"{lucky_name} is the lucky one!")
        for name in people:
            if name == lucky_name:
                people[name] = 0
            else:
                people[name] = total / (len(people)  - 1)
    else:
        print("No one is going to be lucky")      
        for name in people:
            people[name] = round(total / len(people), 2)
    print(people)
else:
    print("No one is joining for the party")
    