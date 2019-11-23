function_decoder = {
        "add": "100000",
        "addu": "100001",
        "and": "100100",
        "div": "011010",
        "divu": "011011",
        "mfhi": "010000",
        "mflo": "010010",
        "mthi": "010001",
        "mtlo": "010011",
        "mult": "011000",
        "multu": "011001",
        "nor": "100111",
        "or": "100101",
        "sll": "000000",
        "sllv": "000100",
        "slt": "101010",
        "sltu": "101011",
        "sra": "000011",
        "srav": "000111",
        "srl": "000010",
        "srlv": "000110",
        "sub": "100010",
        "subu": "100011",
        "xor": "100110",
    }
s = []
for f in function_decoder:
    s.append(f.upper())

print(s)