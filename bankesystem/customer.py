from banker import banker1
import pymysql

mydb = pymysql.connect(host='localhost',user='root',password='',database='banking_system')
mycursor = mydb.cursor()

class customer1(banker1):
    
    def __init__(self):
        
        #======Display Menu======
                
        print("Welcome to Customer App\n")
        print("\t\tOperation Menu\n")
        print("\t\t1) Can Register")
        print("\t\t2) Can Login")
        print("\t\t3) Can Withdraw Amount ")
        print("\t\t4) Can deposit amount")
        print("\t\t5) Can view balance\n")

    def Register():
        print("-------------------- Register ------------------------")
        Acno = int(input("Enter Account number : "))
        first_name = input("Enter first_name : ")
        last_name = input("Enter last_name : ")
        mobile = input("Enter mobile : ")
        email = input("Enter Email-id : ")
        password = input("Enter Password : ")
        balance = int(input("Enter Balance : "))

        query = "insert into customer(Acno,first_name,last_name,mobile,email,password,balance) values (%s,'%s','%s','%s','%s','%s',%s) "
        args = (Acno,first_name,last_name,mobile,email,password,balance)
        mycursor.execute(query%args)
        
        print('register successfully done..')
        mydb.commit()

    #========View_customer============
    def Login():
        print("-------------------- login ------------------------")
        try:
            Acno = int(input("Enter Your Account number :"))
            password = input("Enter Password : ")
            query="select * from customer where Acno = %s"
            args = (Acno)
            mycursor.execute(query%args)
            res = mycursor.fetchone()
            if Acno != res[0]:
                print('Invalid Account number!!')
        except:
            print('Invalid Account number!!')
        else:
            if password == res[5]:
                print('login successfully done')
            else:
                print('invalid password')

    def Withdraw_amount():
        print("-------------------- Withdraw amount ------------------------")
        try:
            Acno = int(input("Enter Your Account number :"))
            password = input("Enter Password : ")
            query="select * from customer where Acno = %s"
            args = (Acno)
            mycursor.execute(query%args)
            res = mycursor.fetchone()
            if Acno != res[0]:
                print('Invalid Account number!!')
                
        except:
            print('Invalid Account number!!')
        else:
            if password == res[5]:
                amount = int(input('Enter Amount: '))
                balance1 = res[6]
                if  amount <= balance1:
                    balance = balance1 - amount
                    query="UPDATE customer SET balance = %s  WHERE acno = %s;"
                    args = (balance,Acno)
                    mycursor.execute(query%args)
                    mydb.commit()
                    print('\n Withdraw successfully')
                else:
                    print("\n Insufficient Balance\n")
            else:
                print('invalid password')

    def deposit_amount():
        print("-------------------- Deposit amount ------------------------")
        try:
            Acno = int(input("Enter Your Account number :"))
            password = input("Enter Password : ")
            query="select * from customer where Acno = %s"
            args = (Acno)
            mycursor.execute(query%args)
            res = mycursor.fetchone()
            if Acno != res[0]:
                print('Invalid Account number!!')
        except:
            print('Invalid Account number!!')
        else:
            if password == res[5]:
                amount = int(input('Enter Amount: '))
                balance1 = res[6]
                balance = balance1 + amount
                query="UPDATE customer SET balance = %s  WHERE acno = %s;"
                args = (balance,Acno)
                mycursor.execute(query%args)
                mydb.commit()
                print('\ndeposite successfully')
            else:
                print('invalid password')

    def view_balance():
        print("--------------------  view balance ------------------------")
        try:
            Acno = int(input("Enter Your Account number :"))
            password = input("Enter Password : ")
            query="select * from customer where Acno = %s"
            args = (Acno)
            mycursor.execute(query%args)
            res = mycursor.fetchone()
            if Acno != res[0]:
                print('Invalid Account number!!')
        except:
            print('Invalid Account number!!')
        else:
            if password == res[5]:
                balance = res[6]
                print('\nAmount is: ',balance)
                
            else:
                print('invalid password')