import time
import sys
import random
print '\n'
T = 186 
start = T/2
while True:
    rval = random.randint(1,2)
    if rval == 1:
        start = start + 1
    else:
        start = start - 1
    for t in range(0, start):
        sys.stdout.write('-')
    sys.stdout.write('*')
    for t in range(start, T):
        sys.stdout.write('-')
    time.sleep(0.05)
    sys.stdout.write('\n')
    sys.stdout.flush()
