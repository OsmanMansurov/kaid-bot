import ast

handle = open("data.txt", "r")
dictionary = {}

for i in handle:
    i = i.rstrip()
    vals = i.split(" = ")
    dictionary[vals[0]] = ast.literal_eval(vals[1])

def main():
    print(dictionary)

if __name__ == "__main__":
    main()
