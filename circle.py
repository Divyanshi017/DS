import math

def circle_calc(r):
    area=math.pi*(r**2)
    c=2*math.pi*r
    d=2*r
    return area, c,d

if __name__=="__main__":
    r=int(input("Enter a radius:"))
    a, c, d = circle_calc(r)
    print(f"area {a}, circumference {c}, diameter {d}")