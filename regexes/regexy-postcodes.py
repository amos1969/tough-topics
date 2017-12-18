import re

def is_postcode(postal):
    # findall returns a matching string in a list
    result = re.findall(r"^[A-Z]{1,2}[0-9]{1,2}\s[[0-9][A-Z]{2}$", postal)
    # The result evaluates to True if it isn't empty false otherwise
    result = bool(result)
    return result

postcode = "BL1 3DU"
postcode2 = "W5 3TR"
not_postcode = "TTR 4XJ"
not_postcode2 = "XT 7PJ"

print(postcode, is_postcode(postcode))
print(postcode2, is_postcode(postcode2))
print(not_postcode, is_postcode(not_postcode))
print(not_postcode2, is_postcode(not_postcode2))