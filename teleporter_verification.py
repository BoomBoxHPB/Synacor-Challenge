import sys

regs = [0 for x in range(8)]
stack = []

def f6027():
    if regs[0] != 0:
        return f6035()
    else:
        regs[0] = ( regs[1] + 1 ) % 32768
    return

def f6035():
    if regs[1] != 0:
        return f6048()
    else:
        regs[0] = ( regs[0] + 32767 ) % 32768
        regs[1] = regs[7]
        f6027()
    return

def f6048():
    stack.append(regs[0])
    regs[1] = ( regs[1] + 32767 ) % 32768
    f6027()
    regs[1] = regs[0]
    regs[0] = stack.pop()
    regs[0] = ( regs[0] + 32767 ) % 32768
    return f6027()

def main():
    # sys.setrecursionlimit(5000)
    for x in range(1, 32768):
        #run verification for all possible inputs, stop once the out is 6
        regs[0] = 4
        regs[1] = 1
        regs[2] = 0
        regs[3] = 0
        regs[4] = 0
        regs[5] = 0
        regs[6] = 0
        regs[7] = x
        f6027()
        if regs[0] == 6:
            print(x)
            return

main()