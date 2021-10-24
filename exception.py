#Exception Handling
a=int(input("Enter a value"));
b=int(input("Enter a value"));
try:
	print(a/b);
	k=int(input("Enter a number :"));
	print(k)	
except ZeroDivisionError as e:
	print("We cannot divide a number by zero:",e);
except Exception:
	print("Hey,Something went wrong");
finally:
	print("End");
