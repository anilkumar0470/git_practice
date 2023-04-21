# # #n=input("enter value")
# # #if n==1:
# #         #print("n is 1")
# # #elif n==2:
# #         #print ("n is 2")
# # #elif n==3:
# #         #print ("n is 3")
# # #else:
# #         #print ("a is not in the range")
# # #print("hi this is practice for elseis")
# # """
# # a=input("enter a value")
# # if a<=10:
# #         print("a value is below 10")
# # elif a>=10 & a<=20:
# #         print("a value is above 10 and below 20")
# # else:
# #         print("a is out of range")
# # """
# #
# # #a=input("enter a value")
# # #b=input("enter b value")
# # #c=input("enter c value")
# # #if a<b :
# #         #if b<c :
# #                 #print ("c is bigger")
# #         #else:
# #                 #print ("b is bigger")
# # #else:
# #         #if a<c:
# #                 #print ("c is bigger")
# #         #else :
# #                 #print ("a is bigger")
# #
# #
# # """for line in range(1,11):
# #     for table in range(1,11):
# #         print line * table, '\t',
# #     print
# # """
# # global std_list
# # std_list = []
# #
# #
# # def student_register():
# #
# #     f = True
# #     while f:
# #         name = raw_input ("enter the name of student:")
# #         regNo = raw_input ("enter the roll number:")
# #         address = raw_input ("enter the address:")
# #         section = raw_input ("enter the class:")
# #         mobile = raw_input ("enter the mobile number:")
# #         dob = raw_input ("enter the date of bitrh :")
# #         fd = open("std_details.txt","w")
# #         p = "="
# #         z = p *50
# #         fd.write(z)
# #         fd.write("\n")
# #         fd.write("        student details      ")
# #         fd.write("\n")
# #         print p
# #         fd.write("\n")
# #         fd.write(z)
# #
# #         fd.write("\n")
# #         fd.write("\t")
# #         #fd.write("SNO \t")
# #         fd.write("Name \t \t")
# #         fd.write("Location \t \t")
# #         fd.write("Mobile \t \t")
# #         fd.write("DOB \t \t")
# #         fd.write("\n")
# #
# #         fd.write(name)
# #         fd.write("\t\t")
# #         fd.write(address)
# #         fd.write("\t\t")
# #         fd.write(mobile)
# #         fd.write("\t\t")
# #         fd.write(dob)
# #         fd.write("\t\t")
# #         std_list.append({'name':name,'reg':regNo,'address':address,'section':section,'contact':mobile,'dob':dob})
# #         fd.writelines(std_list)
# #         ent=raw_input("enter if you want student or not if yes or no?")
# #         if ent in ['yes','y']:
# #             f=True
# #         else:
# #             f=False
# #
# # student_register()
#
#
# #
# # import requests
# #
# # url = "https://service-uat.upstox.com/portfolio/historical-holding/graph?interval=week"
# #
# # payload={}
# # headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIyMDEyMjUyMCIsImp0aSI6IjQ2V3V3cGZVSWphM192SjFWQzRCQ1F6eEdmWSIsImlhdCI6MTY0ODQ2ODk0MywiZXhwIjoxNjY0MDIwOTQzLCJpc3MiOiJsb2dpbi1zZXJ2aWNlIiwic2NvcGUiOltdLCJjbGllbnRfaWQiOiJPRkxYLWFiY2RrbXBYVU9lUUNJUzBKeGtBczVNIiwia2V5X2lkIjoiaWR0MTY0MTAxODYwMDc0NyIsInJlZnJlc2hfdG9rZW5faWQiOiJrY0p4cFBqQk1qR0g0ZWV3TVNGb3paZmgta3ciLCJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwicm9sZSI6IkNVU1RPTUVSIiwidXNlcl90eXBlIjoiQ1VTVE9NRVIiLCJ1c2VyX2lkIjoiQUEwMDA1IiwidmVyc2lvbiI6IlYyIn0.Sqmn36BPMLBzL9Iwge6h6WmkTcVvbfZ9--8OwOv9Pz1PwtkFWbz2Yi09ldkE4lFx0dzKt0AdPl326MwfDCa4o6Qlta7CAKJ4ZWYv4lYnxgJKTg_EG8169k5RquzosYtLjJVvVlDmakwsV0lINv_Hkyu8M1QOZxblhzGgNUbaeSGWQ-k3_TmWDyyV2tGj0LEseV3hAtmmbV7D6GWsfDRS1TstxQcisYac4vZwMN9BFc_P0WqUwtKv_vEIs9_R53V_XnuDKsclHZzjAGQiUWoaqvMOXUrHll4-YcNx_1EKyWeWeXhXjRI0kc3n2qcKxCiyjyWDj1fVNn6WA_xP1bFCHw','Cookie': '_cfuvid=ME0HVFGQIeTLvpwpxSIDwZNWUm.05UUNJaj4eVmXcW0-1655109651936-0-604800000'}
# # response = requests.request("GET", url, headers=headers, data=payload)
# # print(response.text)
#
# import time
#
# # t = 5
# # while True:
# #     if t:
# #         print("waiting for {} second(s)!".format(t))
# #         time.sleep(1)
# #         t = t - 1
# #     else:
# #         break
# # print ('tasks done, now sleeping for 10 seconds')
# # for i in range(10,0,-1):
# #     time.sleep(1)
# #     print (i)
#
#
# # import sys
# # import time
# # for i in range(10,0,-1):
# #     sys.stdout.write(str(i)+' ')
# #     sys.stdout.flush()
# #     time.sleep(1)
#
#
# import imaplib
# import email
# from email.header import decode_header
#
# username = 'contact.jagadeeshforpython@gmail.com'
# password = 'Login@123'
#
#
# def get_otp():
#     otp = []
#
#     # create an IMAP4 class with SSL
#     imap = imaplib.IMAP4_SSL("imap.gmail.com")
#     # authenticate
#     imap.login(username, password)
#
#     status, messages = imap.select("Inbox")
#     # number of top emails to fetch
#     N = 1
#     # total number of emails
#     messages = int(messages[0])
#
#     for i in range(messages, messages - N, -1):
#         # fetch the email message by ID
#         res, msg = imap.fetch(str(i), "(RFC822)")
#         for response in msg:
#             if isinstance(response, tuple):
#                 # parse a bytes email into a message object
#                 msg = email.message_from_bytes(response[1])
#                 if msg.is_multipart():
#                     # iterate over email parts
#                     for part in msg.walk():
#                         # extract content type of email
#                         content_type = part.get_content_type()
#                         content_disposition = str(part.get("Content-Disposition"))
#                         try:
#                             # get the email body
#                             body = part.get_payload(decode=True).decode()
#                         except:
#                             pass
#                         if content_type == "text/plain" and "attachment" not in content_disposition:
#                             # print text/plain emails and skip attachments
#
#                             # depending on your where your OTP is in the email, you will have to modify the string split method
#                             body = body.split('Your login OTP is')[1]
#                             body = body.split('In case if you have not tried to login')[0]
#                             otp.append(int(body))
#
#     imap.close()
#     imap.logout()
#     return otp
#
# # otp = get_otp()
# # print(otp)
#
# import poplib
# import string, random
# import StringIO, rfc822
# import logging
#
# SERVER = "pop.gmail.com"
# USER  = "contact.jagadeeshforpython@gmail.com"
# PASSWORD = "Login@123"
#
# # connect to server
# logging.debug('connecting to ' + SERVER)
# server = poplib.POP3_SSL(SERVER)
# #server = poplib.POP3(SERVER)
#
# # login
# logging.debug('logging in')
# server.user(USER)
# server.pass_(PASSWORD)
#
# # list items on server
# logging.debug('listing emails')
# resp, items, octets = server.list()
#
# # download the first message in the list
# id, size = string.split(items[0])
# resp, text, octets = server.retr(id)
#
# # convert list to Message object
# text = string.join(text, "\n")
# file = StringIO.StringIO(text)
# message = rfc822.Message(file)
#
# # output message
# print(message['From']),
# print(message['Subject']),
# print(message['Date']),
# #print(message.fp.read())

