class sample:
    def __init__(self):
        self.l=[]
    def read_from_file(self,filename):
        f1=open(filename,'r')
        return f1.read()
    def write_to_file(self,filename,content):
        f2=open(filename,'a')
        f2.write(str(content)+'\n')
    def actual_primes(self,func):
        def inner(n):
            self.l=[]
            li=func(n)
            for i in li:
                c=0
                for j in range(2,i+1):
                    if i%j==0:
                        c+=1
                if c==1:
                    self.l.append(i)
            return self.l
        return inner
    def all_primes(self,n):
        y=[]
        for i in range(1,n+1):
            y.append(i)
        return y
    def test_primes(self,n):
        self.all_primes=self.actual_primes(self.all_primes)
        e=self.all_primes(n)
        d={}
        d['primes']=e
        self.write_to_file('output1.txt', d)
    def printingfinalstatement(self):
        q='all primes are entered into output file'
        yield q
class child(sample):
    def all_primes(self,n):
        y=[]
        for i in range(1,n+1):
            c=0
            for j in range(2,i+1):
                if i%j==0:
                    c+=1
            if c==1:
                y.append(i)
        return y
def main():
    x=int(input("Enter a number: "))
    ob=sample()
    ob.test_primes(x)
    r = ob.printingfinalstatement()
    try:
        print(r.__next__())
    except StopIteration:
        print("No more primes")
    k = child()
    p = k.all_primes(x)
    print(p)


if __name__=='__main__':
    main()


