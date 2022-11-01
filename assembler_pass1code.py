inp = open("input.txt","r")
out = open("output.txt","w")
symtab = open("SymbolTab.txt","w")
sym = {}
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

first = inp.readline()
out.write("  -\t\t"+first)
first_line = first.split()

LOCCTR = first_line[2]

for line in inp.readlines():
	line_elem = line.split()
	symtab.write(str(hex(int(LOCCTR,16)))+"\t"+line)
	sym[line_elem[0]] = str(hex(int(LOCCTR,16)))

	if line_elem[1] in optab or line_elem[1] == 'WORD':
		LOCCTR = str(hex(int(LOCCTR,16)+3))
	elif line_elem[1] == "RESW":
		temp = hex(int(line_elem[2])*3)
		LOCCTR = str(hex(int(LOCCTR,16)+int(temp,16)))
	elif line_elem[1]=="RESB":
		LOCCTR = str(hex(int(LOCCTR,16)+int(line_elem[2])))
	elif line_elem[1]=="BYTE":
		if line_elem[2][0]=="X":
			LOCCTR = str(hex(int(LOCCTR,16)+(len(line_elem[2])-3)/2))
		elif line_elem[2][0]=="C":
			LOCCTR = str(hex(int(LOCCTR,16)+(len(line_elem[2])-3)))
symtab.close()
symtab = open('SymbolTab.txt','r')
sym.pop('-')

for line in symtab.readlines():
	symbol_line_elem = line.split()
	out.write(line.replace("\n","\t"))
	
	if symbol_line_elem[1] in sym :
		out.write(sym[symbol_line_elem[3]]+"\n")
	else:
		out.write(symbol_line_elem[0][2:6]+"\n")
		
	
"""
	只剩下把'TABLE,X'轉換成'TABLE'!!!
"""

	# if line_elem[2] in sym:
	# 	out.write("hello\n")
	# elif line_elem[1] == 'RSUB':
	# 	out.write("4C0000"+"\n")
	# elif line_elem[1] not in optab:
	# 	out.write("- "+"\n")
	


inp.close()
out.close()
symtab.close()
   


