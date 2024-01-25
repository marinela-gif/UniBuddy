
#Case Study Story:
# Imagine the first day of university for a freshman named
# Alex. Alex is excited but also overwhelmed by the vast campus, numerous courses,
# and the sea of new faces. To aid new students like Alex, the university's IT
# department has developed a personalised chatbot. This chatbot, named
# "UniBuddy", is designed to make the transition smoother for freshmen. Upon
# accessing the chatbot, Alex is prompted to enter their name, favourite colour, and
# age. Based on this input, UniBuddy offers a personalised greeting. For instance, if
# Alex's favourite colour is blue, UniBuddy might suggest joining the university's "Blue
# Art Club". If Alex is 18, the chatbot might provide information about
# freshman-specific events. The chatbot also offers a feature where Alex can input
# specific queries, like "Where is the library?" or "How do I join the debate club?", and
# UniBuddy responds with relevant information, all while adhering to a friendly tone,
# using string transformation methods to ensure the responses feel personalised
# and engaging.

#print welcome message

print('''
Welcome to UniBuddy app!
I will be your go to Buddy to make your freshman journey easier to access and enjoyable!
Please enter your credentials below to get started.
''')

# request input from user for name, age and fovourite colour
user_name = input("Please enter your name : "). capitalize()
user_age = int(input("Please enter your age :"))
fav_colour = input("Please enter your favourite colour : "). capitalize()

# printed out welcome message and suggestions
print(f"""
Welcome {user_name}! I can see you are {user_age} old and your favourite colour is {fav_colour}.
I have the following suggestion for your consideration!
""")
if fav_colour == 'Blue':
    print("If your favorite colour is blue, please look into the following options : ")

    print("""
1. Our Swimming competions which happen at the beginning of every term. 
2. Our Clean air club volunteering activities.
3. Our Wisdom society where we discuss campus challenges.          
""")
    
elif fav_colour == 'Red':
    print("If your favorite colour is blue, please check the following options : ")

    print("""
1. Our Digital fighting club.
2. Our Meat lovers cookery club.
3. Our Spanish dance club.
4. Our footbal club.          
 """)
    
elif fav_colour == 'Green':
    print("If your favorite colour is green, please check the following options : ")
    print(""" 
1. Our Vegetarian cookery club.
2. Our Green planet club.
3. Our Grow your own vegetables gardening club.
4. Our Run a marathon club.          
""")
    
elif fav_colour == 'White':
    print("If your favorite colour is white, please check the following options : ")
    print("""
1. Our Book reading club.
2. Our Restore a book club.                    
3. Our Learn to act club.
4. Our Charity by choice club.
""")
    
else:
    print("Please try again by choosing between these colours: red, blue, green or white! ")

# created options for freshman students
if user_age == 18:
    print("There are some freshman specific events to attend!")
    print(""" 
1. Movie event on every Friday evening at 6.00 pm.
2. Freshmans' Got talent competition on 10th December 2023 at 5.00 pm.
3. Pop a question event on 30th September at 3.00 pm.
4.                            
""")

else:
    print("There are some events that you might be interested to attend!")
    print("""
1. Career advice service drop offs sessions.
2. 1:1 career advice appointments.
3. Career fair events starting with 1st April 2024 events.             
""")

# requested questions from user and created answer options
user_question = input("""Please enter any question you might have here or type 'quit'
                      to end the session.""" )

if user_question == 'Where is the career service office?' :
    print("The carrer service office is situate on the third floor on the left.")

elif user_question == 'What are the canteen openning hours?':
    print("The canteen opening hours sre between 7.00 am to 8.30 pm.")

else:
    print("""This question requires additional support.
          Please contact the student support team on: 0208 339 2534, 
          alternatively send an email to: student.support@myuniversity.com.
          """)

