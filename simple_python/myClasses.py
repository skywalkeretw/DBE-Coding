from cmath import exp
from unittest import expectedFailure
from venv import create


class filectr:
    def __init__(self, filename):
        self.filename = filename

    def createFile(self):
        print("Creating File:", self.filename)
        try:
            open(self.filename, "x")
            print("FILE", self.filename, "has been created")
        except FileExistsError:
            print("FILE", self.filename, "Already exists")

    def writeFile(self, content):
        print("Writting:", content , "to", self.filename)
        f = open(self.filename, "w")
        f.write(content)
        f.close()

    def readFile(self):
        print("Reading from:",  self.filename)
        f = open(self.filename, "r")
        data = f.read()
        f.close()
        return data
   
