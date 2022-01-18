import sys
complete_input = sys.stdin.read()
input1 = []
f=(complete_input.split("\n"))

for i in range(len(f)):
    input1.append(f[i] + "\n")


input2 = []  # line by line without spaces inputs # final input
input3 = []
input4 = []               # for error generation
for i in input1:
    if i != "\n" and i != "hlt":
        input4.append(i[:-1])
    elif i == "hlt":
        input4.append("hlt")
    else:
        input4.append("\n")

count3 = 1
for line in input1:
    lineInput = line.split()
    if lineInput != []:
        lineInput.append(count3)
        input2.append(lineInput)
    count3 += 1
for line in input2:
    if line[0] == "var":
        input2.remove(line)
        input3.append(line)
input2.extend(input3)
for i in range(len(input2)):
    input2[i].append(i)  # final input2 with line numbers as mem_address
finalOutput = []

count5 = 0
var_declared_at_line = []

for i in range(len(input1)):
    if input1[i][0: 3] == "var":
        var_declared_at_line.append(i + 1)
        count5 += 1
for i in range(count5):
    if input1[i][0: 3] != "var":
        z = "variable not declared at the beginning and declared at line number "
        z = z + str(var_declared_at_line[-1])
        finalOutput.append(z)
        break
varNameList = []
for i in range(len(input2)):
    if input2[i][0] == "var":
        varNameList.append(input2[i][1])

for i in range(len(varNameList)):
    if type(varNameList[i]) != int:
        if varNameList[i].isnumeric():
            finalOutput.append("illegal variable name")

if len(varNameList) > 1:
    for i in range(len(varNameList)):
        for j in range(i + 1, len(varNameList)):
            if varNameList[i] == varNameList[j]:
                finalOutput.append("variable redeclared")

opcode_names = ["add", "sub", "mul", "xor", "or", "and", "mov", "rs", "ls",
                "div", "not", "cmp", "ld", "st", "jmp", "jlt", "jgt", "je", "hlt", "var"]

labelName = []

non_flag_reg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

opcode = {
    "add": ("00000", "A"),
    "sub": ("00001", "A"),
    "mul": ("00110", "A"),
    "xor": ("01010", "A"),
    "or": ("01011", "A"),
    "and": ("01100", "A"),
    "mov_imm": ("00010", "B"),
    "rs": ("01000", "B"),
    "ls": ("01001", "B"),
    "mov_reg": ("00011", "C"),
    "div": ("00111", "C"),
    "not": ("01101", "C"),
    "cmp": ("01110", "C"),
    "ld": ("00100", "D"),
    "st": ("00101", "D"),
    "jmp": ("01111", "E"),
    "jlt": ("10000", "E"),
    "jgt": ("10001", "E"),
    "je": ("10010", "E"),
    "hlt": ("10011", "F"),
}

reg = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111"
}

def add(reg1, reg2, reg3):  # type A
    a = opcode["add"][0]
    b = "00"
    c = reg[reg1]
    d = reg[reg2]
    e = reg[reg3]
    output = a + b + c + d + e
    return output


def sub(reg1, reg2, reg3):
    a = opcode["sub"][0]
    b = "00"
    c = reg[reg1]
    d = reg[reg2]
    e = reg[reg3]
    output = a + b + c + d + e
    return output


