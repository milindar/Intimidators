s = open("02.txt","r")
r = open("final.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  segment, sales = data

  if segment != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = segment 
    thisValue = 0.0
  
  # apply the aggregation function

  thisValue += 1

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
