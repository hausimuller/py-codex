# guard.py

import rand

def main():
    print("Welcome to ChatGPT Codex")
    a: int = -10
    b: int = 30
    my_ran_ints: list = rand.generate_random_integers(a, b)
    print(my_ran_ints)

if __name__ == "__main__":
    main()
