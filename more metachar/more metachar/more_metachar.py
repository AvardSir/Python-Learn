
import re
def snezinka():
    pattern = r"yellow(-green)*"#zero or more

    if re.match(pattern, "yellow"):
        print("snezinka yellow")

    if re.match(pattern, "yellow-green"):
        print("snezinka yellow-green")

    if re.match(pattern, "green"):
        print("snezinka green")
def plus():
    pattern = r"yellow(-green)+"#one or more

    if re.match(pattern, "yellow"):
        print("plus yellow")

    if re.match(pattern, "yellow-green"):
        print("plus yellow-green")

    if re.match(pattern, "yellow-green-green-green"):
        print("plus yellow-green-green-green")
def question():
    pattern = r"yellow(-green)?-yellow"#one Or zero (and only)

    if re.match(pattern, "yellow-yellow"):
        print("question yellow-yellow")

    if re.match(pattern, "yellow-green-yellow"):
        print("question yellow-green-yellow")

    if not re.match(pattern, "yellow-green-green-green-yellow"):
        print("question NOT yellow-green-green-green-yellow")

question()
#plus    ()
#snezinka()