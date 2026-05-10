class state9:
    def __init__(self,live):
        self.live=int(float(float(live)/11.1112))
        if self.live>8:
            self.live=8
    
    def lost(self):
            self.live=self.live-1
            if self.live<1:
               self.live=0


    def report(self):
        print("live : "+str(int(self.live * 11.1112))+" % ")


a=state9(100)
for b in range(9):
    a.report()
    a.lost()
