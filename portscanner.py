# import socket
# import sys
# from datetime import datetime

# #defineourtarget
# if len(sys.argv)==2:
#     target=socket.gethostbyname(sys.argv[1]) #translate port name to ip
# else:
#     print("invalid amount of arguments")
#     print("syntax?:python3 scanner.py")
#  #add a pretty banner
# print("_"*50)
# print("scanning target: "+target)
# print("time started "+str(datetime.now()))
# print("_"*50)

# try:
#     for port in range(50,85):
#         s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
#         socket.setdefaulttimeout(1)   
#         result=s.connect_ex((target,port))
#         if result==0:
#             print(f'port {port} is open')
#         s.close()
# except KeyboardInterrupt:
#     print("\n Existing port")
#     sys.exit()
# except socket.gaierror:
#     print("host name could not be resolved")
#     sys.exit()
# except socket.error:
#     print("could now connect to server")
#     sys.exit()

             ############ WEB SCRAPING#####################



import requests
from bs4 import BeautifulSoup
page =requests.get('https://www.pmd.gov.pk/en/')
soup=BeautifulSoup(page.content,'html.parser')














