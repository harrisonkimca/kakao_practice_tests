
def make_2D_array(rows, columns):
    rows, cols = (rows, columns)
    arr=[]
    for i in range(rows):
        col = []
        inner = 1
        for j in range(cols):    
            col.append(inner)
            inner += 1
        arr.append(col)
    print(arr)