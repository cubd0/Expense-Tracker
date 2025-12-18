import commands.addexpense
import commands.listexpenses
import commands.delete_expense
import commands.summary
import argparse
import json
import os

file = "allexpenses.json"
try:
     with open(file, "r") as f:
        all_expenses = json.load(f)
except FileNotFoundError:
    all_expenses = []

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command", required=True, title="commands")

add_parser = subparsers.add_parser("add",  help="Add an expense")
add_parser.add_argument("amount", type=int, help=("Amount spent"))
add_parser.add_argument("description", type=str, help=("Description of the expense"))

list_parser = subparsers.add_parser("list", help=("List or sort expenses"))
list_parser.add_argument("-i", "--id", type=int, help="Search expenses by ID")
list_parser.add_argument("-m", "--month", type=int,choices=range(1, 13), help="Search expenses by month")

summary_parser = subparsers.add_parser("summary", help="Get summary of all expenses or a month of expenses")
summary_parser.add_argument("-m", "--month", type=int, choices=range(1, 13), help="Summarize expenses by month")

delete_parser = subparsers.add_parser("delete", help="Delete expenses")
delete_parser.add_argument("--clear", action="store_true", help="Clear all expenses")
delete_parser.add_argument("-m", "--month", type=int, choices=range(1, 13), help="Delete a month of expenses")
delete_parser.add_argument("-i", "--id", type=int, help="Delete a transaccion by ID")

args = parser.parse_args()

if args.command == "add":
    expense = commands.addexpense.addExpense(args.amount, args.description, all_expenses)
    with open(file, "w") as f:
        json.dump(all_expenses, f, indent=2)
if args.command == "list":
    if args.month is not None and args.id is not None:
        pass
    else:
        commands.listexpenses.listExpenses(all_expenses, args.id, args.month)
if args.command == "summary":
    commands.summary.summaryExpense(all_expenses, args.month)
if args.command == "delete":
    commands.delete_expense.deleteExpenses(all_expenses, args.id, args.month, args.clear)
    if all_expenses == []:
        os.remove("allexpenses.json")