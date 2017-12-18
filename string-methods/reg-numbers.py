def is_reg_number(reg_num):
    valid = True
    if len(reg_num) != 8:
        valid = False
    elif not reg_num[0].isalpha():
        valid = False
    elif not reg_num[1].isalpha():
        valid = False
    elif not reg_num[2].isnumeric():
        valid = False
    elif not reg_num[3].isnumeric():
        valid = False
    elif reg_num[4] != " ":
        valid = False
    elif not reg_num[5].isalpha():
        valid = False
    elif not reg_num[6].isalpha():
        valid = False
    elif not reg_num[7].isalpha():
        valid = False
    return valid

reg = "MM10 JVP"
non_reg = "F387 XEJ"

print(reg, is_reg_number(reg))
print(non_reg, is_reg_number(non_reg))