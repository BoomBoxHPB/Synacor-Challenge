import sys

pc = 0
kbd_input = ""

def main():
    global pc
    regs = [0 for x in range(8)]
    stack = []
    memory = [0 for x in range(32678)]
    pc = 0
    f = open(sys.argv[1], "rb")

    def halt_op():
        quit()
        return

    def set_op():
        loc = read_next_word()
        write_to_loc(loc, read_reg_or_value(read_next_word()))
        return

    def push_op():
        val = read_reg_or_value(read_next_word())
        # print(stack)
        stack.append(val)
        return

    def pop_op():
        val = stack.pop()
        loc = read_next_word()
        # print(val)
        # print(stack)
        write_to_loc(loc, val)
        return

    def eq_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        # print("eq", val_b, val_c)
        if val_b == val_c:
            write_to_loc(loc, 1)
        else:
            write_to_loc(loc, 0)
        return

    def gt_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        if val_b > val_c:
            write_to_loc(loc, 1)
        else:
            write_to_loc(loc, 0)
        return

    def jmp_op():
        loc = read_reg_or_value(read_next_word())
        set_pc(loc)
        return

    def jt_op():
        compare = read_reg_or_value(read_next_word())
        loc = read_reg_or_value(read_next_word())
        if compare != 0:
            set_pc(loc)
        return

    def jf_op():
        compare = read_reg_or_value(read_next_word())
        loc = read_reg_or_value(read_next_word())
        if compare == 0:
            set_pc(loc)
        return

    def add_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        write_to_loc(loc, (val_b + val_c) % 32768)
        return

    def mult_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        write_to_loc(loc, (val_b * val_c) % 32768)
        return

    def mod_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        write_to_loc(loc, val_b % val_c)
        return

    def and_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        write_to_loc(loc, val_b & val_c)
        return

    def or_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        val_c = read_reg_or_value(read_next_word())
        write_to_loc(loc, val_b | val_c)
        return

    def not_op():
        loc = read_next_word()
        val_b = read_reg_or_value(read_next_word())
        write_to_loc(loc, val_b ^ 32767)
        return

    def rmem_op():
        write_loc = read_next_word()
        read_loc = read_reg_or_value(read_next_word())
        # print("rmem", write_loc, read_loc)
        write_to_loc(write_loc, memory[read_loc])
        return

    def wmem_op():
        write_loc = read_reg_or_value(read_next_word())
        read_val = read_reg_or_value(read_next_word())
        # print("wmem", write_loc, read_val)
        memory[write_loc] = read_val
        return

    def call_op():
        addr = read_reg_or_value(read_next_word())
        stack.append(pc)
        # print(stack)
        set_pc(addr)
        return

    def ret_op():
        addr = stack.pop()
        # print(stack)
        set_pc(addr)
        return

    def out_op():
        print(chr(read_reg_or_value(read_next_word())), end='')
        return

    def in_op():
        # print("need to read now")
        global kbd_input
        if kbd_input == "":
            kbd_input = input() + '\n'
        ch = ord(kbd_input[0])
        kbd_input = kbd_input[1:]
        # print(kbd_input)
        write_loc = read_next_word()
        write_to_loc(write_loc, ch)
        return

    def noop_op():
        # Aaaaand we're done!
        return

    def read_next_word():
        word = memory[pc]
        set_pc(pc + 1)
        return word

    def read_reg_or_value(word):
        if word >= 32768 and word < 32776:
            return regs[word-32768]
        else:
            return word

    def write_to_loc(loc, val):
        if loc >= 32776:
            print("Error, invalid location")
            quit()
        elif loc >= 32768:
            regs[loc-32768] = val
        # memory has its own write mechanism
        else:
            print("Error, invalid location (in memory)")
            # memory[loc] = val
        return

    def set_pc(new_pc):
        global pc
        pc = new_pc

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


    pc = 0
    while pc < 32678:
        word = f.read(2)
        # print(word)
        if word == b'':
            break
        # print(pc, int.from_bytes(word, byteorder='little'))
        memory[pc] = int.from_bytes(word, byteorder='little')
        pc += 1
    pc = 0
    f.close()

    while True:
        word = read_next_word()
        # print(word)
        ops[word]()
    # word = f.read(2)
    # print(word)
    # print(int.from_bytes(word, byteorder='little'))

main()