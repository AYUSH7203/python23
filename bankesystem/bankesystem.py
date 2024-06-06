import customer as c1

while True:
    print('ROLE:')
    print('\t\t1)Banker')
    print('\t\t2)Customer')
    print('\t\t3)Exit\n')

    try:
        role = int(input('Enter your role: '))

    except:
        print("invalid input please enter correct input\n")
    
    else:

        if role == 1:
            while True:
                c1.banker1()
                try: 
                    choice = int(input('\nEnter your choice: '))

                except:
                    print("invalid choice please enter correct choice\n")

                else:
                    if choice == 1:
                        c1.banker1.Register()
                    elif choice == 2:
                        c1.banker1.Login()
                    elif choice == 3:
                        c1.banker1.update()
                    elif choice == 4:
                        c1.banker1.View_All_Customer()
                    elif choice == 5:
                        c1.banker1.delete()
                    else:
                       print("invalid choice please enter correct choice\n")

                    con = input("Do you perform more operaions 'y' for yes or 'n' for no :")

                    if con == 'n':
                        exit()
            

        elif role == 2:

            while True:
                c1.customer1()
                try: 
                    choice = int(input('\nEnter your choice: '))

                except:
                    print("invalid choice please enter correct choice\n")

                else:
                    if choice == 1:
                        c1.customer1.Register()
                    elif choice == 2:
                        c1.customer1.Login()
                    elif choice == 3:
                        c1.customer1.Withdraw_amount()
                    elif choice == 4:
                        c1.customer1.deposit_amount()
                    elif choice == 5:
                        c1.customer1.view_balance()
                        
                    else:
                       print("invalid choice please enter correct choice\n")

                    con = input("Do you perform more operaions 'y' for yes or 'n' for no :")

                    if con == 'n':
                        exit()

        elif role == 3:
            exit()

        else:
            print("invalid input please enter correct input\n")
    
       
    