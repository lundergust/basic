import random
w, h = 32, 32;
buff  = [[0 for x in range(w)] for y in range(h)]
for i in range(32):
    for j in range(32):
        buff[i][j]= int(random.random()*100)
        print(buff[i][j])

max = 0
for i in range(32):
    for j in range(32):
        newmax = buff[i][j]
        if newmax > max:
            max = newmax
            newI = i
            newJ = j

print("Max = " + str(max))
print("x = " + str(newI))
print("y = " + str(newJ))
# print("Position = " + str(position))
