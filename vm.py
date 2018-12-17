import sys

def main():
    regs = [0 for x in range(8)]
    f = open(sys.argv[1], "rb")

    def halt_op():
        quit()
        return

    def set_op():
        reg = read_next_word() - 32768
        regs[reg] = read_reg_or_value(read_next_word())
        return

    def push_op():
        return

    def pop_op():
        return

    def eq_op():
        reg = read_next_word() - 32768
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        if val_b == val_c:
            regs[reg] = 1
        else:
            regs[reg] = 0
        return

    def gt_op():
        reg = read_next_word() - 32768
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        if val_b > val_c:
            regs[reg] = 1
        else:
            regs[reg] = 0
        return

    def jmp_op():
        loc = read_next_word()
        # need to account for registers
        f.seek(loc * 2)
        return

    def jt_op():
        compare = read_reg_or_value(read_next_word())
        loc = read_reg_or_value(read_next_word())
        if compare != 0:
            f.seek(loc * 2)
        return

    def jf_op():
        compare = read_reg_or_value(read_next_word())
        loc = read_reg_or_value(read_next_word())
        if compare == 0:
            f.seek(loc * 2)
        return

    def add_op():
        reg = read_next_word() - 32768
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        regs[reg] = (val_b + val_c) % 32768
        return

    def mult_op():
        return

    def mod_op():
        return

    def and_op():
        return

    def or_op():
        return

    def not_op():
        return

    def rmem_op():
        return

    def wmem_op():
        return

    def call_op():
        return

    def ret_op():
        return

    def out_op():
        print(chr(read_next_word()), end='')
        return

    def in_op():
        return

    def noop_op():
        # Aaaaand we're done!
        return

    def read_next_word():
        return int.from_bytes(f.read(2), byteorder='little')

    def read_reg_or_value(word):
        if word >= 32768 and word < 32776:
            return regs[word-32768]
        else:
            return word

    ops = [
        halt_op,
        set_op,
        push_op,
        pop_op,
        eq_op,
        gt_op,
        jmp_op,
        jt_op,
        jf_op,
        add_op,
        mult_op,
        mod_op,
        and_op,
        or_op,
        not_op,
        rmem_op,
        wmem_op,
        call_op,
        ret_op,
        out_op,
        in_op,
        noop_op
    ]

    while True:
        word = read_next_word()
        print(word)
        ops[word]()
    # word = f.read(2)
    # print(word)
    # print(int.from_bytes(word, byteorder='little'))

main()