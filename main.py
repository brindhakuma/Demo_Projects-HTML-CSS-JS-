expenses = []
expense1 = {'amount': '51.00', 'category': 'dress'}
expenses.append(expense1)
expense2 = {'amount': '25.50', 'category': 'groceries'}
expenses.append(expense2)

def removeExpense():
    while True:
        listExpenses()
        print("what expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except:
            print("invalid")


def addExpense(amount,category):
    expense = {'amount':amount,'category':category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options...")
    print("1. add an expense")
    print("2. remove an expense")
    print("3. list all expense")

def listExpenses():
    print("\nhere list of your expense...")
    
    counter = 0
    for expense in expenses:
        print("#", counter, " - ",expense['amount'], " - ", expense['category'])
        counter += 1
    expenses.append(expense)
        



if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if (optionSelected == "1"):
            print("how much was this expense")
            while True:
                try:
                    amountToAdd = input("> ")
                    break
                except:
                    print("invalid")

            print("what category was this expense")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                    print("invalid")
              
                addExpense(amountToAdd,category)
        elif (optionSelected == '2'):
            removeExpense()
        elif (optionSelected == '3'):
            listExpenses()
        else:
            print("invalid")
                  



















