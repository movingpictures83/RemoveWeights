import sys

def isValue(ch):
    return (ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch == '8' or ch == '9' or ch == '.' or ch == ":")


class RemoveWeightsPlugin:
    def input(self, inputfile):
        infile = open(inputfile, 'r')
        self.data = infile.read()

    def run(self):
        self.finalstr = ""
        signal = False
        for i in range(len(self.data)):
            if (self.data[i] == ':'):
                self.finalstr += self.data[i]
                signal = True
            elif (not signal):
                self.finalstr += self.data[i]
            if (self.data[i] == ',' or self.data[i] == ')'):
                signal = False
                self.finalstr += "1"+self.data[i]

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        outfile.write(self.finalstr)
