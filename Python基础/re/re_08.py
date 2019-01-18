import re 
a = 'PythonPythonPythonPythonPython'
r = re.findall('(Python){3}',a)
print(r)
language = 'PythonC#\nJavaPHP'
s = re.findall('c#.{1}',language,re.I | re.S)
print(s)