
n1 = int ( input (" Enter your first number : "))
n2 = int (input( " Enter your second number : "))
sym = input ( " Input your symbol : ")
if sym =="+":
    r = n1+n2
elif sym == "-":
    r = n1-n2
elif sym == "*":
    r = n1*n2
elif sym =="/":
    r = n1/n2
else:
    print( " Invalid Operator.") 
print ( f" Result : {n1} {sym} {n2} = {r}")   
     
while 1:       
  choice = input ( " Do you to work with another number : ")
  if choice == "yes":      
      n = int ( input(" Enter your new number : "))
      s = input ( " Input your Symbol : ")
      if s =="+":
          re = r+n
      elif s == "-":
          re = r-n
      elif s == "*":
          re = r*n
      elif s =="/":
          re = r/n
      else:
          print( " Invalid Operator.")            
      print ( f" Result : {r} {s} {n} = {re}")    
      r = re
  else:
      print ( " Qutting!")
      break
       
       
    








































