
def nLargest():
    a=[1,572,13,14,55,61,7,123438,2349]
    l=len(a)
    n=2
    n1=0
    n2=0
    for i in range(1,l):
        if(n1<a[i]):
            n1=a[i]
        if(n2<a[i] & a[i]<n1):
            n2=a[i]
    print(n1,"\n",n2)
if __name__ == "__main__":
    nLargest()
