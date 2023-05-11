'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

for num in range(1, 26):

    if num % 3 == 0 and num % 5 == 0:

        print("FizzBuzz")

    elif num % 3 == 0:

        print("Fizz")

    elif num % 5 == 0:

        print("Buzz")

    else:

        print(num)
