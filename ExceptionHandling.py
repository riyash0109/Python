# LEARNING TO TAKE USE DATETIME IN PYTHON
# LEARNING HOW TO USE EXCEPTION HANDLING IN OUR CODE
# HOW TO VALIDATE A INPUT DATE


from datetime import datetime
choice = 'y'
while ((choice == 'y') or (choice == 'Y')):

    print("**KNOW YOUR CHARACHTER BASED ON YOUR BIRTHDATE**")
    print("To QUIT press : Q")
    print("To know the format press : ?")

    Birthday = input("\tENTER YOUR DATE OF BIRTH : ")

    if Birthday == "":
        print("\tMy zodiac sign - Virgo : Elegant, perfectionist and picky!!!")

    elif Birthday == '?':
        print("\tPlease enter your date of birth in format(in DD/MM/YYYY): ")

    elif Birthday == 'q' or Birthday == 'Q':
        print("BYEE!!! HOPE YOU RUN THIS PROGRAM AGAIN!!!")
        break
    else:
        try:
            Birthdate = datetime.strptime(Birthday, "%d/%m/%Y").date()
            print("\tYour Birthday is : " + Birthdate.strftime('%d/%B/%Y'))
            Valid_Date = True
        except:
            Valid_Date = False

        if Valid_Date:
            day, month, year = Birthday.split("/")
            Valid_bday = True
            try:
                day = int(day)
                month = int(month)
                year = int(year)

            except ValueError:
                Valid_bday = False
            if (Valid_bday):
                print("The date of birth is valid ..")
                if month == 12:
                    if (day < 22):
                        print("Sagittarius : You are unconstrained, lively and loyal")
                    else:
                        print("Capricorn : You are perseverant, practical and lonely")
                elif month == 1:
                    if (day < 20):
                        print("Capricorn : You are perseverant, practical and lonely")
                    else:
                        print("Aquarius : You are smart, liberalistic and changeful")
                elif month == 2:
                    if (day < 19):
                        print("Aquarius : You are smart, liberalistic and changeful")
                    else:
                        print("Pieces : You are romantic, kind and sentimental")
                elif month == 3:
                    if (day < 21):
                        print("Pieces : You are romantic, kind and sentimental")
                    else:
                        print("Aries : You are energetic, candid and willful")
                elif month == 4:
                    if (day < 20):
                        print("Aries : You are energetic, candid and willful")
                    else:
                        print("Taurus : You are reliable, diligent and conservative")
                elif month == 5:
                    if (day < 21):
                        print("Taurus : You are reliable, diligent and conservative")
                    else:
                        print("Gemini : You are quick-witted, capricious and cheerful")
                elif month == 6:
                    if (day < 21):
                        print("Gemini : You are quick-witted, capricious and cheerful")
                    else:
                        print("Cancer : You are considerate, imaginative and sensitive")
                elif month == 7:
                    if (day < 23):
                        print("Cancer : You are considerate, imaginative and sensitive")
                    else:
                        print("Leo : You are enthusiastic, proud and arrogant")
                elif month == 8:
                    if (day < 23):
                        print("Leo : You are enthusiastic, proud and arrogant")
                    else:
                        print("Virgo : You are elegant, perfectionist and picky")
                elif month == 9:
                    if (day < 23):
                        print("Virgo : You are elegant, perfectionist and picky")
                    else:
                        print("Libra : You are equitable, charming and hesitant")
                elif month == 10:
                    if (day < 23):
                        print("Libra : You are equitable, charming and hesitant")
                    else:
                        print("Scorpio : You are insightful, mysterious and suspicious")
                elif month == 11:
                    if (day < 22):
                        print("Scorpio : You are insightful, mysterious and suspicious")
                    else:
                        print("Sagittarius : You are unconstrained, lively and loyal")
            else:
                print("The date of birth is not valid..")
        else:
            print("The date of birth is not valid..")

    choice = input("PRESS Y to continue : ")


#########################################################END OF PROGRAM########################################################################
