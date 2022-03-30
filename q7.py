import json
dict={"Name": "Abhishek",
"Designation": "CEO of navgurukul",
"Gender": "male","age":29}
with open("himani.json","w") as file:
    json.dump(dict,file,indent=4)