#collect user preferences 
#-length
#-should contain uppercse
#-should contain lowercase
#-should contain special char
#-should contain digits

#create all available characters
#randomly pick char upto length 
#ensure we have atleast one char type
#ensure length is valid

import random 
import string

def generate_password():
    length=int(input("Enter the desired password length: ").strip())
    include_uppercase=input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special=input("Include special characters? (yes/no): ").strip().lower()
    include_digits=input("Include digits? (yes/no): ").strip().lower()

    if length<4:
        print("Password length must be atleast 4 characters.")
        return
    
    lower=string.ascii_lowercase
    uppercase=string.ascii_uppercase if include_uppercase=="yes" else ""
    special=string.ascii_uppercase if include_special=="yes" else ""
    digits=string.digits if include_digits=="yes" else ""
    all_characters=lower+uppercase+special+digits

    required_characters=[]
    if include_uppercase=="yes":
        required_characters.append(random.choice(uppercase))
    if include_special=="yes":
        required_characters.append(random.choice(special))
    if include_digits=="yes":
        required_characters.append(random.choice(digits))


    remaining_length=length-len(required_characters)
    password=required_characters

    for _ in range(remaining_length):
        character=random.choice(all_characters)
        password.append(character)


    random.shuffle(password)

    str_password="".join(password)
    return str_password

password=generate_password()
print(password)



generate_password()