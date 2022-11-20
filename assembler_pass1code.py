from binarytree import Node

inp = open("input.txt","r")
# out = open("output.txt","w")
symtab = open("SymbolTab.txt","w")

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
sym = {}
tree = Node()

with open('input.txt','r') as test_input:
	first_line = test_input.readline().split()
	LOCCTR = first_line[2]
	tree.insert(first_line[0], hex(int(LOCCTR,16)))

	with open('SymbolTab.txt','w') as Symbol_output:
		for line in test_input.readlines():
			line_elem = line.split()
			
			# symtab.write(hex(int(LOCCTR,16)))+"\t"+line
			sym[line_elem[0]] = hex(int(LOCCTR,16))
			
			if line_elem[0] != '-':
				tree.insert(line_elem[0], LOCCTR)
				Symbol_output.write(tree.inorder()[0])
				Symbol_output.write(tree.inorder()[1])
				

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

print(tree.inorderTraversal())

"""
first = inp.readline()
out.write("  -\t\t"+first)
first_line = first.split()
"""

# LOCCTR = first_line[2]
# sym = {}
# tree = Node()


# for line in inp.readlines():
# 	# print(line)
# 	line_elem = line.split()
# 	symtab.write(str(hex(int(LOCCTR,16)))+"\t"+line)
# 	sym[line_elem[0]] = str(hex(int(LOCCTR,16)))
	
# 	if line_elem[0] != '-':
# 		tree.insert(line_elem[0], LOCCTR)

# 	if line_elem[1] in optab or line_elem[1] == 'WORD':
# 		LOCCTR = str(hex(int(LOCCTR,16)+3))
# 	elif line_elem[1] == "RESW":
# 		temp = hex(int(line_elem[2])*3)
# 		LOCCTR = str(hex(int(LOCCTR,16)+int(temp,16)))
# 	elif line_elem[1]=="RESB":
# 		LOCCTR = str(hex(int(LOCCTR,16)+int(line_elem[2])))
# 	elif line_elem[1]=="BYTE":
# 		if line_elem[2][0]=="X":
# 			LOCCTR = str(hex(int(LOCCTR,16)+(len(line_elem[2])-3)/2))
# 		elif line_elem[2][0]=="C":
# 			LOCCTR = str(hex(int(LOCCTR,16)+(len(line_elem[2])-3)))

# tree.inorder()

"""
	-------------------------------------------------------------
"""
# symtab = open('SymbolTab.txt','r')
# sym.pop('-')
# sym.update({'TABLE,X':'0x1126'})


# for line in symtab.readlines():
# 	symbol_line_elem = line.split()
# 	print(symbol_line_elem)
# 	out.write(line.replace("\n","\t"))
# 	if symbol_line_elem[2] in optab: out.write(optab[symbol_line_elem[2]])
# 	else:pass
# 	if symbol_line_elem[3] in sym :
# 		out.write(sym[symbol_line_elem[3]][2:6]+"\n")
# 	elif symbol_line_elem[2] == 'RESB' or symbol_line_elem[2] == 'RESW' or symbol_line_elem[2] == 'END':
# 		out.write("  -  "+"\n")
# 	elif symbol_line_elem[2] not in optab:
# 		out.write(symbol_line_elem[0][2:6]+"\n")
# 	elif symbol_line_elem[2] == 'WORD':
# 		out.write('hello'+"\n")
# 	elif symbol_line_elem[2] == 'RSUB':
# 		out.write('0000'+"\n")
# """
# 	只剩下把'TABLE,X'轉換成'TABLE'!!!
# """

	# if line_elem[2] in sym:
	# 	out.write("hello\n")
	# elif line_elem[1] == 'RSUB':
	# 	out.write("4C0000"+"\n")
	# elif line_elem[1] not in optab:
	# 	out.write("- "+"\n")
	


# inp.close()
# out.close()
# symtab.close()
   


# https://www.javatpoint.com/python-dictionary-update-method
