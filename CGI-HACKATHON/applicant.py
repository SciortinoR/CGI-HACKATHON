'''
Created on May 26, 2018

@author: Roberto Sciortino
'''
#class cv for cv parser
class CV:
    def __init__(self, name):
        self.address = name
        self.keywordList = [""]
        self.softscore = 0
        self.eduscore = 0
        self.langscore = 0
        self.commscore = 0
        self.softwarescore = 0
        self.techscore = 0
        self.hardscore = 0
        self.totalscore = 0
        
