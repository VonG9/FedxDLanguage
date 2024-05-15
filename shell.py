import basic
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not filename.endswith(".fedx"):
        print("Unsoported File Error: File must be a .fedx file")
    with open(filename, "r") as file:
        script = file.read()
        script.strip("`")
        str(script)
    result, error = basic.run(sys.argv[1], script)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))

    exit()

while True:
    text = input("FedxD > ")

    if text.strip() == "":
        continue
    if text == "exit":
        break

    result, error = basic.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
