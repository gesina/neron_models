#! /usr/bin/env python3

PI=5
RANGE_FACTOR=20
RANGE_A=(-RANGE_FACTOR*PI,RANGE_FACTOR*PI)
RANGE_B=(0,RANGE_FACTOR*PI)

def RESTRICTION(d,a,pi):
    return (d!=0
            and (6912*a**3)%d==0
            and d%(pi**2)==0 and d%(pi**3)!=0)

def primzerlegung(num):
    """Prime factors of num"""
    prime_factors={}
    maximum=2
    while num>maximum:
        for i in range(maximum,num+1):
            if num%i == 0:
                maximum=i
                power=0
                while num%i==0:
                    num=(int)(num/i)
                    power=power+1
                prime_factors[i]=power
                break
    for i in prime_factors:
        if i>maximum:
            maximum=i
    return prime_factors

def discriminant(a,b):
    return ((4*(a**3))+(27*(b**2)))

def make_list(pi=PI,
              range_a=RANGE_A,range_b=RANGE_B,
              step_a=PI, step_b=PI,
              restriction=RESTRICTION):
    l=[]
    for a in range(range_a[0], range_a[1]+1, step_a):
        for b in range(range_b[0], range_b[1]+1, step_b):
            d=abs(discriminant(a,b))
            if restriction(d,a,pi):
                #print(a,'|',b,'|',d,'|',primzerlegung(d))
                l.append((a,b,d,primzerlegung(d)))
    return l

def print_list(l, sep='\t'):
    for i in l:
        print(sep.join(map(str, i)))

def get_result(pi=PI,
               range_factor=20,
               restriction=RESTRICTION,
               sep="\t",
               step_a=0, step_b=0):
    step_a=step_a or pi
    step_b=step_b or pi
    print("PI:",pi,"; RANGE_FACTOR:",range_factor,"-----------------------")
    l = make_list(pi=pi,
                  range_a=(-range_factor*pi,range_factor*pi),
                  range_b=(0,range_factor*pi),
                  step_a=step_a, step_b=step_b,
                  restriction=restriction)
    print_list(l,sep=sep)
    return l
    

if __name__ == "__main__":
    startlist=get_result()
