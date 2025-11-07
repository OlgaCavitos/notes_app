#Task1 String manipulation

name_1='helloworld'
if len(name_1)<2:
    print('')
else:
    print(name_1[:2]+name_1[-2:])

name_2='my'
if len(name_2)<2:
    print('')
else:
    print(name_2[:2]+name_2[-2:])

name_3='x'
if len(name_3)<2:
    print('')
else:
    print(name_3[:2]+name_3[-2:])



 #Task 2 The valid phone number program.
Phone_number='1234567805'
if len(Phone_number)!=10:
    print("The phone number is invalid")
elif not Phone_number.isdigit():
    print("The phone number is invalid")
else:
    print("The phone number is valid")

#Task 3 The math quiz program.

mathematical_expression="5*5"
correct_answer=25
user_answer=25
if user_answer==correct_answer:
    print(f"Correct {mathematical_expression}={correct_answer}")
else:
    print(f"Incorrect {mathematical_expression}={correct_answer}")

#Task 4 The name check.

My_name="olya"
input_name='Olya'
if input_name.lower()==My_name:
    print("names matches")
else:
    print("names do not match")

