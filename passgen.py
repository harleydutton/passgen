import random
import argparse

parser = argparse.ArgumentParser(description='Generate a password of given length.')

parser.add_argument('length',metavar='len',type=int,
        help='the length of the password')

parser.add_argument('-cap', dest='cap', action='store_const', const=True,
        default=False, help='Add caps to the password')

parser.add_argument('-sym', dest='sym', action='store_const', const=True, 
        default=False, help='Add caps to the password')

args = parser.parse_args()

out=""
legalChars="1234567890abcdefghijklmnopqrstuvwxyz"

capitals="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if args.cap:
    legalChars+=capitals

symbols="~!@#$%^&*()_+`-={}|[]<>?,.;:'\"\\/"
if args.sym:
    legalChars+=symbols

for i in range(args.length):
        out+=random.choice(legalChars)
print(out)

