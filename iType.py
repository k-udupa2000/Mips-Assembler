from printColor import printColor
from writeToFile import writeToFile
from getRegisterCode import getRegisterCode


def iType2Args(inst, reg1, reg2):
    l = ["SW", "LW", "BLTZ", "BLEZ", "BGTZ"]
    if inst.upper() not in l:
        raise Exception(" Wrong instruction format")

    regCode1 = getRegisterCode(reg1)
    printColor(regCode1, "red")
    writeToFile(regCode1)

    if reg2.find("(") != -1:
        index = reg2.index("(")
        offset = reg2[0:index]
        offset = int(offset)
        if offset % 4:
            raise Exception(" Boundary is not word aligned")
        binaddr = ""
        binaddr += bin(offset).replace("0b", "")
        binaddr = binaddr.zfill(16)
        index2 = reg2.index(")")
        secondReg = reg2[(index + 1) : index2]

        regCode2 = getRegisterCode(secondReg)
        printColor(regCode2, "blue")
        writeToFile(regCode2)

        printColor(binaddr + "\n", "green")
        writeToFile(binaddr + "\n")
    else:
        binaddr = ""
        for i in range(3, len(reg2)):
            binaddr += "{0:04b}".format(int(reg2[i], 16))
        printColor(binaddr[2:] + "\n", "blue")
        writeToFile(binaddr[2:] + "\n")


def iType3Args(inst, reg1, reg2, dest):
    set1 = ["ADDI", "SUBI", "DIVI", "SLTI"]
    set2 = ["BEQ", "BNE", "BLT", "BGT"]
    binaddr = ""

    if inst.upper() in set1:
        if dest.find("0x") == -1:
            binaddr += bin(int(dest, 16)).replace("0b", "")
            binaddr = binaddr.zfill(16)
        else:
            for i in range(6, len(dest)):
                binaddr += "{0:04b}".format(int(dest[i], 16))

    elif inst.upper() in set2:
        for i in range(6, len(dest)):
            binaddr += "{0:04b}".format(int(dest[i], 16))

    regCode1 = getRegisterCode(reg1)
    printColor(regCode1, "red")
    writeToFile(regCode1)

    regCode2 = getRegisterCode(reg2)
    printColor(regCode2, "blue")
    writeToFile(regCode2)

    printColor(binaddr + "\n", "green")
    writeToFile(binaddr + "\n")
