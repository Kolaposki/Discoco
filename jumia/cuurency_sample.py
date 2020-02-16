"""
    name='cuurency_sample',
    project='discoco'
    date='2/13/2020',
    author='Oshodi Kolapo',
"""

# Python program to convert the currency of one country to that of another country

# Import the modules needed
import requests

# 364.252164 , 365.03 ,  366.503242 , 366.11 , 355 ,

'''
access_key = '1bdeb1d4655b743e722f55054fd4aa44'
url = str('http://data.fixer.io/api/latest?access_key=' + access_key)
data = requests.get(url).json()
status = data['success']
date = data['date']
rates = data['rates']
print(rates)

print('----------------------------------------------')

naira = round(rates['NGN'], 2)
dollar = round(rates['USD'], 2)
euro = float(rates['EUR'])
'''
naira = 393.96
dollar = 1.08
print("Naira  :", naira)
print("Dollar :", dollar)

price = 1
amount = (price / dollar)

print(amount)
real = round(amount * naira , 2)

print(real)
print("363.50 from dolls to ngn")