def best_fit_line(data):
    list_x = []
    list_y = []
    for coord in data:
        list_x.append(coord[0])
        list_y.append(coord[1])
        
    m1 = 0.0
    for i in range(len(data)):
        m1 += list_x[i] * list_y[i]
        
    m2 = (sum(list_x) * sum(list_y))/len(data)
    
    m3 = 0.0
    for i in range(len(data)):
        m3 += pow(list_x[i], 2)
        
    m4 = pow(sum(list_x), 2) / len(data)
    
    m = round((m1 - m2) / (m3 - m4), 2)
    b = round((sum(list_y)/len(list_y)) - m * (sum(list_x)/len(list_x)), 2)
    return m , b
    
    
data = []
x = input("Enter x: ")
while x != '':
    y = input("Enter y: ")
    data.extend([[float(x), float(y)]])
    x = input("Enter x: ")
m, b = best_fit_line(data)
print(f"y = {m}x + {b} ")
