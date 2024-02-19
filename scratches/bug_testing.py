operation_list = ["-", "+", "x", "/", "^"]
operation_sign_in_screen = True
visor = {"text":"5+"}

x = visor["text"]
y = x[-1::]
if operation_sign_in_screen and y in operation_list:
    visor["text"] = visor["text"][:-1:]
    print(visor["text"])