print("Example of break:")
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print(i)

print("\nExample of continue:")
for i in range(5):
    if i == 3:
        print("Skipping i =", i)
        continue
    print(i)

print("\nExample of pass:")
for i in range(3):
    if i == 1:
        pass  # no action
    print(i)
