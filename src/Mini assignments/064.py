import time

userinfo = {}
phone = input("What is your phone number ")
userinfo["phone"] = phone
cellphone = input("What is your cellphone number? ")
userinfo["cellphone"] = cellphone
fax = input("What is your fax number? ")
userinfo["fax"] = fax
print(userinfo)
time.sleep(5)
print("What are you a doctor or something??? We don't use faxes anymore LOL ")
del userinfo["fax"]
print(userinfo)
