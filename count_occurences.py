char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
empty=[ ]
while i<len(char_list):
    j=0
    count=0
    empty1=[ ]
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    empty1.append(char_list[i])
    empty1.append(count)
    if empty1 not in empty:
        empty.append(empty1)
    i=i+1
print(empty)
print(count)