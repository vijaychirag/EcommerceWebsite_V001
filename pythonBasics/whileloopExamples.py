# while loop : basically while loop is a condition, if the condition is true loop will continue untill given
# condition becomes false

'''it = 5
while it > 1:
    if it != 3:
        print(it)
    it = it - 1'''
print("while loop execution is done")

it1 = 12
while it1 > 1:
    if it1 == 9:
        it1 = it1 - 1
        continue
    if it1 == 4:
        break
    print(it1)
    it1 = it1 - 1

print("in while loop, break method execution is done")
