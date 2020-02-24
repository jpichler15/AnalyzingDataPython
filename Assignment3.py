#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:55:11 2020
@author: jarodpichler
"""
print("Hey, we are going to analyze some data from a survey conducted by stackOverflow:")
def task1():
    file = open("stackOverflowData.txt","r")
    Dict={}
    for aline in file:
        values = aline.split("|")
        if(values[1] in Dict):
            Dict[values[1]] = Dict[values[1]]+1
        else:
            if(values[1]!='Country'):
                Dict[values[1]]=1
    sortedDict = sorted(Dict,key = Dict.get,reverse=True)
    print("Here is the number of people that responded from each country:")
    for k in sortedDict:
        print(k,Dict[k])
    file.close()
print("Task 1")
task1()     
print() 
def task2():
    file = open("stackOverflowData.txt","r")
    Dict={}
    for aline in file:
        values = aline.split("|")
        values2 = values[12].split(";")
        values2[len(values2)-1] = values2[len(values2)-1][0:len(values2[len(values2)-1])-1]
        for i in range(len(values2)):
            if(values2[i] in Dict):
                Dict[values2[i]] = Dict[values2[i]]+1
            else:
                Dict[values2[i]]=1
    sortedDict = sorted(Dict,key = Dict.get,reverse=True)
    print("Here is the ten most popular prgramming languages in the survey:")
    count=1
    for k in sortedDict:
        if(count<11):
            print(count,k)
        else:
            break
        count=count+1 
    file.close
print("Task 2")
task2()
print()
def task3():
    file = open("stackOverflowData.txt","r")
    sumMale = 0
    sumFemale = 0
    totalMales = 0
    totalFemales = 0
    avgMale = 0
    avgFemale=0
    count = 0
    for aline in file:
        if(count>0):
            values = aline.split("|")
            if(values[6]=='Male'):
                sumMale = sumMale+float(values[4]) 
                totalMales = totalMales+1
            else:
                sumFemale = sumFemale+float(values[4])
                totalFemales = totalFemales+1
        count = count+1
    avgMale = sumMale/totalMales
    avgFemale = sumFemale/totalFemales
    #fix seperation between $ and number
    print("The average salary for females is: ${}" .format(int(avgFemale)))
    print("The average salary for males is: ${}".format(int(avgMale)))
    file.close
print("Task 3")
task3()
print()
def task4():
    file = open("stackOverflowData.txt","r")
    Dict = {}
    for aline in file:
            values = aline.split("|")
            if(values[1] in Dict):
                Dict[values[1]][0] =  Dict[values[1]][0]+1
                Dict[values[1]][1] =  Dict[values[1]][1]+float(values[4])
                if(float(values[4])>Dict[values[1]][2]):
                    Dict[values[1]][2] =  float(values[4])
            else:
                if(values[1]!='Country'):
                    Dict[values[1]] = [1,float(values[4]),float(values[4])]
    for k in Dict:
        countryMax = Dict[k][2]
        avgSalary = Dict[k][1]/Dict[k][0]
        print(k,"-","AverageSalary =",int(avgSalary),"MaxSalary =",countryMax)
    file.close()
print("Task 4")
print("Here is the average and max salary for each country")
print()
task4()
def task5():
    file = open("stackOverflowData.txt","r")
    Dict={}
    for aline in file:
        values = aline.split("|")
        if(values[5]=="3 - 4 times per week"):
            values2 = values[12].split(";")
            values2[len(values2)-1] = values2[len(values2)-1][0:len(values2[len(values2)-1])-1]   
            for i in range(len(values2)):
                if(values[5] in Dict):
                    Dict[values[5]] = Dict[values[5]]+(values2[i]+' ')
                else:
                     Dict[values[5]]=(values2[i]+' ')
    Dict2 = {}
    values3 = Dict["3 - 4 times per week"].split(" ")
    for i in range(len(values3)):
        if(values3[i] in Dict2):
            Dict2[values3[i]] = Dict2[values3[i]]+1
        else:
            Dict2[values3[i]] = 1
    sortedDict = sorted(Dict2,key = Dict2.get,reverse=True)
    print("The top progrmaming language for people who exercize 3 - 4 times per week is",sortedDict[0])
    file.close()
print()
print("Task 5")#extra credit
task5()
print()
def task6():#extra credit - How often do computer science proffessionals exercise number of people for each amount of exercise
    file = open("stackOverflowData.txt","r")
    Dict={}
    for aline in file:
        values = aline.split("|")
        if(values[5] in Dict):
            Dict[values[5]] = Dict[values[5]]+1
        else:
            if(values[5]!='Exercise'):
                Dict[values[5]]=1
    sortedDict = sorted(Dict,key = Dict.get,reverse=True)
    print("Here is how often computer science proffessionals exercise:")
    for k in sortedDict:
        print(k,"-",Dict[k],"people")
    file.close()
print("Task 6")
task6()     
   


    