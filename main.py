a = float(input("Gimme 'a'"))
b = float(input("Gimme 'b'"))
c = float(input("Gimme 'c'"))
delta = b * b - 4.0 * a * c
print("Delta: " + str(delta))
elementDelta = delta ** 0.5
print("Element of delta: " + str(elementDelta))
if delta > 0:
    xi = ((-b - elementDelta) / 2 * a)
    xii = ((-b + elementDelta) / 2 * a)
    print("Solution I = " + str(xi) + "\nSolution II = " + str(xii))
elif delta == 0:
    xo = -b / (2 * a)
    print("Because Delta = 0, u have only one solution = " + str(xo))
else:
    print("You don't have real solutions.")