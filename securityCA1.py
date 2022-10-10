import csv  # To write to and read from config file
import hashlib
from cgitb import text
from supportFunctions import *
from userOptions import *
from views import *
import getpass




# GLOBALS - SESSION
sessionAvailable = False
session = {'user':"",'userType': "none", 'grantedPriviledges':{ 
    'read_personal': "",
    'read_sickness': "",
    'read_drugPres': "",
    'read_labTestPres': "",
    'write_personal': "",
    'write_sickness': "",
    'write_drugPres': "",
    'write_labTestPres': "",
    'write_configData': ""}}



# Initialize csv file
configFile = "conf.csv"
fields = ["uname", "password", "userType"]
rows = []
def initCsv():
  with open(configFile, 'w') as csvfile:
      # creating a csv writer object
      csvwriter = csv.writer(csvfile)

      # writing the fields
      csvwriter.writerow(fields)


def getPriviledges(userType):
  """Accepts a userType and gives a dictionary of available and NotAvailable priviledges"""

  # Default Priviledges
  priviledgesDict = { 
    'read_personal': "A",
    'read_sickness': "A",
    'read_drugPres': "A",
    'read_labTestPres': "A",
    'write_personal': "NA",
    'write_sickness': "NA",
    'write_drugPres': "NA",
    'write_labTestPres': "NA",
    'write_configData': "NA"}
  
  if(userType == "lab"):
    priviledgesDict["write_configData"]   = "NA"
    priviledgesDict["read_drugPres"]      = "NA"
    priviledgesDict["read_labTestPres"]   = "A"
    priviledgesDict["read_personal"]      = "A"
    priviledgesDict["read_sickness"]      = "NA"
    priviledgesDict["write_drugPres"]     = "NA"
    priviledgesDict["write_labTestPres"]  = "NA"
    priviledgesDict["write_personal"]     = "NA"
    priviledgesDict["write_sickness"]     = "NA"
    return priviledgesDict
  elif(userType == "pharmacy"):
    priviledgesDict["write_configData"]   = "NA"
    priviledgesDict["read_drugPres"]      = "A"
    priviledgesDict["read_labTestPres"]   = "NA"
    priviledgesDict["read_personal"]      = "A"
    priviledgesDict["read_sickness"]      = "NA"
    priviledgesDict["write_drugPres"]     = "NA"
    priviledgesDict["write_labTestPres"]  = "NA"
    priviledgesDict["write_personal"]     = "NA"
    priviledgesDict["write_sickness"]     = "NA"
    return priviledgesDict
  elif(userType == "patient"):
    priviledgesDict["write_configData"]   = "NA"
    priviledgesDict["read_drugPres"]      = "A"
    priviledgesDict["read_labTestPres"]   = "A"
    priviledgesDict["read_personal"]      = "A"
    priviledgesDict["read_sickness"]      = "A"
    priviledgesDict["write_drugPres"]     = "NA"
    priviledgesDict["write_labTestPres"]  = "NA"
    priviledgesDict["write_personal"]     = "A"
    priviledgesDict["write_sickness"]     = "NA"
    return priviledgesDict
  elif(userType == "nurse"):
    priviledgesDict["write_configData"]   = "NA"
    priviledgesDict["read_drugPres"]      = "A"
    priviledgesDict["read_labTestPres"]   = "A"
    priviledgesDict["read_personal"]      = "A"
    priviledgesDict["read_sickness"]      = "A"
    priviledgesDict["write_drugPres"]     = "NA"
    priviledgesDict["write_labTestPres"]  = "NA"
    priviledgesDict["write_personal"]     = "NA"
    priviledgesDict["write_sickness"]     = "A" # Because he/she might need to update in emergencies
    return priviledgesDict
  elif(userType == "doctor"):
    priviledgesDict["write_configData"]   = "NA"
    priviledgesDict["read_drugPres"]      = "A"
    priviledgesDict["read_labTestPres"]   = "A"
    priviledgesDict["read_personal"]      = "A"
    priviledgesDict["read_sickness"]      = "A"
    priviledgesDict["write_drugPres"]     = "A"
    priviledgesDict["write_labTestPres"]  = "A"
    priviledgesDict["write_personal"]     = "A"
    priviledgesDict["write_sickness"]     = "A"
    return priviledgesDict
  elif(userType == "admin"):
    priviledgesDict["write_configData"]   = "A"
    priviledgesDict["read_drugPres"]      = "NA"
    priviledgesDict["read_labTestPres"]   = "NA"
    priviledgesDict["read_personal"]      = "NA"
    priviledgesDict["read_sickness"]      = "NA"
    priviledgesDict["write_drugPres"]     = "NA"
    priviledgesDict["write_labTestPres"]  = "NA"
    priviledgesDict["write_personal"]     = "NA"
    priviledgesDict["write_sickness"]     = "NA"
    return priviledgesDict

# Create user function
def addRecordToConfig(recordDict):
  """Accepts a dictionary of format {uname:"", password:"", userType:""}"""
  # Need to have high priviledges
  if (sessionAvailable == True): #If a user has logged in
    if(session["grantedPriviledges"]["write_configData"] == "A"):
      with open(configFile, 'a') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)

        # writing data rows
        writer.writerow(recordDict)
        print("Write Complete")
      return
    else:
      print ("You DON'T have permission")
      return
  else:
    print("LOGIN first")
    return
  

def createUser():
  username = input("Enter new Username")
  password = input("Enter new password")
  passwordIn = hashlib.md5(passwordIn.encode()).hexdigest()
  userType = input("Enter user Type")

  userDict = {'uname': username, 'password': password, 'userType': userType}
  addRecordToConfig(userDict)

