from ai import AI

jarvis = AI()

command = ""

while True and command != "goodbye":
    command = jarvis.listen()
    print("Command was:", command)

    if command in ["hello", "hi"]:
        print("Hello sir")