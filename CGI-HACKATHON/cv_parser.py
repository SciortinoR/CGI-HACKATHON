'''
Created on May 26, 2018

@author: Roberto Sciortino
'''
import os
import re
from applicant import CV
import operator
#import codecs
import sys

#Determining weights for each category of skills
#Set to 1 each for reference
EDU = 1
LANG = 1
SOFT = 1
COMM = 1
TECH = 1

#using command line to set value of skill category they want to search for
if int(sys.argv[2]) == 0 or int(sys.argv[3]) == 0:
    EDU = 1
    LANG = 1
    COMM = 1
    SOFT = 1
    TECH = 1
elif int(sys.argv[2])==1:
    LANG = 5
elif int(sys.argv[2])==2:
    SOFT = 5
elif int(sys.argv[2]) == 3:
    TECH = 5
elif int(sys.argv[2]) == 4:
    EDU = 5
elif int(sys.argv[2]) ==5:
    COMM = 5
    
if int(sys.argv[3])==1:
    LANG = 3
elif int(sys.argv[3])==2:
    SOFT = 3
elif int(sys.argv[3]) == 3:
    TECH = 3
elif int(sys.argv[3]) == 4:
    EDU = 3
elif int(sys.argv[3]) ==5:
    COMM = 3
    
#reading hardkills/softskills txts and splitting based on new line and spaces
hardskills = open(r"C:\Users\rober\Desktop\MY FILES\PROJECTS\CGI HACKATHON\hardskills.txt").read()
hardskills = re.split('[ "\n]',hardskills)
softskills = open(r"C:\Users\rober\Desktop\MY FILES\PROJECTS\CGI HACKATHON\softskills.txt").read()
softskills = re.split('[ "\n"]',softskills)

#creating path for opening cvs
#Path = r"C:\\Users\\rober\\Desktop\\MY FILES\\PROJECTS\\CGI HACKATHON\\cv\\"
Path = sys.argv[1]
filelist = os.listdir(Path)

#seperating hardskills into categories
for i in hardskills:
    if i == "=":
        languages = hardskills[0:hardskills.index(i)]
        soft = hardskills[hardskills.index(i)+1:]
        for k in soft:
            if k == "=":
                software = soft[0:soft.index(k)]
                tech = soft[soft.index(k)+1:]
hard = [languages, software, tech]                  #hard skills list of lists

#seperating softskills into categories
for i in softskills:
    if i == "=":
        education = softskills[0:softskills.index(i)]
        personal = softskills[softskills.index(i)+1:]
soft = [education,personal]                         #soft skills list of lists

#creating dict of CV objects
Dict = {}
for i in filelist:
    Dict[i] = CV(i)

#looping through each CV Object and comparing words from cv with words from keyword lists
for k, value in Dict.items():
    with open(Path + value.address, encoding = "utf-8") as f:
        for line in f:
            line = line.lower()
            myvar = re.split('[\' ;:.,*()_]',line)
            for word in myvar:
                #checks softskill education list
                for text in soft[0]:
                    if text==word:
                        for i in value.keywordList:
                            if i==text:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(text)
                                value.eduscore += EDU
                                break
                #checks softskills communication
                for text in soft[1]:
                    if text==word:
                        for i in value.keywordList:
                            if i==text:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(text)
                                value.commscore += COMM
                                break
                #checks hardskills language 
                for text in hard[0]:
                    if text==word:
                        for i in value.keywordList:
                            if i==text:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(text)
                                value.langscore += LANG
                #checks hardskills software list
                for text in hard[1]:
                    if text==word:
                        for i in value.keywordList:
                            if i==text:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(text)
                                value.softwarescore += SOFT
                #checks hardskills tech list
                for text in hard[2]:
                    if text==word:
                        for i in value.keywordList:
                            if i==text:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(text)
                                value.techscore += TECH
        f.close()
        
    #modifies final score values
    value.keywordList.pop(0)        #removes first empty string from keyword list
    value.softscore = value.eduscore + value.commscore
    value.hardscore = value.langscore + value.softwarescore + value.techscore
    value.totalscore = value.softscore + value.hardscore

#writing results to txt file
results = open(r"C:\Users\rober\Desktop\MY FILES\PROJECTS\CGI HACKATHON\results.txt", "w")
for i, value in Dict.items():
    results.write('%s%s%s\n' % (i, " Hard Score: ", value.hardscore))
    results.write('%s%s%s\n' % (i, " Soft Score: ", value.softscore))
    results.write('%s%s%s\n' % (i, " Total Score: ", value.totalscore))
    results.write('%s%s\n' % ("Keywords: ",value.keywordList))
    results.write('\n')

#lists candidates in descending order for best candidates
results.write("Top Candidates: ")
results.write('\n')
for score in (sorted(Dict.values(), key=operator.attrgetter('totalscore'), reverse = True)):
    results.write('%s%s%s%s\n' % (score.address, "-", "Total Score: ", score.totalscore))

results.close()
print("Process Completed")

'''FOLLOWING CODE WAS A DIFFERENT ALGORITHM TESTED FOR LOOPING THROUGH ALL CV'S AND KEYWORD FILES
for a,b,c,d,e in zip(hard[0],hard[1],hard[2],soft[0],soft[1]):
                    if a == word:
                        for i in value.keywordList:
                            if i==a:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(a)
                                value.langscore += LANG
                                break
                    elif b == word:
                        for i in value.keywordList:
                            if i==b:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(b)
                                value.softwarescore += SOFT
                                break
                    elif c == word:
                        for i in value.keywordList:
                            if i==c:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(c)
                                value.techscore += TECH
                                break
                    elif d == word:
                        for i in value.keywordList:
                            if i==b:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(d)
                                value.eduscore += EDU
                                break
                    elif e == word:
                        for i in value.keywordList:
                            if i==e:
                                break
                            if i==value.keywordList[-1]:
                                value.keywordList.append(e)
                                value.commscore += COMM
                                break'''