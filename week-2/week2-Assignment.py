from asyncio.windows_events import INFINITE

#要求一
def calculate(min, max, step):
    list=[*range(min,max+1,step)] 
    print(sum(list))

calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

#要求二
def avg(data):
    sum=0
    number=0
    average=0
    for i in range(len(data["employees"])):
        if data["employees"][i]["manager"]==False:
            sum=sum+data["employees"][i]["salary"]
            number=number+1 
            average=sum/number
    print(average)

avg(
    {"employees":
    [
    {"name":"John","salary":30000,"manager":False},
    {"name":"Bob","salary":60000,"manager":True},
    {"name":"Jenny","salary":50000,"manager":False},
    {"name":"Tony","salary":40000,"manager":False}
    ]
    }
)

# 要求三
def func(a):
    return lambda x,y: print(a+(x*y))
    
func(2)(3,4)
func(5)(1,-5)
func(-3)(2,9)
       

# 要求四
def maxProduct(list):
    result=-INFINITE

    for i in range(len(list)):    
        for j in range(i+1, len(list)):
            product=list[i]*list[j]
            if product>result:
                result=product
    print(result)


maxProduct([5,20,2,6])
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

# 要求五
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum=nums[i]+nums[j]
            if sum==target:
                return[i,j]
result=twoSum([2,11,7,15],9)
print(result)

#要求六
def maxZeros(nums):
    result=0
    zerolist=[]
    for i in range(len(nums)):
        if nums[i]==0:
            result=result+1
        else:
            zerolist.append(result)
            result=0
    
    zerolist.append(result)
    print(max(zerolist))

maxZeros([0,1,0,0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) 
maxZeros([1, 1, 1, 1, 1]) 
maxZeros([0, 0, 0, 1, 1]) 

