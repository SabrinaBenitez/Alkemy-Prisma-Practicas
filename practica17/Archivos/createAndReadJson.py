import json
test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
json_str = json.dumps(test_dict,indent=4,sort_keys=True)

with open('test.json',"w") as f:
    f.write( json_str)

with open('test.json',"r") as f:
    json_dic = json.load(f)

print( json_dic["bigberg"])