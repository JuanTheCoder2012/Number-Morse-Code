print("Welcome, enter your morse code now from 0 - 9: ")
print("Make sure to input in this format X, X, X, X, X,\n")


def convert_to_morse(code):
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")
    return code

lock_code = input()


print(f"\nInitial code: {lock_code}")

morse = convert_to_morse(lock_code)
print(f"\nMorse code: {morse}")

