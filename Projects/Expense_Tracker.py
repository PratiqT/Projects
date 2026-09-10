
expenses = []
#Total expense calculate and print
def total_expense():
    amount = 0
    for expense in expenses:
        amount += expense["amount"]
        print(amount)           
def add_expense():
    global expenses

    category = input("Category: ")
    try:
        amount = int(input("Amount: "))
    except ValueError:
        print("Invalid amount")
        return
    description = input("Description: ")

    entry = {
        "category": category,
        "amount": amount,
        "description": description,
    }
    expenses.append(entry)
    print("expense added successfully\n")
def daily():
    dtravel = int(input("how much did you spend on TRAVEL today? "))
    dfood = int(input("how much did you spend on FOOD today? "))
    dtotal = dtravel + dfood 
    print("Total Expense Today:",dtotal)
    offby = dtotal - 100
    if offby == 0:
        print("you just survived today")
    if dtotal > 100:
        dleft = int(input("how much you have left this month? "))
        print(f"Warning: You are spending a lot!, if you keep spending you will last: {dleft/dtotal: .0f} days") 
    else:
        print("you are safe")
def monthly():
    mtravel = int(input("how much did you spend on TRAVEL this month? "))
    mfood = int(input("how much did you spend on FOOD this month? "))
    mextra = int(input("how much did you on extra's this month? "))
    mtotal = mtravel + mfood + mextra
    print("Total Expense This Month:",mtotal)
    if mtotal > 5000:
         print("Warning: You are spending a lot!")
    else:
        print("you are safe")  
def main():
    try:

        while True:

            print("1.Add Expense")
            print("2.Show totalExpense")
            what = input("> ")

            if what.startswith("1"):
                add_expense()
            elif what.startswith("2"):
                total_expense()
    except KeyboardInterrupt:
        print("Thanks for using!")

if __name__ == "__main__":
    main()




        



    




