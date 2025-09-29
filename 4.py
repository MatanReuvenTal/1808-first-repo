my_file = open("name.txt", "a")
def save_name():
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
    my_file.close()
def show_name(file_name):
    open(file_name, "r").close()
    my_file = open(file_name, "r")
    for name in my_file:
        print (name, end="")
    my_file.close()
show_name("name.txt")