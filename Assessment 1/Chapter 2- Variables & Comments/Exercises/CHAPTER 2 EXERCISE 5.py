# the cost of usb sticks and budget 
usb_stick_cost = 6
total_budget = 50

# calculate how many usb sticks she can buy
num_usb_sticks = total_budget // usb_stick_cost

# calculate money left 
remaining_budget = total_budget % usb_stick_cost

# Print the results
print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have ${remaining_budget} left.")
