from Account_holder import Account_holder
import os

run = True

def get_accno():
    # If file doesn't exist yet, create it and return 0
    if not os.path.exists("Account_holders.txt"):
        open("Account_holders.txt", "w").close()
        return 0
        
    accno_g = open("Account_holders.txt" , 'r')
    Accounts = accno_g.readlines()
    accno_g.close()
    
    # Filter out empty strings or blank lines
    Accounts = [line.strip() for line in Accounts if line.strip()]
    
    if not Accounts:
        return 0
        
    last_acc = Accounts[-1]
    # Split by space to easily grab the last element (the account number)
    parts = last_acc.split()
    if len(parts) >= 4:
        return int(parts[3])
    return 0

while (run):
    print("\n**************************Welcome to The Bank of Krishna**************************")
    print("Select An Operation You want to Perform: ")
    print("1. Create Account")
    print("2. Delete Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Exit Application")

    try:
       opt = int(input("Enter the Number Before the Operation: "))
    except (TypeError, ValueError):
        print("Please Enter A Valid Number Before An Operation")
        continue

    if opt == 1:
        print("\n--- Creating An Account ---")
        name = str(input("Please Enter Your name: "))
        age = str(input("Please Enter Your age: "))
        balance = str(input("Please Enter Your initial balance: "))
        
        next_acc_no = get_accno() + 1

        add_acc = open("Account_holders.txt", "a")
        # Ensure data formatting matches: name age balance accno
        add_acc.write(f"{name} {age} {balance} {next_acc_no}\n")
        add_acc.close()

        print("Your Account has Been Created...")
        print("This Is your Account No: " + str(next_acc_no))

    elif opt == 2:
        print("\n--- Deleting Your Account ---")
        acc_d_no = input("Enter Your Account Number to Delete: ").strip()

        if not os.path.exists("Account_holders.txt"):
            print("No accounts exist yet.")
            continue

        del_acc = open("Account_holders.txt" , "r")
        lines = del_acc.readlines()
        del_acc.close()

        found = False
        new_lines = []
        for line in lines:
            parts = line.split()
            # If line matches data structure and the account number matches, skip it
            if len(parts) >= 4 and parts[3] == acc_d_no:
                found = True
                continue # Skip writing this line to delete it
            new_lines.append(line)

        if found:
            rewrite_acc = open("Account_holders.txt", "w")
            rewrite_acc.writelines(new_lines)
            rewrite_acc.close()
            print("Deletion Successful...")
        else:
            print("Account Number Not Found.")

    elif opt == 3:
        print("\n--- Deposit Money ---")
        acc_no = input("Enter Your Account Number: ").strip()
        dep_amount = float(input("Enter Amount to Deposit: "))

        if not os.path.exists("Account_holders.txt"):
            print("No accounts found.")
            continue

        file_acc = open("Account_holders.txt", "r")
        lines = file_acc.readlines()
        file_acc.close()

        found = False
        new_lines = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 4 and parts[3] == acc_no:
                found = True
                # Reconstruct record using Account_holder class object
                holder = Account_holder(parts[0], parts[1], parts[2], parts[3])
                holder.balance += dep_amount
                new_lines.append(f"{holder.name} {holder.age} {holder.balance} {holder.accno}\n")
                print(f"Deposited successfully. New Balance: {holder.balance}")
            else:
                new_lines.append(line)

        if found:
            writer = open("Account_holders.txt", "w")
            writer.writelines(new_lines)
            writer.close()
        else:
            print("Account Number Not Found.")

    elif opt == 4:
        print("\n--- Withdraw Money ---")
        acc_no = input("Enter Your Account Number: ").strip()
        with_amount = float(input("Enter Amount to Withdraw: "))

        if not os.path.exists("Account_holders.txt"):
            print("No accounts found.")
            continue

        file_acc = open("Account_holders.txt", "r")
        lines = file_acc.readlines()
        file_acc.close()

        found = False
        new_lines = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 4 and parts[3] == acc_no:
                found = True
                holder = Account_holder(parts[0], parts[1], parts[2], parts[3])
                
                # Check for sufficient balance
                if holder.balance >= with_amount:
                    holder.balance -= with_amount
                    new_lines.append(f"{holder.name} {holder.age} {holder.balance} {holder.accno}\n")
                    print(f"Withdrawal successful. Remaining Balance: {holder.balance}")
                else:
                    print("Insufficient Balance! Transaction cancelled.")
                    new_lines.append(line)
            else:
                new_lines.append(line)

        if found:
            writer = open("Account_holders.txt", "w")
            writer.writelines(new_lines)
            writer.close()
        else:
            print("Account Number Not Found.")

    elif opt == 5:
        print("\n--- Check Balance ---")
        acc_no = input("Enter Your Account Number: ").strip()

        if not os.path.exists("Account_holders.txt"):
            print("No accounts found.")
            continue

        file_acc = open("Account_holders.txt", "r")
        lines = file_acc.readlines()
        file_acc.close()

        found = False
        for line in lines:
            parts = line.split()
            if len(parts) >= 4 and parts[3] == acc_no:
                found = True
                print(f"Account Holder: {parts[0]}")
                print(f"Current Balance: {parts[2]}")
                break
        
        if not found:
            print("Account Number Not Found.")

    elif opt == 6:
        print("Thank you for banking with The Bank of Krishna. Goodbye!")
        run = False