def movei(reg1, imm):  # imm passed as string
    a = opcode["mov_imm"][0]
    b = reg[reg1]
    c = bin(int(imm))[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def mover(reg1, reg2):  # type c
    a = opcode["mov_reg"][0]
    b = "00000"
    c = reg[reg1]
    d = reg[reg2]
    output = a + b + c + d
    return output


def load(reg1, mem_addr):  # mem_addr is passed as a string int
    a = opcode["ld"][0]
    b = reg[reg1]
    c = bin(mem_addr)[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def store(reg1, mem_addr):  # mem_addr is passed as decimal int
    a = opcode["st"][0]
    b = reg[reg1]
    c = bin(mem_addr)[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def mul(reg1, reg2, reg3):
    a = opcode["mul"][0]
    b = "00"
    c = reg[reg1]
    d = reg[reg2]
    e = reg[reg3]
    output = a + b + c + d + e
    return output


def div(reg3, reg4):
    a = opcode["div"][0]
    b = "00000"
    c = reg[reg3]
    d = reg[reg4]
    output = a + b + c + d
    return output


def rs(reg1, imm):
    a = opcode["rs"][0]
    b = reg[reg1]
    c = bin(int(imm))[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def ls(reg1, imm):
    a = opcode["ls"][0]
    b = reg[reg1]
    c = bin(int(imm))[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def xor(reg1, reg2, reg3):
    a = opcode["xor"][0]
    b = "00"
    c = reg[reg1]
    d = reg[reg2]
    e = reg[reg3]
    output = a + b + c + d + e
    return output


def Or(reg1, reg2, reg3):
    a = opcode["or"][0]
    b = "00"
    c = reg[reg1]
    d = reg[reg2]
    e = reg[reg3]
    output = a + b + c + d + e
    return output


def And(reg1, reg2, reg3):
    a = opcode["and"][0]
    b = "00"
    c = reg[reg1]
    d = reg[reg2]
    e = reg[reg3]
    output = a + b + c + d + e
    return output


def Invert(reg1, reg2):
    a = opcode["not"][0]
    b = "00000"
    c = reg[reg1]
    d = reg[reg2]
    output = a + b + c + d
    return output


def Compare(reg1, reg2):
    a = opcode["cmp"][0]
    b = "00000"
    c = reg[reg1]
    d = reg[reg2]
    output = a + b + c + d
    return output


def jump(mem_addr):  # type E
    a = opcode["jmp"][0]
    b = "000"
    c = bin(mem_addr)[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def jlt(mem_addr):
    a = opcode["jlt"][0]
    b = "000"
    c = bin(mem_addr)[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def jgt(mem_addr):
    a = opcode["jgt"][0]
    b = "000"
    c = bin(mem_addr)[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def je(mem_addr):
    a = opcode["je"][0]
    b = "000"
    c = bin(mem_addr)[2:]
    n = len(c)
    l = 8 - n
    d = "0" * l
    output = a + b + d + c
    return output


def halt():  # type F
    a = opcode["hlt"][0]
    b = "00000000000"
    output = a + b
    return output


labelInstructionName = []
for i in range(len(input2)):
    if input2[i][0][-1] == ":":
        temp = input2[i]
        labelInstructionName.append(temp)


for i in range(len(input2)):
    if input2[i][0] in opcode_names:
        if input2[i][0] == "add":
            count = 0
            for j in range(1, 4):
                if input2[i][j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(add(input2[i][1], input2[i][2], input2[i][3]))
        if input2[i][0] == "sub":
            count = 0
            for j in range(1, 4):
                if input2[i][j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(sub(input2[i][1], input2[i][2], input2[i][3]))
        if input2[i][0] == "mov":
            temp = input2[i][2]
            if temp[0] == "$":
                temp2 = temp[1:]
                if input2[i][1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                else:
                    if 0 <= int(temp2) <= 255:
                        finalOutput.append(movei(input2[i][1], temp2))
                    else:
                        finalOutput.append("illegal immediate value in line number " + str(input2[i][-2]))
            elif reg[temp] in ["000", "001", "010", "011", "100", "101", "110", "111"]:
                if input2[i][1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                else:
                    finalOutput.append(mover(input2[i][1], input2[i][2]))
            else:
                finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
        if input2[i][0] == "mul":
            count = 0
            for j in range(1, 4):
                if input2[i][j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(mul(input2[i][1], input2[i][2], input2[i][3]))
        if input2[i][0] == "div":
            if input2[i][1] not in non_flag_reg or input2[i][2] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
            else:
                finalOutput.append(div(input2[i][1], input2[i][2]))
        if input2[i][0] == "rs":
            temp = input2[i][2]
            if temp[0] == "$":
                temp2 = temp[1:]
                if input2[i][1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                else:
                    if 0 <= int(temp2) <= 255:
                        finalOutput.append(rs(input2[i][1], temp2))
                    else:
                        finalOutput.append("illegal immediate value in line number " + str(input2[i][-2]))
        if input2[i][0] == "ls":
            temp = input2[i][2]
            if temp[0] == "$":
                temp2 = temp[1:]
                if input2[i][1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                else:
                    if 0 <= int(temp2) <= 255:
                        finalOutput.append(ls(input2[i][1], temp2))
                    else:
                        finalOutput.append("illegal immediate value in line number " + str(input2[i][-2]))
        if input2[i][0] == "or":
            count = 0
            for j in range(1, 4):
                if input2[i][j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(Or(input2[i][1], input2[i][2], input2[i][3]))
        if input2[i][0] == "and":
            count = 0
            for j in range(1, 4):
                if input2[i][j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(And(input2[i][1], input2[i][2], input2[i][3]))
        if input2[i][0] == "not":
            if input2[i][1] not in non_flag_reg or input2[i][2] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
            else:
                finalOutput.append(Invert(input2[i][1], input2[i][2]))
        if input2[i][0] == "cmp":
            if input2[i][1] not in non_flag_reg or input2[i][2] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
            else:
                finalOutput.append(Compare(input2[i][1], input2[i][2]))
        if input2[i][0] == "xor":
            count = 0
            for j in range(1, 4):
                if input2[i][j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(xor(input2[i][1], input2[i][2], input2[i][3]))
        if input2[i][0] == "ld":
            tempLabel = input2[i][2]
            flag = 0
            index_having_address = 0
            if input2[i][1] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
            else:
                for j in range(len(input2)):
                    if input2[j][0] == "var":
                        if input2[j][1] == tempLabel:
                            flag += 1
                            index_having_address = j
                if flag == 1:
                    finalOutput.append(load(input2[i][1], input2[index_having_address][-1]))
                elif flag == 0:
                    finalOutput.append("use of undefined variable in line number" + str(input2[i][-2]))
                else:
                    finalOutput.append("variable declared more than once")
        if input2[i][0] == "st":
            tempLabel = input2[i][2]
            flag = 0
            index_having_address = 0
            if input2[i][1] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(input2[i][-2]))
            else:
                for j in range(len(input2)):
                    if input2[j][0] == "var":
                        if input2[j][1] == tempLabel:
                            flag += 1
                            index_having_address = j
                if flag == 1:
                    finalOutput.append(store(input2[i][1], input2[index_having_address][-1]))
                elif flag == 0:
                    finalOutput.append("use of undefined variable in line number" + str(input2[i][-2]))
                else:
                    finalOutput.append("variable declared more than once")
        if input2[i][0] == "jmp":
            tempLabel = input2[i][1] + ":"
            flag = 0
            label_defined_at_line = []
            tempList = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(input2[i][-2]))
            elif flag == 1:
                finalOutput.append(jump(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if input2[i][0] == "jlt":
            tempLabel = input2[i][1] + ":"
            flag = 0
            label_defined_at_line = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(input2[i][-2]))
            elif flag == 1:
                finalOutput.append(jlt(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if input2[i][0] == "jgt":
            tempLabel = input2[i][1] + ":"
            flag = 0
            label_defined_at_line = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(input2[i][-2]))
            elif flag == 1:
                finalOutput.append(jgt(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if input2[i][0] == "je":
            tempLabel = input2[i][1] + ":"
            flag = 0
            label_defined_at_line = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(input2[i][-2]))
            elif flag == 1:
                finalOutput.append(je(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if input2[i][0] == "hlt":
            lineNumber = input2[i][-2]
            flag = 0
            for j in range(len(input2)):
                if input2[j][-2] > lineNumber:
                    flag = 1
            if flag == 1:
                finalOutput.append("halt not last instruction and declared at line number " + str(input2[i][-2]))
            else:
                finalOutput.append(halt())
    elif input2[i][0][-1] == ":":
        instructionList = input2[i][1:]
        if instructionList[0] == "add":
            count = 0
            for j in range(1, 4):
                if instructionList[j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(add(instructionList[1], instructionList[2], instructionList[3]))
        if instructionList[0] == "sub":
            count = 0
            for j in range(1, 4):
                if instructionList[j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(sub(instructionList[1], instructionList[2], instructionList[3]))
        if instructionList[0] == "mov":
            temp = instructionList[2]
            if temp[0] == "$":
                temp2 = temp[1:]
                if instructionList[1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                else:
                    if 0 <= int(temp2) <= 255:
                        finalOutput.append(movei(instructionList[1], temp2))
                    else:
                        finalOutput.append("illegal immediate value in line number " + str(instructionList[-2]))
            elif reg[temp] in ["000", "001", "010", "011", "100", "101", "110", "111"]:
                if instructionList[1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                else:
                    finalOutput.append(mover(instructionList[1], instructionList[2]))
            else:
                finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
        if instructionList[0] == "mul":
            count = 0
            for j in range(1, 4):
                if instructionList[j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(mul(instructionList[1], instructionList[2], instructionList[3]))
        if instructionList[0] == "div":
            if instructionList[1] not in non_flag_reg or instructionList[2] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
            else:
                finalOutput.append(div(instructionList[1], instructionList[2]))
        if instructionList[0] == "rs":
            temp = instructionList[2]
            if temp[0] == "$":
                temp2 = temp[1:]
                if instructionList[1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                else:
                    if 0 <= int(temp2) <= 255:
                        finalOutput.append(rs(instructionList[1], temp2))
                    else:
                        finalOutput.append("illegal immediate value in line number " + str(instructionList[-2]))
        if instructionList[0] == "ls":
            temp = instructionList[2]
            if temp[0] == "$":
                temp2 = temp[1:]
                if instructionList[1] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                else:
                    if 0 <= int(temp2) <= 255:
                        finalOutput.append(ls(instructionList[1], temp2))
                    else:
                        finalOutput.append("illegal immediate value in line number " + str(instructionList[-2]))
        if instructionList[0] == "or":
            count = 0
            for j in range(1, 4):
                if instructionList[j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(Or(instructionList[1], instructionList[2], instructionList[3]))
        if instructionList[0] == "and":
            count = 0
            for j in range(1, 4):
                if instructionList[j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(And(instructionList[1], instructionList[2], instructionList[3]))
        if instructionList[0] == "not":
            if instructionList[1] not in non_flag_reg or instructionList[2] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
            else:
                finalOutput.append(Invert(instructionList[1], instructionList[2]))
        if instructionList[0] == "cmp":
            if instructionList[1] not in non_flag_reg or instructionList[2] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
            else:
                finalOutput.append(Compare(instructionList[1], instructionList[2]))
        if instructionList[0] == "xor":
            count = 0
            for j in range(1, 4):
                if instructionList[j] not in non_flag_reg:
                    finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
                    count += 1
                    break
            if count == 0:
                finalOutput.append(xor(instructionList[1], instructionList[2], instructionList[3]))
        if instructionList[0] == "ld":
            tempLabel = instructionList[2]
            flag = 0
            index_having_address = 0
            if instructionList[1] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
            else:
                for j in range(len(input2)):
                    if input2[j][0] == "var":
                        if input2[j][1] == tempLabel:
                            flag += 1
                            index_having_address = j
                if flag == 1:
                    finalOutput.append(load(instructionList[1], input2[index_having_address][-1]))
                elif flag == 0:
                    finalOutput.append("use of undefined variable in line number" + str(instructionList[-2]))
                else:
                    finalOutput.append("variable declared more than once")
        if instructionList[0] == "st":
            tempLabel = instructionList[2]
            flag = 0
            index_having_address = 0
            if instructionList[1] not in non_flag_reg:
                finalOutput.append("typo in register name in line number " + str(instructionList[-2]))
            else:
                for j in range(len(input2)):
                    if input2[j][0] == "var":
                        if input2[j][1] == tempLabel:
                            flag += 1
                            index_having_address = j
                if flag == 1:
                    finalOutput.append(store(instructionList[1], input2[index_having_address][-1]))
                elif flag == 0:
                    finalOutput.append("use of undefined variable in line number" + str(instructionList[-2]))
                else:
                    finalOutput.append("variable declared more than once")
        if instructionList[0] == "jmp":
            tempLabel = instructionList[1] + ":"
            flag = 0
            label_defined_at_line = []
            tempList = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(instructionList[-2]))
            elif flag == 1:
                finalOutput.append(jump(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if instructionList[0] == "jlt":
            tempLabel = instructionList[1] + ":"
            flag = 0
            label_defined_at_line = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(instructionList[-2]))
            elif flag == 1:
                finalOutput.append(jlt(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if instructionList[0] == "jgt":
            tempLabel = instructionList[1] + ":"
            flag = 0
            label_defined_at_line = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(instructionList[-2]))
            elif flag == 1:
                finalOutput.append(jgt(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if instructionList[0] == "je":
            tempLabel = instructionList[1] + ":"
            flag = 0
            label_defined_at_line = []
            for j in range(len(input2)):
                if input2[j][0] == tempLabel:
                    label_defined_at_line.append(input2[j][-2])
                    tempInputList = input2[j]
                    flag += 1
            if flag == 0:
                finalOutput.append("use of undefined label in line number" + str(instructionList[-2]))
            elif flag == 1:
                finalOutput.append(je(tempInputList[len(tempInputList) - 1]))
            else:
                s = "label defined more than once at lines: "
                for k in range(len(label_defined_at_line)):
                    s = s + str(label_defined_at_line[k]) + ", "
                finalOutput.append(s)
        if instructionList[0] == "hlt":
            lineNumber = instructionList[-2]
            flag = 0
            for j in range(len(input2)):
                if input2[j][-2] > lineNumber:
                    flag = 1
            if flag == 1:
                finalOutput.append("halt not last instruction and declared at line number " + str(instructionList[-2]))
            else:
                finalOutput.append(halt())
    else:
        finalOutput.append("typo in instruction name in line number " + str(input2[i][-2]))

# error in which var is not declared at the starting

count2 = 0
for i in range(len(finalOutput)):
    if "1001100000000000" in finalOutput:
        if "1001100000000000" != finalOutput[-1]:
            finalOutput.append("halt not last instruction")
            count2 = -100
    elif "1001100000000000" not in finalOutput:
        count2 = -200
for i in range(len(finalOutput)):
    if len(finalOutput[i]) != 16:
        print(finalOutput[i])
        count2 += 1
        break
if count2 == -100:
    for j in range(len(finalOutput)):
        if len(finalOutput[j]) != 16:
            print(finalOutput[j])
            break
if count2 == -200:
    print("missing halt instruction")
else:
    if count2 == 0:
        for j in range(len(finalOutput)):
            print(finalOutput[j])
