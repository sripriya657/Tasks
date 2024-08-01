class Processor:
    def __init__(self, l,x):
        self.l = l
        self.x = x

    def counting_occurrences(self,list):
        d={}
        for i in list:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        return d
    def divide_by_number(self):
        try:
            while True:
                for i in self.l:
                    yield i/self.x
                break
        except ZeroDivisionError:
            print("Division by zero")

    def read_from_file(self,filename):
        f1=open(filename,'r')
        return f1.read()
    def write_to_file(self,filename,content):
        f2=open(filename,'a')
        f2.write(str(content)+'\n')
    def printingfinalstatement(self):
        q='task completed'
        yield q
    def process(self):
        self.write_to_file('input.txt',self.l)
        self.write_to_file('input.txt',self.x)
        d=self.counting_occurrences(self.l)
        self.write_to_file('output.txt',d)
        div_elements = list(self.divide_by_number())
        self.write_to_file('output.txt', div_elements)
        r=self.printingfinalstatement()
        print(r.__next__())

def main():
    l=list(map(int,input().split()))
    x=int(input())
    p=Processor(l,x)
    p.process()
if __name__=='__main__':
    main()







