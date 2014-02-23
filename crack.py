import sys
import os
import crypt
def testPass(cryptPass, dictFile):
  salt = cryptPass[0:2]
  for word in dictFile.readlines():
    word = word.strip('\n')
    cryptWord = crypt.crypt(word, salt)
    if (cryptWord == cryptPass):
      print('[+] Found Password: '+word)
      return
  print('[-] Password not found. Encrypted: '+cryptPass)
  return
def checkFileExist(fileName):
  return os.path.isfile(fileName)
def checkFileAccess(fileName):
  return os.access(fileName, os.R_OK)
def main():
  if len(sys.argv) == 3:
    fileList = list()
    fileList.append(sys.argv[1]) #password file
    fileList.append(sys.argv[2]) #dictionary file
    for file in fileList:
      if not checkFileExist(file):
        print('[-] '+str(file)+' does not exist')
        exit(0)
      if not checkFileAccess(file):
        print('[-] '+str(file)+' access denied')
        exit(0)
  else:
    print('[-] Must specify a password file followed by a dictionary file')
    exit(0)
  passFile = open(fileList[0])
  dictFile = open(fileList[1])
  for line in passFile.readlines():
    if ":" in line:
      user = line.split(':')[0]
      cryptPass = line.split(':')[1].strip(' ')
      print("Cracking password for: "+user)
      testPass(cryptPass, dictFile)
if __name__ == "__main__":
  main()
