name = input("Whom should I sign this to: ")
save = input("Where shall I save it: ")

with open(save, "w") as f:
    f.write("Hi " + name + ", we hope you enjoy learning Python with us! Best, Mooc.fi Team")