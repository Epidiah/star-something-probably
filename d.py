import math
import random
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            size = int(sys.argv[1])
            pad = len(sys.argv[1])
        except:
            if sys.argv[1].lower() in ['-f', 'f']:
                size = -1
                pad = 1
            else:
                print('Only -f and  integers >= 0 are allowed as arguments.')
                sys.exit()
    else:
        size = 6
        pad = 1
    r = -1
    if size >= 1:
        rset = set(range(1,size+1))
    elif size == 0:
        rset = set(range(10))
    else:
        rset = {'+','-',' '}
    for n in range(random.randint(7,17)):
        r = random.choice(list(rset.difference([r])))
        print(f'[{r:{pad}}]',end='\r')
        time.sleep(0.1+0.01*n**1.5)
        print(' '*n,end='')
    print(f'\033[1m[{random.choice(list(rset.difference([r]))):{pad}}]\033[0m')
