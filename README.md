# CUCM_BulkEM_Login
#
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
#  C:\Users\Brian>py CUCM_BulkEM_Login.py Hostname/IP EM-API-Username EM-API-Password myfile.txt
#
# You can pass in the parameters on the command line or edit the
# sys.argv line at the bottom of the script.
