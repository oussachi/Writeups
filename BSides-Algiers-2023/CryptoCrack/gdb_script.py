import os
import sys
LOG_FILE = '/tmp/gdb.log'


print('setting the fork follow mode')
gdb.execute('set follow-fork-mode child')
gdb.execute('b *main+260')
gdb.execute('r')
print('bypassing the child debugging check')
gdb.execute('set $rax = 0')
gdb.execute('c')
