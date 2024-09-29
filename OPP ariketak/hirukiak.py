class Hirukia:
    def __init__(self,a,b,c):
        self.setAldeak(a,b,c)
    
    def setAldeak(self,a,b,c):
        #koprobatu danak positiboak eta direla
        if a<=0 or b<=0 or c<=0:
            raise ValueError('Aldeak ezin dira 0 edo 0 baino TXIKIAGOAK izan')
        #konprobatu danak int edo float direal

        if not (isinstance(a,(float,int)) and isinstance(b,(float,int)) and isinstance(c,(float,int))):
            raise ValueError('Aldeak zenbaki errealak iza behar dira')
        
        #konprobatu alde bakoitza beste bien batura baino txikiagoa izan behar du
        if a+b<=c or a+c<=b or c+b<=a:
            raise ValueError('alde bakitza beste bien arteko batura baino txikiagoa izan behar du, sartutako zenbakiek ez dute baldintza betetzen')
        
        #baldintza guztiak ez badira betetzen, datuak edefinitu
        self.a=a
        self.b=b
        self.c=c
    
    def aldeHandiena(self):
        max_aldea=max(self.c,self.a,self.b)
        print(f'Hirukiaren alderik handiena:{max_aldea} ')
    
    def hiruki_mota(self):
        if self.a==self.b==self.c:
            print('Sortutako hirukia aldeberdina da')
        elif self.a==self.b or self.a==self.c or self.b==self.c:
            print('Sortutako hirukia isoszelea da')
        else:
            print('Sortutako hirukia eskalenoa da')
            