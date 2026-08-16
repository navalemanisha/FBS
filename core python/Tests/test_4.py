area = float(input("Enter area of one wall: "))

interior_cost = float(input("Enter cost of interior wall per sq. unit: "))
exterior_cost = float(input("Enter cost of exterior wall per sq. unit: "))

# According to the given diagram
total_interior = area * 2
total_exterior = area * 8

cost_interior = total_interior * interior_cost
cost_exterior = total_exterior * exterior_cost

total_cost = cost_interior + cost_exterior

print("Interior painting cost =", cost_interior)
print("Exterior painting cost =", cost_exterior)
print("Total painting cost =", total_cost)