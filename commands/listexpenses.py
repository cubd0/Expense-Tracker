import datetime
def listExpenses(expense_list, id=None, month=None):
    print("ID\tDate\tDescription\tAmount")
    if id is None and month is None:
        for e in expense_list:
            print(f"{e.get('ID')}\t{e.get('Added at')}\t{e.get('Description')}\t{e.get('Amount')}")
    if id is not None:
        slc_id = id
        for x in expense_list:
            if x.get("ID") == slc_id:
                slc_expense = expense_list[x]
        print(f"{slc_expense.get('ID')}\t{slc_expense.get('Added at')}\t{slc_expense.get('Description')}\t{slc_expense.get('Amount')}")
    if month is not None:
        slc_month = month
        m_list = []
        for x in expense_list:
            m_exp = x.get("Added at")
            m_exp = datetime.fromisoformat(m_exp)
            if m_exp.month == slc_month:
                m_list.append(x)
        m_list.sort(key= lambda x: datetime.fromisoformat(x.get("Added at")))
        for e in m_list:
            print(f"{e.get('ID')}\t{e.get('Added at')}\t{e.get('Description')}\t{e.get('Amount')}")
    return