popu={'china':146,'india':136,'usa':32,'pakistan':21}
def add():
    c=input("Enter the country:")
    if c in popu:
        print("Already exists")
        return
    p=int(input("enter population for country"))
    popu[c]=p
    print(popu)
def remove():
    c=input("Enter the country to remove:")
    if c not in popu:
        print("Does not exists")
        return
    del popu[c]
    print(popu)
def query():
    c=input("Enter the country:")
    if c not in popu:
        print("Does not exists")
        return
    print(f'Population of {c} if {popu[c]} crore')
def print_all():
    for c,p in popu.items():
        print(f"{c}==>{p}")
def main():
    a=input("Enter the operation(add,remove,query,print)"'\n')
    if a=='add':
        add()
    elif a=='remove':
        remove()
    elif a=='query':
        query()
    elif a=='print':
        print_all()
if __name__=='__main__':
    main()