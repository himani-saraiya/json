from inspect import indentsize
import json
dic={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20"}}
with open("himani1.json","w") as file:
    json.dump(dic,file,indent=4)
    x=input("konsa item :")
    y=int(input("kitne item chahte ho:"))
    with open("himani1.json","w") as file:
        for i in dic.values():
            
