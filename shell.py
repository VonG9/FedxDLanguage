import basic
import sys

running = True

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not filename.endswith(".fedxd"):
        print("Unsoported File Error: File must be a .fedx file")
    with open(filename, "r") as file:
        script = file.read()
        str(script)
    fn = filename.split("/")[-1] or filename.split("\\")[-1]
    fn = fn.split(".")[0]

    result, error = basic.run(fn, script)

    if error:
        print(error.as_string())
    running = False
        
else:
    print("FedxD Programming Language")
    print("Version 1.0.0")
    print("Type 'exit' to exit")
    print("")

while running:
    text = input("FedxD > ")

    if text.strip() == "":
        continue
    if text == "exit":
        running = False

    result, error = basic.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
