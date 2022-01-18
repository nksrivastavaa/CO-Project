import sys
import matplotlib
from matplotlib import pyplot as plt
complete_input = sys.stdin.read()
input1 = []
f = (complete_input.split("\n"))

for i in range(len(f)):
    input1.append(f[i] + "\n")

input2 = []
for line in input1:
    lineInput = line.split()
    if lineInput != []:
        input2.append(lineInput)
memory = ['0000000000000000'] * 256
for i in range(len(input2)):
    memory[i] = input2[i][0]


Reg = {
    "000": ["R0", 0],
    "001": ["R1", 0],
    "010": ["R2", 0],
    "011": ["R3", 0],
    "100": ["R4", 0],
    "101": ["R5", 0],
    "110": ["R6", 0],
    "111": ["FLAGS", [0, 0, 0, 0]]
}

opcode = {
    "00000": ("add", "A"),
    "00001": ("sub", "A"),
    "00110": ("mul", "A"),
    "01010": ("xor", "A"),
    "01011": ("or", "A"),
    "01100": ("and", "A"),
    "00010": ("mov_imm", "B"),
    "01000": ("rs", "B"),
    "01001": ("ls", "B"),
    "00011": ("mov_reg", "C"),
    "00111": ("div", "C"),
    "01101": ("not", "C"),
    "01110": ("cmp", "C"),
    "00100": ("ld", "D"),
    "00101": ("st", "D"),
    "01111": ("jmp", "E"),
    "10000": ("jlt", "E"),
    "10001": ("jgt", "E"),
    "10010": ("je", "E"),
    "10011": ("hlt", "F"),
}


def flagreset():
    Reg['111'][1][0] = 0
    Reg['111'][1][1] = 0
    Reg['111'][1][2] = 0
    Reg['111'][1][3] = 0


# type a
def add(a, b, c):  # where a,b,c are the opcodes of the registers(strings)
    flagreset()
    Reg[a][1] = Reg[b][1] + Reg[c][1]
    if Reg[a][1] > 255:
        Reg["111"][1][0] = 1


def sub(a, b, c):
    flagreset()
    Reg[a][1] = Reg[b][1] - Reg[c][1]
    if Reg[c][1] > Reg[b][1]:
        Reg[a][1] = 0
        Reg["111"][1][0] = 1


def mul(a, b, c):
    flagreset()
    Reg[a][1] = Reg[b][1] * Reg[c][1]
    if Reg[a][1] > 255:
        Reg["111"][1][0] = 1


def And(a, b, c):
    flagreset()
    Reg[a][1] = Reg[b][1] & Reg[c][1]


def Or(a, b, c):
    flagreset()
    Reg[a][1] = Reg[b][1] | Reg[c][1]


def xor(a, b, c):
    flagreset()
    Reg[a][1] = Reg[b][1] ^ Reg[c][1]


# type b
def movi(a, b):  # where a is reg and b is immediate value in strings
    flagreset()
    Reg[a][1] = int(b, 2)



def rs(a, b):
    flagreset()
    x = int(b, 2)

    Reg[a][1] = Reg[a][1] // (2 ** x)


def ls(a, b):
    flagreset()
    x = int(b, 2)
    Reg[a][1] = Reg[a][1] * (2 ** x)



# type c


def movr(a, b):  # a and b are regs in strings
    if b == "111":
        Reg[a][1] = Reg[b][1][0] * 8 + Reg[b][1][1] * 4 + Reg[b][1][2] * 2 + Reg[b][1][3] * 1
    flagreset()
    if b != "111":
        Reg[a][1] = Reg[b][1]


def divide(a, b):
    flagreset()
    Reg["000"][1] = Reg[a][1] // Reg[b][1]
    Reg["001"][1] = Reg[a][1] % Reg[b][1]


def invert(a, b):
    flagreset()
    x = bin(Reg[b][1])[2:]
    y = len(x)
    z = "0" * (16 - y) + x
    p = ""
    for i in range(len(z)):
        if z[i] == "0":
            p = p + "1"
        elif z[i] == "1":
            p = p + "0"
    Reg[a][1] = int(p, 2)



def cmp(a, b):
    flagreset()
    if Reg[a][1] > Reg[b][1]:
        Reg["111"][1][2] = 1
    elif Reg[a][1] < Reg[b][1]:
        Reg["111"][1][1] = 1
    elif Reg[a][1] == Reg[b][1]:
        Reg["111"][1][3] = 1


# type d


def ld(a, b):  # a is reg and b is mem_addr in strings
    flagreset()
    dec_mem = int(b, 2)
    Reg[a][1] = int(memory[dec_mem], 2)


def st(a, b):
    flagreset()
    dec_mem = int(b, 2)
    t = bin(Reg[a][1])
    y = t[2:]
    l = len(y)
    memory[dec_mem] = (16 - l) * '0' + y


