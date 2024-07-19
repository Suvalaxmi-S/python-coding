items=['apple','cucumber','grapes']
def largest(items):
    max=0
    str=''
    for i in items:
        length=len(i)
        if length > max:
            max=length
            str=i
    return str  
print("largest",largest(items))  