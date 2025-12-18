import datetime
def deleteExpenses(expense_list, id=None, month=None, clear=False):
    if clear is True and id is None and month is None:
        expense_list.clear()
    elif clear is False:
        if month is not None and id is None:
            slc_month = month
            for x in expense_list:
                m_exp = x.get("Added at")
                m_exp = datetime.datetime.fromisoformat(m_exp)
                if m_exp.month == slc_month:
                   expense_list.remove(x)
        if id is not None and month is None:
             slc_id = id
        for x in expense_list:
            if x.get("ID") == slc_id:
                expense_list.remove(x)
    return