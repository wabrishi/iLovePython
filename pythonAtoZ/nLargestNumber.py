
def nLargest(n):
    a=[1,572,13,14,55,61,7,123438,2349]
    a.sort(reverse=True)
    print(a[:n])
if __name__ == "__main__":
    nLargest(3)
