n=22 # publicly known
g=42 # publicly known
x=int (input ("Enter the key Person 1 knows : \n")) # only A knows this
y=int (input ("\nEnter the key Person 2 knows : \n") ) # only B knows this
A = (g**x)%n #sends
Bcomputes = (A**y)%n # computes
B= (g**y)%n #sends
Acomputes= (B**x)%n #computed
print( "Person 1 sends ",A)
print ("Person 2 computes ", Bcomputes )
print ("Person 2 sends ", B)
print ("Person 1 computes ", Acomputes)
print ("In theory both should have ", (g**(x*y))%n) # same result
