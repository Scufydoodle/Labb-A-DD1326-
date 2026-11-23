def finns(p,value):
    stringValue = str(value)
    if p == None:
        return False

    if p.key == stringValue:
        return True    
      
    if min(p.key, stringValue) == stringValue:
        return finns(p.leftPointer, value)
    return finns(p.rightPointer, value)
