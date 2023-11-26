import argparse

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

def main():
    parser = argparse.ArgumentParser(description='Greet someone with name and age. ex) > python3 simple_arguments.py (name) (age)')
    parser.add_argument('name', type=str, help='Name of the person')
    parser.add_argument('age', type=int, help='Age of the person')

    args = parser.parse_args()
    greet(args.name, args.age)

if __name__ == "__main__":
    main()

# > python3 simple_arguments.py Alice 30
# Hello, Alice! You are 30 years old.