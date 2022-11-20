from binarytree import Node

optab = {
	"ADD":"18",
	"AND":"40",
	"COMP":"28",
	"DIV":"24",
	"J":"3C",
	"JEQ":"30",
	"JGT":"34",
	"JLT":"38",
	"JSUB":"48",
	"LDA":"00",
	"LDCH":"50",
	"LDL":"08",
	"LDX":"04",
	"MUL":"20",
	"OR":"44",
	"RD":"D8",
	"RSUB":"4C",
	"STA":"0C",
	"STCH":"54",
	"STL":"14",
	"STSW":"E8",
	"STX":"10",
	"SUB":"1C",
	"TD":"E0",
	"TIX":"2C",
	"WD":"DC"
}

line_elem = []
tree = Node()
# sym = {}


with open('input.txt','r') as test_input:
    first_line = test_input.readline().split()
    LOCCTR = first_line[2]
    tree.insert(first_line[0], hex(int(LOCCTR,16)))
    # with open('SymbolTab.txt','w') as Symbol_output:
    for line in test_input.readlines():
        line_elem = line.split()
        # sym[line_elem[0]] = hex(int(LOCCTR,16))

        if line_elem[0] != '-':
            tree.insert(line_elem[0], LOCCTR)

        if line_elem[1] in optab or line_elem[1] == 'WORD':
            LOCCTR = hex(int(LOCCTR,16)+3)
        elif line_elem[1] == "RESW":
            temp = hex(int(line_elem[2])*3)
            LOCCTR = hex(int(LOCCTR,16)+int(temp,16))
        elif line_elem[1]=="RESB":
            LOCCTR = hex(int(LOCCTR,16)+int(line_elem[2]))
        elif line_elem[1]=="BYTE":
            if line_elem[2][0]=="X":
                LOCCTR = hex(int(LOCCTR,16)+(len(line_elem[2])-3)/2)
            elif line_elem[2][0]=="C":
                LOCCTR = hex(int(LOCCTR,16)+(len(line_elem[2])-3))

tree.inorder()

