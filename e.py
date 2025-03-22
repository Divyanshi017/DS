# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
exp_mon=["january","february","march","april","may"]
exp=[2340,2500,2100,3100,2980]
e=int(input("Enter the expenses"))
m=-1
for i in range (len(exp)):
    if e==exp[i]:
        m=i
        break
if m!=-1:
    print(f'expense {e} is spent in {exp_mon[m]}')
else:
    print("not found")