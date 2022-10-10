import csv
visitFile = "visitDetails.csv"
drugFile = "drugPrescriptions.csv"
labFile = "labTestPrescriptions.csv"
personFile = "personalDetails.csv"
# VIEW
"""with open(configFile, 'r') as csvfile:
   # creating a csv reader object
   csvreader = csv.reader(csvfile)
   # extracting field names through first row
   fields = next(csvreader)
   # extracting each data row one by one
   for row in csvreader:
     rows.append(row)
   # Check if the user exist
   for record in rows:
     if (record[0] == uname and record[1] == password):
       #Getting priviledged
       priviledges = getPriviledges(record[2])
       global sessionAvailable
       global session
       sessionAvailable = True        
       session = {'user': uname, 'userType': record[2], 'grantedPriviledges': priviledges}
       return True
     else:
       continue
   return False"""




def editVisit(personalNo)

# WRITE
def prescribeDrug(personalNo, doctor):
  return

def prescribeLab(personalNo, doctor):
  return

def editSickness(personalNo, issuer):
  return

def markLabIssued(labNo):
  return

def markDrugIssued(drugNo):
  return