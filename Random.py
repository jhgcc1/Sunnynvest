import numpy as np
def rnd(list,size=200):
    if(list[0]=="Beta"):
        return np.random.beta(list[1],list[2],size=size).tolist()
    elif(list[0]=="Gamma"):
        return np.random.gamma(list[1],list[2],size=size).tolist()
    elif(list[0]=="Laplace"):
        return np.random.laplace(list[1],list[2],size=size).tolist()
    elif(list[0]=="Lognormal"):
        return np.random.lognormal(list[1],list[2],size=size).tolist()
    elif(list[0]=="Normal"):
        return np.random.normal(list[1],list[2],size=size).tolist()
    elif(list[0]=="Exponential"):
        return np.random.exponential(list[1],size=size).tolist()
    elif(list[0]=="Weibull"):
        return np.random.weibull(list[1],size=size).tolist()
    elif(list[0]=="Uniform"):
        return np.random.uniform(list[1],list[2],size=size).tolist()
    elif(list[0]=="Fixed value"):
        return [list[1] for x in range(0,size)]

def rndCustom(inputOBJ,size=200):
    resultList=[]
    if(inputOBJ[0]=="Custom probabilities"):
        sizeList=np.random.uniform(0,1,size=size)
        PMF={}
        cumulative=0
        for key in inputOBJ[1]:
            cumulative=cumulative + inputOBJ[1][key]["probability"]
            PMF[key]=cumulative
        for item in sizeList:
            for key in inputOBJ[1]:
                if item<=PMF[key]:
                    resultList.append(inputOBJ[1][key]["value"])
                    break
        return resultList
    else:
        return [inputOBJ[1]["value1"]["value"] for x in range(0,size)]
