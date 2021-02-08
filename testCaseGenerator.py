#------------------Imports-------------------------------------------------------------------------------
import numpy as np
import  random
import string 

#------------------Single Number Generator----------------------------------------------------------------
def SingleNumber(filename, n, minVal, maxVal, dataType):
    if dataType=="int":
        a = random.sample(range(minVal, maxVal), n)
    else:
        a = set()
        while len(a)<n:
            x = random.uniform(minVal, maxVal)
            x = round(x,2)
            a.add(x)
    file = open("TestCases/"+filename,"w+")
    for x in a:
        file.write(str(x) + "\n")
    file.close()
    
#------------------Array Generator------------------------------------------------------------------------
# Note: Max dimension is 2
def ArrayGenerate(fileName, n, dimen,minVal, maxVal, dataType):
    if dataType=="int":
        file = open(fileName,"w+")
        dimension = tuple(dimen)
        for i in range(0, n):
            a = np.random.randint(minVal, maxVal+1, size=dimension)
            x = dimen[0]
            y = dimen[1]
            for i in range(0, x):
                for j in range(0, y):
                    file.write(str(a[i][j]) + " ")
                file.write("\n")
            file.write("\n")
        file.close()
    else:
        file = open(fileName,"w+")
        dimension = tuple(dimen)
        for i in range(0, n):
            a = np.random.uniform(minVal, maxVal, size=dimension)
            x = dimen[0]
            y = dimen[1]
            for i in range(0, x):
                for j in range(0, y):
                    a[i][j] = round(a[i][j], 2)
                    file.write(str(a[i][j]) + " ")
                file.write("\n")
            file.write("\n")
        file.close()
        

#------------------String Generator-----------------------------------------------------------------------
def StringGenerate(filename, n):
    pass

#------------------Character Generator--------------------------------------------------------------------
def CharacterGenerate(filename, n):
    pass

#------------------Main Function--------------------------------------------------------------------------
def main():
    print("Choose Testcase Type: ")
    print("1. Single Number\n2. Array\n3. String\n4. Characters\n")
    choose = int(input(f"You Choose: "))
    
    fileName = input("Enter the file Name: ") # input the filename along with .txt
    n = int(input("Number of test-cases: "))
    if choose==1:
        dataType = input("What's the data type of number(type int for integer and float for floating point number): ")
        if dataType == "int":
            minVal = int(input("Minimum Value: "))
            maxVal = int(input("Maximum Value: "))
        else:
            minVal = float(input("Minimum Value: "))
            maxVal = float(input("Maximum Value: "))
        SingleNumber(fileName, n, minVal, maxVal, dataType)
    elif choose==2:
        dataType = input("What's the data type of array(type int for integer and float for floating point number): ")
        d = (input("Enter the dimension of the array separated by space: ")).split()
        dimen = []
        for xx in d:
            dimen.append(int(xx))
        if dataType == "int":
            minVal = int(input("Minimum Value: "))
            maxVal = int(input("Maximum Value: "))
        else:
            minVal = float(input("Minimum Value: "))
            maxVal = float(input("Maximum Value: "))
        ArrayGenerate(fileName, n, dimen,minVal, maxVal, dataType)
    elif choose==3:
        StringGenerate(fileName, n)
    else:
        CharacterGenerate(fileName, n)

#-----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#-------------------END-------------------------------------------------------------------------------------