def regtosixteenbitbin():# format(REg, "08b")
    #return "0" * 8 + format(Reg['000'][1], "08b") + " " + "0" * 8 + format(Reg['001'][1], "08b") + " " + "0" * 8 + format(Reg['010'][1], "08b") + " " + "0" * 8 + format(Reg['011'][1], "08b") + " " + "0" * 8 + format(Reg['100'][1], "08b") + " " + "0" * 8 + format(Reg['101'][1], "08b") + " " + "0" * 8 + format(Reg['110'][1], "08b") + " " + 12 * '0' + str(Reg['111'][1][0]) + str(Reg['111'][1][1]) + str(Reg['111'][1][2]) + str(Reg['111'][1][3])

     return (16 - len(bin(Reg['000'][1])[2:])) * '0' + bin(Reg['000'][1])[2:][len(bin(Reg['000'][1])[2:]) - 16:] + " " + (
                  16 - len(bin(Reg['001'][1])[2:])) * '0' + bin(Reg['001'][1])[2:][len(bin(Reg['001'][1])[2:]) - 16:] + " " + (
                         16 - len(bin(Reg['010'][1])[2:])) * '0' + bin(Reg['010'][1])[2:][len(bin(Reg['010'][1])[2:]) - 16:] + " " + (
                         16 - len(bin(Reg['011'][1])[2:])) * '0' + bin(Reg['011'][1])[2:][len(bin(Reg['011'][1])[2:]) - 16:] + " " + (
                         16 - len(bin(Reg['100'][1])[2:])) * '0' + bin(Reg['100'][1])[2:][len(bin(Reg['100'][1])[2:]) - 16:] + " " + (
                         16 - len(bin(Reg['101'][1])[2:])) * '0' + bin(Reg['101'][1])[2:][len(bin(Reg['101'][1])[2:]) - 16:] + " " + (
                         16 - len(bin(Reg['110'][1])[2:])) * '0' + bin(Reg['110'][1])[2:][len(bin(Reg['110'][1])[2:]) - 16:] + " " + (
                         12 * '0' + str(Reg['111'][1][0]) + str(Reg['111'][1][1]) + str(Reg['111'][1][2]) + str(
                     Reg['111'][1][3]))


def perform(instruct):
    global PC
    global halt
    if instruct[0:5] == '00000':
        add(instruct[7:10], instruct[10:13], instruct[13:])
    elif instruct[0:5] == '00001':
        sub(instruct[7:10], instruct[10:13], instruct[13:])
    elif instruct[0:5] == '00110':
        mul(instruct[7:10], instruct[10:13], instruct[13:])
    elif instruct[0:5] == '01010':
        xor(instruct[7:10], instruct[10:13], instruct[13:])
    elif instruct[0:5] == '01011':
        Or(instruct[7:10], instruct[10:13], instruct[13:])
    elif instruct[0:5] == '01100':
        And(instruct[7:10], instruct[10:13], instruct[13:])
    elif instruct[0:5] == '00010':
        movi(instruct[5:8], instruct[8:])
    elif instruct[0:5] == '01000':
        rs(instruct[5:8], instruct[8:])
    elif instruct[0:5] == '01001':
        ls(instruct[5:8], instruct[8:])
    elif instruct[0:5] == '00011':
        movr(instruct[10:13], instruct[13:])
    elif instruct[0:5] == '00111':
        divide(instruct[10:13], instruct[13:])
    elif instruct[0:5] == '01101':
        invert(instruct[10:13], instruct[13:])
    elif instruct[0:5] == '01110':
        cmp(instruct[10:13], instruct[13:])
    elif instruct[0:5] == '00100':
        ld(instruct[5:8], instruct[8:])
    elif instruct[0:5] == '00101':
        st(instruct[5:8], instruct[8:])
    elif instruct[0:5] == '01111':
        flagreset()
        decimal_mem = int(instruct[8:], 2)

        PC = decimal_mem - 1

    elif instruct[0:5] == '10000':

        if Reg['111'][1][1] == 1:
            decimal_mem = int(instruct[8:], 2)
            PC = decimal_mem - 1
        flagreset()

    elif instruct[0:5] == '10001':

        if Reg['111'][1][2] == 1:
            decimal_mem = int(instruct[8:], 2)
            PC = decimal_mem - 1
        flagreset()

    elif instruct[0:5] == '10010':

        if Reg['111'][1][3]:
            decimal_mem = int(instruct[8:], 2)
            PC = decimal_mem - 1
        flagreset()

    elif instruct[0:5] == '10011':
        halt = True


PC = 0
halt = False
list1 = []
while halt == False:
    instruct = memory[PC]
    perform(instruct)
    a = bin(PC)
    b = a[2:]
    l = len(b)
    print((8 - l) * '0' + b, end=" ")
    print(regtosixteenbitbin())
    list1.append(PC)
    PC += 1


for i in memory:
    print(i)
# q3
x = range(1, len(list1)+1)
plt.scatter(x, list1)
plt.show()