# out = ["good"]
# import pdb
# # pdb.set_trace()
# last = [i for i in range(5) if out == "good"]
#
# print(last)

# l1 = [1,2,3,4,5]
# l2 = [4,5,6,7,4]
#
# for i in l1[:]:
#     # print(l1[:])
#     if i in l2:
#         for j in range(l1.count(i)):
#             l1.remove(i)
#         for k in range(l2.count(i)):
#             l2.remove(i)
# #
# # print(l1)
# # print(l2)
# number = 1
# l11 = [1, 2, 3, 1, 4, 5]
# for ind in range(len(l11)):
#     if number == l11[ind]:
#         print(ind)



# import requests
# new_dict = {}
# for i in range(1,3):
#     response = requests.get("https://jsonmock.hackerrank.com/api/article_users?page={}".format(i))
#     page_out = response.json()["data"]
#     print(page_out)
#     for entry in page_out:
#         if entry["username"] and entry["submission_count"]:
#             new_dict.update({entry["username"]: entry["submission_count"]})
# print(new_dict)
#
# count = 10
# new_list = []
# for key,value in new_dict.items():
#     if value >= count:
#         new_list.append(key)
# print(new_list)

import requests

url = "https://api.upstox.com/live/profile/balance"

payload={}
headers = {
  'Authorization': 'Bearer B-5a40d282aa1de2a56624baccf8c50dc0a5dbf450',
  'x-api-key': 'kVaqLtiSNPgVfSrXhUKJa2A5HRizcDf3rxf1KCh3',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)






# out = list(new_dict.values())
# out.sort(reverse=True)
#
# new_list = []
# for l in range(2):
#     for key, value in new_dict.items():
#         if out[l] == value:
#             new_list.append(key)




# import requests
#
# url = "https://api.upstox.com/live/profile/balance"
#
# payload={}
# headers = {
#   'Authorization': 'Bearer B-bfb8652e5a8e4103949e0bd75571cfa2e49eefc5',
#   'x-api-key': 'kVaqLtiSNPgVfSrXhUKJa2A5HRizcDf3rxf1KCh3',
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

list1 = ["a", "Z", "o", "k", "e", "A","x", "L"]
# list1.sort()
# print(list1)
print(ord("z"))
for i in range(len(list1)):
  for j in range(i+1, len(list1)):
    if ord(list1[i]) > ord(list1[j]):
      list1[i], list1[j] = list1[j], list1[i]
print(list1)