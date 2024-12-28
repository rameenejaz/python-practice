wii_cost=300
amount=float(input("Enter the amount of money you have:"))
no_of_wii=int(amount/wii_cost)
remaining_amount=(amount%wii_cost)
money_needed_for_one_more_wii=float(wii_cost-remaining_amount)
print(f"You can afford {no_of_wii} wiis")
print(f" remaining money: ${remaining_amount}")
print(f"Money needed for one more wii: ${money_needed_for_one_more_wii:.2f}")