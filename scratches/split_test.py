signs = ["-", "+", "x", "/", "^"]
test = "23^4"

for i in signs:
    if len(test.split(i)) >= 2:
        print(test.split(i))

# lststr = "2.2 + 34 - 43 x 67.23 ^ 3 / 3.5"
lststr = "2 ^ 3"
lst = lststr.split(" ")
fstr = ""
for i in lst:
    if i == "x":
        fstr += "*"
    elif i == "^":
        fstr += "**"
    else:
        fstr += i

print(fstr)
print(eval(fstr))
