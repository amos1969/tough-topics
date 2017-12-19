def is_it_a_reg_number(reg):
    if reg[0:2].isalpha() and reg[2:4].isnumeric() and (reg[4] == " ") and reg[5:].isalpha():
        return True
    return False

reg_num = "MM10 JVP"
not_reg_num = "F387 XEJ"
totally_not_a_reg = "F81 TEJ"

print(is_it_a_reg_number(reg_num))
print(is_it_a_reg_number(not_reg_num))
print(is_it_a_reg_number(totally_not_a_reg))