# Opens a file and prints its content
def main():
    file = open("hello_world.py", "r")
    text = file.read()
    print(text)
main()