code = []

with open("input") as j:
    for i in j:
        code = i.split(",")

for i in range(len(code)):
    code[i] = int(code[i])
OLDCODE = []
for i in code:
    OLDCODE.append(i)
code[1] = 12
code[2] = 2


def Eval(code,i,II):
    #code = []
    #for i in Code:
        #code.append(i)
    #print(code == Code)
    pos = 1
    op = None
    operators = []
    code[1] = i
    code[2] = II
    for i in code:
        if pos == 1:
            if i == 1:
                op = "ADD"
            if i == 2:
                op = "TIMES"
            if i == 99:
                return(code[0])
        elif pos == 2 or pos == 3:
            if i< len(code):
                operators.append(code[i])
            else:
                return(0)
        else:
            if i< len(code):
                if op == "ADD":
                    code[i] = operators[0]+operators[1]
                else:
                    code[i] = operators[0]*operators[1]
            operators=[]
        pos+= 1
        if pos ==  5:
            pos = 1

Part_1 = Eval(code,12,2)
print(Part_1)
Part_2 = None
nounFound = False
verbfound = False
noun = 0
verb = 0
Part_2 = None


for k in range(10000):
    temp = []
    for i in OLDCODE:
        temp.append(i)
    j = str(k)
    while len(j)<4:
        j="0"+j
    k = Eval(temp,int(j[0:1]),int(j[2:3]))
    if k == 19690720:
        Part_2 = j
    #print(OLDCODE==temp)
    print(19690720-k)
            

print("Part 1:",Part_1)
print("Part 2:",Part_2)