def printAdminHome():
  """Admin does not need access to patient details or any medical information"""
  print("\nADMIN HOME\n")
  print("""
  1\t Create User
  x\t Logout""")
  return

def printDoctorHome():
  """Doctor has full access to medical information"""
  print("\nDOCTOR HOME\n")
  print("""
  1\t View Visit Details
  2\t View Personal Details
  3\t View Sickness Details
  4\t View Lab Test Prescriptions
  5\t View Drug Prescriptions

  6\t Issue Lab Test Prescriptions
  7\t Issue Drug Prescriptions
  8\t Edit Sickness Details
  x\t Logout""")
  return

def printPatientHome():
  """Patient can view all his information"""
  print("\nPATIENT HOME\n")
  print("""
  1\t View Personal Details
  2\t View Sickness Details
  3\t View Lab Test Prescriptions
  4\t View Drug Prescriptions
  x\t Logout""")
  return

def printNurseHome():
  """Nurse can view all patients information"""
  print("\nNURSE HOME\n")
  print("""
  1\t View Personal Details
  2\t View Sickness Details
  3\t View Lab Test Prescriptions
  4\t View Drug Prescriptions

  5\t Update sickness
  x\t Logout""")
  return


def printLabHome():
  print("\nLABORATORY HOME\n")
  print("""
  1\t View Personal Details
  2\t View Lab Test Prescriptions
  3\t Mark prescription as issued
  x\t Logout""")
  return

def printPharmacyHome():
  print("\nPHARMACY HOME\n")
  print("""
  1\t View Personal Details
  2\t View Drug Prescriptions
  3\t Mark prescription as issued
  x\t Logout""")
  return