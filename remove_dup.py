dict1 = {1: "hello", 2: "hey", 3: "hi", 4: "hello"}

tmp = [] 
result = dict() 
for key, val in dict1.items(): 
    if val not in tmp: 
        tmp.append(val) 
        result[key] = val

print(f"Cleared: {result}")