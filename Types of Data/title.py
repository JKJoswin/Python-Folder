def convert(s):
    dict={}
    for item in s:
        dict[item[0]]=item[1:]
    return dict

student=[[1,"James","5"],[2,"John","6"],[3,"Jack","5"]]
print(student)
print(convert(student))