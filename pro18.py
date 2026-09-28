bill=float(input("Enter total bill amount:  "))

tip_percent=int(input("Enter Tip percent "  ))

tip=bill*(tip_percent/100)

total=bill+tip

print(f"Tip Amount: {tip:.2f}")
print(f"Total Bill(with tip): {total:.2f}")