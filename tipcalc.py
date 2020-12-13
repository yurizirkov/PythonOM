bill = float(input("How much was your bill?")) 

#if replace('$',''):
#	pass
#bill.replace("$","")
#if "," in bill: bill = bill.replace(",",".")

print("Your bill was", f"${bill}")

tip = float(input("What percentage do you want to tip?"))

print("You want to tip", f"{tip}%")

total_tip = bill * (tip / 100)

tip_amount = total_tip + bill

print("Your bill is now", f"${tip_amount}")

print("You tipped", f"${total_tip}")
