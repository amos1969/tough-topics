def is_postcode(postal):
    valid = True
    # Add some code here to make this work

    return valid


postcode = "BL1 3DU"
postcode2 = "W5 3TR"
not_postcode = "TTR 4XJ"
not_postcode2 = "XT 7PJ"

print(postcode, is_postcode(postcode))
print(postcode2, is_postcode(postcode2))
print(not_postcode, is_postcode(not_postcode))
print(not_postcode2, is_postcode(not_postcode2))