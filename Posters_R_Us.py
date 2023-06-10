def result_1():
    print("\nFirst Name - " + f_n + "\nSurname - " + s_n + "\nEmail - " + email + 
    "\nPhone Number -  " + str(p_n) + "\nTotal Cost Of Posters - £" + "%.2f" %  amnt_3)
def result_2():
    print("\nFirst Name - " + f_n + "\nSurname - " + s_n + "\nEmail - " + email + 
    "\nPhone Number - " + str(p_n) + "\nTotal Cost Of Posters - £" + "%.2f" % amnt_1)


def post_amnt():
    global amnt_1
    global amnt_3
    print("Hi " + f_n + ",\nWhat is the length and width of your poster")
    length = int(input("Length: "))
    if length == str:
        print("Worng format")
        post_amnt()
    else:
        width = int(input("Width: "))
        if width == str:
            print("Wrong format")
            post_amnt()
        else:
            size = length + width
            poster = int(input("How many posters(min 10): "))
            if poster > 10:
                amnt_1 = 10 * (size * 0.03)
                poster -= 10
                amnt_2 = poster * (size * 0.75)
                amnt_3 = amnt_1 + amnt_2
                p_type = input("""What paper type:
115gm - no extra charge
135gm - extra 5p per poster
PVC - extra 35p per poster\n""")
                if p_type == "115gm":
                    result_1()
                
                elif p_type == "135gm":
                    amnt_3 += 0.05
                    result_1()
                
                elif p_type == "PVC":
                    amnt_3 += 0.35
                    result_1()

            elif poster == 10:
                amnt_1 = 10 * (size * 0.03)
                p_type = input("""What paper type:
115gm - no extra charge
135gm - extra 5p per poster
PVC - extra 35p per poster\n""")
                if p_type == "115gm":
                    result_2()
                
                elif p_type == "135gm":
                    amnt_1 += 0.05
                    result_2()
                
                elif p_type == "PVC":
                    amnt_1 += 0.35
                    result_2()     
                
            else:
                print("Validation Error 0x34758")
                post_amnt()


def posters():
    global f_n
    global s_n
    global email
    global p_n
    try:
        f_n = input("First Name: ")
        s_n = input("Surname: ")
        email = input("Email: ")
        p_n = int(input("Phone Number: "))
    
    except:
        print("Validation Error 0x34758")
        posters()

    else:
        post_amnt()

print("Welcome to Posters R Us poster maker/ordering interface")
posters()
