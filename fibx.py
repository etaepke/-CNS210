#!/user/bin/python3
import argparse
import os.path

def fib(n, filename):
    if os.path.isfile(filename):
        raise ValueError("File already exists")
    try:
        file=open(filename, "w")
        a, b = 0, 1
        for i in range(n):
                a, b = b, a+b
                print(a)
                file.write("\n"+str(a))
        file.close()
        return a
    except IOError:
        print("Error Permission Not Granted")
def  Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("list", help="The Fibonacci Number " + \
                        "you wish to calculate.", type=int)
    parser.add_argument("-o", nargs="+", metavar='filename', help="Output the " + \
                        "result to a file", type=str)
    args = parser.parse_args()
    print(args)
    result = fib(args.list, args.o[0])
    print("The " +str(args.list)+"the fib number "+str(result))

    if args.output:
           f = open("fibnum.txt", "a")
           f.write(str(results) +"/n")

if __name__ == '__main__':
    Main()