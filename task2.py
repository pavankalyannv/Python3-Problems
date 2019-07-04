# We've to enter a string combination of numbers and char's , the output should contain only numbers with sign
string='-1235dddd-2'
for i in string:
    if(i=='-'):
      print(i,end="")
    else:
      if(i.isdigit()):
        print(i,end="")
  
