def count_charL(s,l,i=0): #LARGE
    if(i==len(s)-1):
        return int(s[i]==l)
    else:
        i+=1
        if s[i-1]==l:
            return 1+count_charL(s,l,i)
        else:
            return count_charL(s,l,i)
        
def count_charM(s,l,i=0): #MEDIUM
    if(i==len(s)-1):
        return int(s[i]==l)
    else:
        return int(s[i]==l) + count_charM(s,l,i+1)

def count_charS(s,l,i=0): #SMALL
    return int(s[i]==l) if (i==len(s)-1) else int(s[i]==l) + count_charS(s,l,i+1)


print(count_charS("bananaaaaaa","a"))