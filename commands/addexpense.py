import datetime
def addExpense(amount, description, expense_list):
    if amount <= 0:
        print("Amount mut be greater than 0")
        return
    if description == None:
        print("Description cannot be empty")
        return
    # reminder to add date later
    expense = {
    "ID" : len(expense_list) + 1,
    "Added at" : datetime.date.today().isoformat(),
    "Description" : description,
    "Amount" : amount
      }
    expense_list.append(expense)
    return