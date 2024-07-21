def recognize_language (msg):
    if msg is None:
        print("Not message was given.")
    elif msg == "hei" or msg == "moi":
        print("Language is finnish.")
    elif msg == "hello" or msg == "hi":
        print("Language is english.")   
    else:
        print("Language not recognized.")

def main_program():
    recognize_language("hello")
    recognize_language("hei")
    recognize_language("tjäna!")

main_program()
