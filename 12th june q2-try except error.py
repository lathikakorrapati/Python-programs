try:
    age = 12
    assert age>=0,"age is invalid"
    if(age>=18):
        print("the person is eligible to vote:",age)
    else:
        age2=18-age
        print("not eligible to vote and the age required to vote is:",age2)
except ValueError:
    print("enter the age in numericals only")