import string #To have the wanted character without writing a long list
import random #To have the ability to randomize things

list_lowercase = list(string.ascii_lowercase) #To have the ability to take random characters easily
list_uppercase = list(string.ascii_uppercase) #To have the ability to take random characters easily
list_digits = list(string.digits) #To have the ability to take random characters easily
list_allowed_panctuation=['@','#','_','@','#','_','@','#','_','@','#','_',] #To have the ability to take random characters easily and to ensure we are using the allowed things according to the rules
password_letters_list=[] #intiates a list for the letters we might use in the random generation
password_letters_list +=list_lowercase #put the lists we need
password_letters_list +=list_uppercase#put the lists we need
password_letters_list += list_digits #put the lists we need
password_letters_list += list_allowed_panctuation#put the lists we need
password_list=[]#initiate the list for the chosen characters for the password
def password_generator():
 def ending():#the ending of the generator
  while True:
     print('do you want to generate another password')
     desicions=input('write y if you want to and n if you dont')#asking the user if they want to make another password at the end
     if desicions.lower() =='y':#what will happen if they type y and this will ensure that even if the user types Y it will be y
        password_generator()
     elif desicions == 'n':#what will happen if they type n and this will ensure that even if the user types N it will be n
        exit() #this function will exit the whole app
     else:
       print('invalid option try again')
 while True:#to ensure that if an invalid option was entered the question will start again
   length_of_password= int(input('please enter your desired length of your password but make its equal to 8 or less than or equal 15'))#to make sure the number is in the integer form not the string
   if length_of_password >= 8 and length_of_password <= 15:# to make sure the user picked a length according to the rules
      for i in  range(length_of_password):
         random_character_password = random.choice(password_letters_list)
         password_list.append(random_character_password)
      generated_password="".join(password_list)
      print("here is your password: " + generated_password)
      ending()

         

 else:
   print('enter a valid value')
def rules():#for the user to know the rules from the rule.txt
    while True:
        question = input('Do you want to read the rules? (y/n): ')
        if question.lower() == 'y':
            print('1. Password length should at least be between eight and fifteen characters to avoid the employees forgetting about it ')
            print('2. Password should include at least one number')
            print('3. Password should consist of at least one uppercase letter')
            print('4. Password should consist of at least one lowercase letter')
            print('5. Password should consist of at least one punctuation from this list only [@,#,_]')
            print('6. password should not contain a space')

            while True:  
                examples = input('Do you want examples? (y/n): ')
                if examples.lower() == 'y':
                    print('Example 1: y#NIiOgjekV_')
                    print('Example 2: Mm@#@V@bYY5KLj')
                    break  # Exit examples loop
                elif examples.lower() == 'n':
                    password_generator()
                    return  # Exit the entire rules function
                else:
                    print('Invalid option. Try again.')
        elif question.lower() == 'n':
            password_generator()
            break  # Exit rules loop if the user doesn't want rules
        else:
            print('Invalid option. Try again.')

rules()