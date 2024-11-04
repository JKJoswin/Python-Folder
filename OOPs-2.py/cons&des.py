class employee:
    def __init__(self):
        print("Constructor called!")
    
    def __del__(self):
        print("Destructor called!")

e1=employee()
e2=employee()

del e1
print("Object deleted!")