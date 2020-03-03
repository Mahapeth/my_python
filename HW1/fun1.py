Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fun(x):
	if -2.4<=float(x)<=5.7:
		return pow(float(x),2)
	else:
		return 4

	
>>> fun(5.7)
32.49
>>> fun(4)
16.0
>>> fun(7)
4
>>> 