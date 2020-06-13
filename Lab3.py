#Muhammad Faraz Sohail

c1=0.10 #conatiners holding litre or less
c2=0.25 #containers holding more than litre


coll1=100 #hundred one litre containers
coll2=71 #seventy-one 2 litre containers
coll3=15 #fifteen half litre containers

calc1=c1*(coll1+coll3)
calc2=c2*coll2

total=calc1+calc2

print("\nRefund for containers of litre and less of Coke = $"+str(round(calc1,2))+"\n Refund for containers more than litre of Pepsi = $"+str(round(calc2,2))+"\n\t\t\t\t   Total Refund = $"+str(round(total,2)),end='\n\n')
