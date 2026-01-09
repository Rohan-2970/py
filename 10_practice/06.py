#  Can you change the self-parameter inside a class 
# to something else (say "harry"). Try changing self 
# to "sif" or "harry" and see the effects.


#  there is no prblm 

from random import randint
class Train:

    def __init__(slf,trainNo):
        slf.trainNo= trainNo
        
    def bookticket(self , fro ,to ):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def status(self):
        print(f"Train no: {self.trainNo} is running on time")
        

    def fare(self, fro , to ):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint (222,5555)}")
        
t = Train(34567)
t.bookticket("rampur", "Delhi")
t.status
t.fare("rampur", "Delhi")
