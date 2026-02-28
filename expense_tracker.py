
<<<<<<< HEAD
=======
from expense import Expense


def main():
    print("Running the expense tracker application...")
    expense_file_path="expenses.txt"
    budget = 2000
    # Get user input for expense
    expense=get_user_expense()
    
    

    # write their expense to a file
#     save_expense_to_file(expense, expense_file_path)    
    


    # read the file and display the expenses
    summarize_expenses(expense_file_path,budget)
    

def get_user_expense():
    print('Getting expense...')
    expense_name = input('Enter expense name: ')
    expense_amount = float(input('Enter expense amount: '))

    
    expense_categories = ["Food","Work","Fun","Misc"]

    while True:
         print('Select expense category: ')
         for i,category_name in enumerate(expense_categories):
              print(f'  {i+1}.  {category_name}')
         value_range=f"[1-{len(expense_categories)}]" 

         selected_index=int(input(f"Enter a category number {value_range}: ")) - 1
         if selected_index in range(len(expense_categories)):
              selected_category=expense_categories[selected_index]
              new_expense = Expense(name=expense_name,category=selected_category,amount=expense_amount)
              
              return new_expense
         else:
              print("Invalid category. Try again.")





         

def save_expense_to_file(expense,expense_file_path):
     print(f'Saving expenses: {expense}')
     with open(expense_file_path,"a") as file:
          file.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path, budget):
     print(f'Summerising expenses: ')
     expense : list[Expense] = []
     with open(expense_file_path,"r") as file:
          
          lines = file.readlines()
          for line in lines:
               
               expense_name, expense_category, expense_amount = line.strip().split(",")
               print(expense_name, expense_category, expense_amount)
               line_expense = Expense(
                    name= expense_name, amount=float(expense_amount), category=expense_category
               )
              
               expense.append(line_expense)
               
     amount_by_category = {}
     for expense in expense:
          key = expense.category 
          if key in amount_by_category:
               amount_by_category[key] += expense.amount
          else:
               amount_by_category[key] = expense.amount
     print("Expense summary by category:")
     for key, amount in amount_by_category.items():
          print(f"{key}: ksh{amount:.2f}")
     
     total_spent =sum([expense.amount for expense in expense])
     print(f"Total spent: ksh{total_spent:.2f}")
     remaining_budget = budget - total_spent
     print(f"Remaining budget: ksh{remaining_budget:.2f}") 
>>>>>>> 923ee62 (second Commit)
if __name__ == "__main__":
     main()