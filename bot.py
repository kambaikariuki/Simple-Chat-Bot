import time
botName = "Aid"
birthYear = 2024

def greet(botName, birthYear):
    print(f'Hello! My name is {botName}')
    
    print(f'I was created in {birthYear}')
    

def remind_name():
    your_name = input('Please remind me your name.\n')
    print(f'What a great name you have, {your_name}!')

def count_num():
    print('Now I will prove to you that I can count any number, try me!')
    print('What number do you want to count to?')
    number = int(input())
    print('Okay, counting...')
    for x in range(number):
        print(x)
        time.sleep(0.5)
    print('Completed! Have a nice day!')

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of your age divided by 3, 5 and 7')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = ((rem3 * 70 + rem5 * 21 + rem7 * 15) % 105)
    print('Hmmm, let\'s see...')
    print(f'Your age is {age}; that\'s a good time to start programming.')


greet("Ex-boot 2000", 2000)
remind_name()
guess_age()
count_num()


