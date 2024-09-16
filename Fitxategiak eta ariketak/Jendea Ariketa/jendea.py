file = open( "jendea.txt" , mode="r")

allLines = file.readlines()
print(allLines)
list_of_all_list = []
for x in allLines:

   list_split = x.split(';')

   for element in list_split:
     dict= {
         "id" : list_split[0],
         "izena" : list_split[1],
         "abizena": list_split[2],
         "jaiotze data" : list_split[3]
      }
   list_of_all_list.append(dict)

file.close()

print(list_of_all_list)