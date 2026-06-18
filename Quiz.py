print("MCQ Based Quiz!")
def mcq_quiz():
    Questions=[ {'Q_':"Which data type is immutable ?",
                 'options':["A)List","B)Tuple","C)Set","D)Dictionary"],
                 'Answer':"B"},
                {'Q_':"Which mode creates a file but gives error if file already exists ?",
                  'options':["A)w","B)a","C)x","D)r"],
                  'Answer':"C"},
                {'Q_':"What is the advantages of using 'with open()' ?",
                 'options':["A)Faster execution","B)Automatically closes file","C)Deletes file","D)None"],
                 'Answer':"B"},
                {'Q_':"Which mode is used for binary files ?",
                 'options':["A)rb","B)ab","C)wb","D)All of these"],
                 'Answer':"D"},
                {'Q_':"Which module is required for file operations like delete/rename ?",
                 'options':["A)sys","B)file","C)os","D)None"],
                 'Answer':"C"},
                {'Q_':"What happens if you don't close a file ?",
                 'options':["A)Nothing","B)Data loss possible","C)Error","D)Delete File"],
                 'Answer':"B"},
                {'Q_':"What does 'seek()' do ?",
                 'options':["A)Reads file","B)Moves the pointer","C)Closes file","D)Deletes file"],
                 'Answer':"B"}
                ]
    score = 0

    for i in Questions:
        print("\n"+i['Q_'])
        for option in i['options']:
            print(option)
        valid_option = ["A","B","C","D"]
        guess=input("Enter your option :").upper()

        while guess not in valid_option:
            guess=input("Enter your option by choosing (A,B,C,D) only :").upper()
            if guess not in valid_option:
                print("Invalid Option! Enter option by choosing (A,B,C,D) only!!")

        if guess==i['Answer']:
            print("Correct!! You are Brilliant!")
            score +=1
        else:
            print("Wrong!! But hey, learning is winning!")
        
    print("\n--- Quiz is Over---⏱")
    print(f"Your Score is : {score}/{len(Questions)}")

    if score==len(Questions):
        print("100% Score!, You're unstoppable!")
    elif 4<= score <=6 :
        print("Nice One!, Almost PRO level!  ")
    elif 1<= score <=3:
        print("Need to improve!, It's happen sometime!")
    else:
        print("Zero! Even Google is shocked!")

mcq_quiz()