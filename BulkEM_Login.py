# This program will login device profiles in bulk using a CSV file.
#
# You must provide a CSV file listing the device name, user profile,
# and end user alias.
# 
# The CUCM user must have this access control group assigned:
# Standard EM Authentication Proxy Rights
#
# Sample CSV format:
# devicename,profile,user
# SEP00AABBCCDDEE,EM_bmeade,bmeade
#
# Sample SQL statement to get devicename, profile, and user from another cluster:
# select d.name as devicename,p.name as profile,eu.userid as user from extensionmobilitydynamic emd left join device d on emd.fkdevice=d.pkid left join device p on emd.fkdevice_currentloginprofile=p.pkid left join enduser eu on emd.fkenduser=eu.pkid
#
# Install Python 3.7 and choose to install the Python Py launcher
# Then install one module
#  C:\Users\Brian>py -m pip install requests
#
# Then run the program BulkEM_Login.py
#  C:\Users\Brian>py BulkEM_Login.py Hostname/IP EM-API-Username EM-API-Password myfile.txt
#
# You can pass in the parameters on the command line or edit the
# sys.argv line at the bottom of the script.
#
import requests
import csv
import sys
import os


def main(argv):
    cucm_server = ""
    appEmProxyUser = ""
    appPw = ""
    csv_target = ""

    try:
        cucm_server = sys.argv[1]
        appEmProxyUser = sys.argv[2]
        appPw = sys.argv[3]
        csv_target = sys.argv[4]
    except:
        print('Please enter hostname/IP Address, username, password, and the CSV file')
        sys.exit()

    uri = "http://" + cucm_server + ":8080/emservice/EMServiceServlet"
    headers = {"Content-Type":"application/x-www-form-urlencoded"}

    with open(csv_target, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            device = row['devicename']
            profile = row['profile']
            emuser = row['user']
            print("Attempting to login to device ",device," with profile ",profile," and emuser ",emuser)
            parameters = "<request>"
            parameters += "<appInfo><appID>" + appEmProxyUser + "</appID><appCertificate>" + appPw + "</appCertificate></appInfo>"
            parameters += "<login><deviceName>" + device + "</deviceName><userID>" + emuser + "</userID><deviceProfile>" + profile + "</deviceProfile>"
            parameters += "<exclusiveDuration><indefinite></indefinite></exclusiveDuration></login>"
            parameters += "</request>"
            r = requests.post(uri,data={"xml":parameters},headers=headers)
            print(r.text)

if __name__ == "__main__":
   #Replace the below values or pass the commands through the command-line and remove the below line
   sys.argv = ["BulkEM_Login.py", "192.168.1.1", "admin", "mypassword", "myfile.txt"]
   main(sys.argv[1:])
