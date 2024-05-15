import basic
import sys

running = True

if len(sys.argv) == 2:
    try:
        filename = sys.argv[1]
        if not filename.endswith(".fedxd"):
            print("Unsoported File Error: File must be a .fedx file")
        
        with open(filename, "r") as file:
            script = file.read()
            str(script)
        fn = filename.split("/")[-1] or filename.split("\\")[-1]
        fn = fn.split(".")[0]

        values = basic.run(fn, script)

        error = values[1]

        if error:
            print(error.as_string())
        running = False
    except FileNotFoundError:
        print("FileNotFoundError: File not found")
        running = False 
    except Exception as e:
        print("Error: ", e)
        running = False        
else:
    print("FedxD Programming Language")
    print("Version 1.0.0")
    print("Type 'exit' to exit")
    print("")

while running:
    try:
        text = input("FedxD > ")

        if text.strip() == "":
            continue
        if text == "exit":
            running = False
            print("\nGoodbye!")
            break

        values = basic.run("<stdin>", text)

        error = values[1] 
        result = values[0]

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt\nType 'exit' to exit")
    except Exception as e:
        print(e)
        print("Error: ", e)
        running = False
        break
