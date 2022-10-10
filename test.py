import hashlib
"""Tha,040b7cf4a55014e185813e0644502ea9,patient
who,01cfcd4f6b8770febfb40cb906715822,doctor
nursy,827ccb0eea8a706c4c34a16891f84e7b,nurse
dococ,6531401f9a6807306651b87e44c05751,lab
ice,495bf9840649ee1ec953d99f8e769889,pharmacy"""
#Tha
print(hashlib.md5(b"12345").hexdigest())
print(hashlib.md5(b"54321").hexdigest()) # who
print(hashlib.md5(b"23456").hexdigest()) #nursy
print(hashlib.md5(b"65432").hexdigest()) #dococ
print(hashlib.md5(b"strawberry").hexdigest()) #ice
print(hashlib.md5(b"lorder").hexdigest()) #lord