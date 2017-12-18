import re

def is_reg_number(reg_num):
    # findall returns a matching string in a list
    result = re.findall(r"^[A-Z]{2}[0-9]{2}\s[A-Z]{3}$", reg_num)
    # The result evaluates to True if it isn't empty false otherwise
    result = bool(result)
    return result

reg = "MM10 JVP"
non_reg = "F387 XEJ"

print(reg, is_reg_number(reg))
print(non_reg, is_reg_number(non_reg))