import sys

pc = 0
kbd_input = ""

def main():
    global pc

    pc = 0
    memory = [0 for x in range(32678)]
    print("Enter input file name:")
    f = open(input(), "rb")
    print("Enter asm output file name:")
    fw = open(input(), "w")


    def halt_op():
        fw.write("halt")
        return

    def set_op():
        # loc = read_next_word()
        # write_to_loc(loc, read_reg_or_value(read_next_word()))
        fw.write("set ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def push_op():
        # val = read_reg_or_value(read_next_word())
        # # print(stack)
        # stack.append(val)
        fw.write("push ")
        print_val_or_reg(read_next_word())
        return

    def pop_op():
        # val = stack.pop()
        # loc = read_next_word()
        # # print(val)
        # # print(stack)
        # write_to_loc(loc, val)
        fw.write("pop ")
        print_val_or_reg(read_next_word())
        return

    def eq_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # val_c = read_reg_or_value(read_next_word())
        # # print("eq", val_b, val_c)
        # if val_b == val_c:
        #     write_to_loc(loc, 1)
        # else:
        #     write_to_loc(loc, 0)
        fw.write("eq ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def gt_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # val_c = read_reg_or_value(read_next_word())
        # if val_b > val_c:
        #     write_to_loc(loc, 1)
        # else:
        #     write_to_loc(loc, 0)
        fw.write("gt ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def jmp_op():
        # loc = read_reg_or_value(read_next_word())
        # set_pc(loc)
        fw.write("jmp ")
        print_val_or_reg(read_next_word())
        return

    def jt_op():
        # compare = read_reg_or_value(read_next_word())
        # loc = read_reg_or_value(read_next_word())
        # if compare != 0:
        #     set_pc(loc)
        fw.write("jt ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def jf_op():
        # compare = read_reg_or_value(read_next_word())
        # loc = read_reg_or_value(read_next_word())
        # if compare == 0:
        #     set_pc(loc)
        fw.write("jf ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def add_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # val_c = read_reg_or_value(read_next_word())
        # write_to_loc(loc, (val_b + val_c) % 32768)
        fw.write("add ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def mult_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # val_c = read_reg_or_value(read_next_word())
        # write_to_loc(loc, (val_b * val_c) % 32768)
        fw.write("mult ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def mod_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # val_c = read_reg_or_value(read_next_word())
        # write_to_loc(loc, val_b % val_c)
        fw.write("mod ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def and_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # val_c = read_reg_or_value(read_next_word())
        # write_to_loc(loc, val_b & val_c)
        fw.write("and ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def or_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # val_c = read_reg_or_value(read_next_word())
        # write_to_loc(loc, val_b | val_c)
        fw.write("or ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def not_op():
        # loc = read_next_word()
        # val_b = read_reg_or_value(read_next_word())
        # write_to_loc(loc, val_b ^ 32767)
        fw.write("not ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def rmem_op():
        # write_loc = read_next_word()
        # read_loc = read_reg_or_value(read_next_word())
        # # print("rmem", write_loc, read_loc)
        # write_to_loc(write_loc, memory[read_loc])
        fw.write("not ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def wmem_op():
        # write_loc = read_reg_or_value(read_next_word())
        # read_val = read_reg_or_value(read_next_word())
        # # print("wmem", write_loc, read_val)
        # memory[write_loc] = read_val
        fw.write("wmem ")
        print_val_or_reg(read_next_word())
        fw.write(", ")
        print_val_or_reg(read_next_word())
        return

    def call_op():
        # addr = read_reg_or_value(read_next_word())
        # stack.append(pc)
        # # print("call", addr)
        # set_pc(addr)
        fw.write("call ")
        print_val_or_reg(read_next_word())
        return

    def ret_op():
        # addr = stack.pop()
        # # print(stack)
        # set_pc(addr)
        fw.write("ret ")
        return

    def out_op():
        # print(chr(read_reg_or_value(read_next_word())), end='')
        fw.write("out ")
        print_val_or_reg(read_next_word())
        return

    def in_op():
        # # print("need to read now")
        # global kbd_input
        # if kbd_input == "":
        #     kbd_input = input() + '\n'
        # ch = ord(kbd_input[0])
        # kbd_input = kbd_input[1:]
        # # print(kbd_input)
        # write_loc = read_next_word()
        # write_to_loc(write_loc, ch)
        fw.write("in ")
        return

    def noop_op():
        # Aaaaand we're done!
        fw.write("noop")
        return

    def read_next_word():
        word = memory[pc]
        set_pc(pc + 1)
        return word

    def set_pc(new_pc):
        global pc
        pc = new_pc

    def print_val_or_reg(val):
        if val >= 32768 and val < 32776:
            fw.write("r" + str(val - 32768))
        else:
            fw.write(str(val))
        return

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
    while pc < len(memory):
        word = f.read(2)
        if word == b'':
            break
        # print(pc, int.from_bytes(word, byteorder='little'))
        memory[pc] = int.from_bytes(word, byteorder='little')
        pc += 1
    pc = 0
    f.close()

    while pc < len(memory):
        word = read_next_word()
        if( word < len(ops)):
            fw.write("\n" + str(pc-1) + ": ")
            ops[word]()
    
    fw.close()

main()