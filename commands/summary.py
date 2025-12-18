import datetime
import calendar
def summaryExpense(expense_list, month=None):
    sum = 0
    if month is None:
        for x in expense_list:
            sum += x.get("Amount")
        print(f"Sum of all expenses is: ${sum}")
    else:
        slc_month = month
        for x in expense_list:
            m_exp = x.get("Added at")
            m_exp = datetime.datetime.fromisoformat(m_exp)
            if m_exp.month == slc_month:
                sum += x.get("Amount")
        print(f"Total expenses for {calendar.month_name[slc_month]}: ${sum}")
    return