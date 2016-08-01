# range function
# This doesn't work well in Python 2.7.  It's meant for Python 3.0.
# the print(i, end=" ") was not really recognized, so I tried
# print(i, " ") because I think that's how you do it in C++
# the result was that everything including the parentheses was printed, with the exception of the
# double quotes being turned into single quotes.
# (0, ' ')
# (1, ' '), etc was the result
# when I tried 
# print i, ' '
# the result was that it printed the numbers in a column, not a row
# last ditch effort was print i, 'hi\t'
# which put a space between the number and the word hi, but still put the results in a column

# I couldn't get it to decrement by using -1
# The last line of the program did NOT make the program wait until a keystroke was made. It produced
# an error that made the program stop running after any key was hit.  So, in effect, it DID stop the 
# program from marching forward until you did something illegal.

#print("range(10)")
#for i in range(10):
#	print(i, end=" ")
#	print(i, " ")
#	print i, 'hi\t'

#print("range(0,50,5)")
#for i in range(0,50,5):
#	print(i, end=" ")
#	print(i, " ")

print("range(10,1,-1)")
for i in range(10,1,-1) #  Python 2.7 doesn't like this statement
#	print(i, end=" ")
	print i

#print("range(10)")
#for i in range(10):
#	print("Hi! ")

#input("\n\nPress the enter key to exit.")
