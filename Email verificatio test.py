email = input("Enter  Here you email:- ")
a = 0
b = 0
c = 0
if len(email) >= 7:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                if email[0::]!='..':
                    for i in email:
                        if i.isspace():
                            a=1
                        elif i.upper():
                            b=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="@" or i==".":
                            continue
                        else:
                            c=1
                    if  a==1 or b==1 or c==1:
                        print("Invalid Email5")
                    else:
                       print("Your email is right")
                else:
                    print("Invalid Email4")
            else:
                print("Invalid Email3")

        else:
            print("Invalid Email2")
    else:
        print ("Invalid Email1")
else:
    print("Invalid email")