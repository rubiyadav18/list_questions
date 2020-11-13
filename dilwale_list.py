kitna_paisa_hai=[3000, 60000, 324990909, 90990900, 30000, 5600000, 510,30000, 5600000, 690909]
i=0
crorpati=0
lakhpati=0
dilwale=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]> 10000000:
        crorpati=crorpati+1
    elif kitna_paisa_hai[i] > 100000:
        lakhpati=lakhpati+1
    else:
        dilwale=dilwale+1
    i=i+1
print(crorpati,"carorpati")
print(lakhpati,"lakhpati")
print(dilwale,"dilwale")