# This is an age judge

age = int(input('What is your age: '))
driving = input('Have you ever driven the car (Type "Yes" or "No"): ')
print('Your age is', age)
# raise SystemExit 

if driving == 'Yes':
    if age >= 18:
        print('You are ok')
    else:
        print('You cannot drive')
elif driving == 'No':
    if age >= 18:
        print('Please go to get driving liscence')
    else:
        print('Please do not drive')
else:
    print('Please tpye "Yes" or "No"')