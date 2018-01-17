import re

val = "01012345678"
pattern = r"^01[016789][1-9][0-9]\d{6,7}$" #raw

if re.match(pattern, val):
    print("matched")
else:
    print("invalid")