import hashlib
import base64


test_passwords = ["Av1d-Reader","L0rd-of-the-Books","Password-123"]
salts = ["961804260","0169402691","402375329"]

for i in range(3):  
  t_sha = hashlib.sha256()
  t_sha.update((test_passwords[i]+salts[i]).encode("utf-8"))
  hashed_password =  base64.urlsafe_b64encode(t_sha.digest()).decode("utf-8")
  print(i,":"+salts[i]+"."+hashed_password)