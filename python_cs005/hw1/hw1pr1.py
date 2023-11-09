# CS5, hw1pr1
# Filename: hw1pr1.py
# Name: Pranav Patel
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]  
print("answer0:", answer0)

# Problem 1: creating [7, 1]
answer1 =   e[1:2] + pi[1:2]           # it's not the right answer, but a start...
print("answer1:", answer1)

#[9, 1, 1] (start:end:step)
answer2 = pi[::-2]
print("answer2:", answer2)

#[1, 4, 1, 5, 9]
answer3 = pi[1:]
print("answer3:", answer3)

#[1, 2, 3, 4, 5]
answer4 = e[::-2] + pi[::2]
print("answer4:", answer4)

# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey' 3 ops
answer5 = h[0] + h[4:6]    
print("answer5:", answer5)

# Problem 6:  'collude' 5 ops
answer6 = c[:-3] + m[1:3] + c[6:]    
print("answer6:", answer6)

# Problem 7:  'arveyudd' 3 ops
answer7 = h[1:] + m[1:]
print("answer7:", answer7)

# Problem 8:  'hardeharharhar' 10 ops FIX
#harveymuddcollege
answer8 = h[:-3] + (h+m+c)[8::6] + h[:-3]+ h[:-3] + h[:-3]
print("answer8:", answer8)

# Problem 9:  'legomyego' 8 ops
#harveymudd
answer9 = c[3:6] + c[1] + (h+m)[-4:-7:-1] + c[-2::-4]
print("answer9:", answer9)

#Problem 10; 'clearcall'
#collegeharvey
answer8 = c[::3] + h[1:3] + (c+h)[::8] + c[2:4]
print("answer8:", answer8)