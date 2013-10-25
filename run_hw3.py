import requests
from os import getcwd

url = 'https://raw.github.com/sosborne/math_566/master/max_flow.py'
directory = getcwd()
filename = directory + 'maxflow.py'
r = requests.get(url)

f = open(filename,'w')