import pymysql

mydb = pymysql.connect(host='localhost',user='root',password='',database='banking_system')
mycursor = mydb.cursor()

class banker1:
    
    def __init__(self):
        
        #======Display Menu======
                
        print("Welcome to Banker's App\n")
        print("\t\tOperation Menu\n")
        print("\t\t1) Can Register")
        print("\t\t2) Can Login")
        print("\t\t3) Can Update all Customers")
        print("\t\t4) Can View all Customers")
        print("\t\t5) Can Delete all Customers\n")

    def Register():
        print("-------------------- Register ------------------------")
        emp_id = int(input("Enter employee id: "))
        emp_name = input("Enter employee name: ")
        mobile = input("Enter mobile: ")
        email_id = input("Enter email id: ")
        password = input("Enter Password: ")

        args = (emp_id,emp_name,mobile,email_id,password,)
        query = "insert into bank(emp_id,emp_name,mobile,email_id,password) values (%s,'%s',%s,'%s','%s')"

        mycursor.execute(query%args)
        print('register successfully done..')
        mydb.commit()
       
    #========View_customer============

    def Login():
        print("-------------------- login ------------------------")
        try:
            emp_id = int(input("Enter employee id: "))
            password = input("Enter Password : ")
            query="select * from bank where emp_id = %s"
            args = (emp_id)
            mycursor.execute(query%args)
            res = mycursor.fetchone()
            if emp_id != res[0]:
                print('Invalid Account number!!')
        except:
            print('Invalid Account number!!')
        else:
            if password == res[4]:
                print('login successfully done')
            else:
                print('invalid password')

    #======update Customer============

    def update():
        print("-------------------- Update all Customers ------------------------")
        try:
            Acno = int(input("Enter customer Account number :"))
            query="select * from customer where Acno = %s"
            args = (Acno)
            mycursor.execute(query%args)
            res = mycursor.fetchone()
            if Acno != res[0]:
                print('Invalid Account number!!')     
        except:
            print('Invalid Account number!!')
        else:
    
            status = True
            while status:
                print('\n1) Update first name \n2) Update last name \n3) Update mobile number \n4) Update email id \n5) password\n')
                ch = int(input('How do you Update feild please Enter :'))
                if ch == 1:
                    name = input('Enter first name: ')
                    query="UPDATE customer SET first_name = '%s' WHERE Acno = %s;"
                    args = (name,Acno)
                    mycursor.execute(query%args)
                    mydb.commit()
                    print('\n Update successfully')
                
                elif ch == 2:
                    name = input('Enter last name: ')
                    query="UPDATE customer SET last_name = '%s' WHERE Acno = %s;"
                    args = (name,Acno)
                    mycursor.execute(query%args)
                    mydb.commit()
                    print('\n Update successfully')

                elif ch == 3:
                    mobile = input('Enter mobile number: ')
                    query="UPDATE customer SET mobile = %s WHERE Acno = %s;"
                    args = (mobile,Acno)
                    mycursor.execute(query%args)
                    mydb.commit()
                    print('\n Update successfully')

                elif ch == 4:
                    email = input('Enter email id: ')
                    query="UPDATE customer SET email = '%s' WHERE Acno = %s;"
                    args = (email,Acno)
                    mycursor.execute(query%args)
                    mydb.commit()
                    print('\n Update successfully')

                elif ch == 5:
                    password = input('Enter password: ')
                    query="UPDATE customer SET password = '%s' WHERE Acno = %s;"
                    args = (password,Acno)
                    mycursor.execute(query%args)
                    mydb.commit()
                    print('\n Update successfully')

                else:
                    print('Invalid input please enter correct choice!!')

                con = input("Do you perform more operaions 'y' for yes or 'n' for no :")

                if con == 'n':
                    exit()

    #======view all Customer============

    def View_All_Customer():
        print("-------------------- DISPLAY All Customers ------------------------")
        mycursor.execute("select * from customer")
       
        res = mycursor.fetchall()
        for i in res:
            print(f' Account No:-  {i[0]}')
            print(f' First_Name:-  {i[1]}')
            print(f' Last_Name:-   {i[2]}')
            print(f' Mobile No:-   {i[3]}')
            print(f' Email:-       {i[4]}')
            print("========================")

        mydb.commit()

    #======Total Customer============
         
    def delete():
        print("-------------------- Delete all customers ------------------------")
        try:
            Acno = int(input("How do you remove customer please enter customer account number: "))
            query="select * from customer where Acno = %s"
            args = (Acno)
            mycursor.execute(query%args)
            res = mycursor.fetchone()
            if Acno != res[0]:
                print('Invalid Account number!!')     
        except:
            print('Invalid Account number!!')

        else:
            query="delete from customer where Acno = %s"
            args = (Acno)
            mycursor.execute(query%args)
            mydb.commit()
            print('\ndelete successfully done')