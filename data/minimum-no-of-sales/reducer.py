s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 9999999999999999999

for line in s:
  data = line.strip().split('\t')
  category, amount = data

  if category != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = category 
    thisValue = 9999999999999999999
  
  # apply the aggregation function
  thisValue = min(thisValue,float(amount))

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
