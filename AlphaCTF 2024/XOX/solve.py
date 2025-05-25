from pwn import *

def sublist(lst1, lst2):
    if((len(lst1) < 3) or len(lst1) > len(lst2)):
         return False
    a = ''
    b = ''
    for i in lst1:
         if(not (i in lst2)):
              return False
    return True


winning_combos = [[1,4,7],[1,5,9],[1,2,3],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]

p=remote(host="35.228.220.66", port=1308)
a = p.recv()
st = a.split(b"\n")[1].split(b"\n")[0].decode()
for i in range(1001):
     X_ind = []
     O_ind = []
     done = False
     i = 0
     while(i < len(st) and not done):
         if(st[i]=="X"):
               X_ind.append(i + 1)
               for listt in winning_combos:
                    if(sublist(listt, X_ind)):
                         print(f"Sending x {X_ind}")
                         p.sendline("X")
                         done = True
                         break
         else:
               O_ind.append(i + 1)
               for listt in winning_combos:
                    if(sublist(listt, O_ind)):
                         print("Sending o")
                         p.sendline("O")
                         done = True
                         break
         i += 1
     if(not(done)):
         print("Sending d")
         p.sendline("D")
     a = p.recv()
     print(a)
     st = a.split(b"\n")[1].split(b"\n")[0].decode()