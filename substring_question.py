substring="the quick born fox jumped over the lazy dog slpet over the"
substring=substring.split(" ")
index=0
empty=0
while index<len(substring):
    if (sbstring[index])=="over":
        empty.append("an")
    else:
        empty.append(substring[index])
    index=index+1
print(empty)