age=int(input("Enter your age"))
if age>=18:
   print("you are eligible to vote")
elif age==17:
    print("you are almost elgiable to vote")
elif age<0:
    print("you have entered an invalid age")

else:
    print("you are not eligible to vote")