# Login function
def findUser(uname, password):
  """Gets the username and password and input.
    If a user exists, update session variables and return true.
    If no user is available, return false"""
  with open(configFile, 'r') as csvfile:
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
    return False

def logout():
  global sessionAvailable
  global session
  sessionAvailable = False
  session = {'user':"",'userType': "none", 'grantedPriviledges':{}}
  print("Successfully LOGGED OUT\n")


visitFile = "visitDetails.csv"
drugFile = "drugPrescriptions.csv"
labFile = "labTestPrescriptions.csv"
personFile = "personalDetails.csv"

def viewVisitDetails(visitNo):
  rows = []
  with open(visitFile, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
      if line['visitNo'] == visitNo:
        formatString = "visitNo: {}, patientNo: {}, sicknessNo: {}, labNo: {}, drugNo: {}".format(line['visitNo'],line['patientNo'],line['sicknessNo'],line['labNo'],line['drugNo'])
        print(formatString)
        break
  return

def viewPersonalDetails(personalNo):
  rows = []
  with open(drugFile, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
      if line['personalNo'] == personalNo:
        formatString = "personalNo: {}, name: {}, age: {}".format(line['personalNo'],line['name'],line['age'])
        print(formatString)
        break  
  return

def viewSicknessDetails(personNo):
  rows = []
  with open(drugFile, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
      if line['personNo'] == personNo:
        formatString = "drugNo: {}, drugs: {}".format(line['drugNo'],line['drugs'])
        print(formatString)
        break  
  return
  

def viewDrugDetails(drugNo):
  rows = []
  with open(drugFile, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
      if line['drugNo'] == drugNo:
        formatString = "drugNo: {}, drugs: {}".format(line['drugNo'],line['drugs'])
        print(formatString)
        break  
  return

def viewLabDetails(labNo):
  rows = []
  with open(labFile, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
      if line['labNo'] == labNo:
        formatString = "labNo: {}, labs: {}".format(line['labNo'],line['labs'])
        print(formatString)
        break  
  return


if __name__ == "__main__":
  while(True):
    if(sessionAvailable):
      if(session["userType"] == "admin"):
        printAdminHome()
        textIn = input()

        if (textIn == '1'):
          createUser()

        elif(textIn == 'x'):
          logout()

        else:
          print("Enter correct option")
        continue

      elif(session["userType"] == "doctor"):
        printDoctorHome()
        textIn = input()

        if(textIn == "1"):
          #visitNo = int(input("Enter visit Number: "))
          viewVisitDetails(input("Enter visit Number: "))
        elif(textIn == "2"):
          personalNo = (input("Enter PatientID : "))
          viewPersonalDetails(personalNo)
        elif(textIn == "3"):
          personalNo = (input("Enter PatientID : "))
          viewSicknessDetails(personalNo)
        elif(textIn == "5"):
          personalNo = (input("Enter PatientID : "))
          viewDrugDetails(personalNo)
        elif(textIn == "4"):
          personalNo = (input("Enter PatientID : "))
          viewLabDetails(personalNo)
        elif(textIn == "6"):
          personalNo = (input("Enter PatientID : "))
          doctor = session['user']
          prescribeDrug(personalNo, doctor)
        elif(textIn == "7"):
          personalNo = (input("Enter PatientID : "))
          doctor = session['user']
          prescribeLab(personalNo, doctor)
        elif(textIn == "8"):
          personalNo = (input("Enter PatientID : "))
          issuer = session['user']
          editSickness(personalNo, issuer)
        elif(textIn == "x"):
          logout()
        else:
          print("Invalid input")
          continue
        
      elif(session["userType"] == "patient"):
        printPatientHome()
        textIn = input()

        if (textIn == "1"):
          viewPersonalDetails(session['user'])
        elif (textIn == "2"):
          viewSicknessDetails(session['user'])
        elif (textIn == "3"):
          viewLabDetails(session['user'])
        elif (textIn == "4"):
          viewDrugDetails(session['user'])
        elif (textIn == "x"):
          logout()
        else:
          print("Invalid input")
          continue

      elif(session["userType"] == "nurse"):
        printNurseHome()
        textIn = input()

        if (textIn == "1"):
          viewPersonalDetails(session['user'])
        elif (textIn == "2"):
          viewSicknessDetails(session['user'])
        elif (textIn == "3"):
          viewLabDetails(session['user'])
        elif (textIn == "4"):
          viewDrugDetails(session['user'])
        elif (textIn == "5"):
          personalNo = (input("Enter PatientID : "))
          issuer = session['user']
          editSickness(personalNo, issuer)
        elif (textIn == "x"):
          logout()
        else:
          print("Invalid input")
          continue

      elif(session["userType"] == "lab"):
        printLabHome()
        textIn = input()

        if (textIn == "1"):
          viewPersonalDetails(session['user'])
        elif (textIn == "2"):
          viewLabDetails(session['user'])
        elif (textIn == "3"):
          markLabIssued(input("Enter Lab prescription No: "))
        elif (textIn == "x"):
          logout()
        else:
          print("Invalid input")
          continue

      elif(session["userType"] == "pharmacy"):
        printPharmacyHome()
        textIn = input()

        if (textIn == "1"):
          viewPersonalDetails(session['user'])
        elif (textIn == "2"):
          viewDrugDetails(session['user'])
        elif (textIn == "3"):
          markDrugIssued(input("Enter drug prescription No: "))
        elif (textIn == "x"):
          logout()
        else:
          print("Invalid input")
          continue

    else:
      #Login user
      usernameIn = input("Input username: ")
      passwordIn = getpass.getpass('Password:')
      passwordIn = hashlib.md5(passwordIn.encode()).hexdigest()

      isUserAvailable  = findUser(usernameIn, passwordIn)
      if (isUserAvailable == False):
        # User session not created
        continue
      else:
        # UserSession initiated
        continue

