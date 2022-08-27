electronics = ["mobile", "computer", "PC"]
for elec in electronics:
  print(elec)
  print(elec + " gadget")

##################################################
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
sum = 0
for heights in student_heights:
    sum = sum + heights
    count = count + 1
print(round(sum/count)) 

##################################################
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maximum = 0
for score in student_scores:
    if maximum <= score:
        maximum = score
print(f"The highest score in the class is: {maximum}") 

#########################################################
sum = 0
for number in range(2,101,2):
  sum += number
print(sum)
#########################################################

#Write your code below this row 👇
for number in range(1,101):
    if number%3 ==0 and number%5==0:
        print("FizzBuzz")
    elif number%3 ==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)



Output - 
mobile
mobile gadget
computer
computer gadget
PC
PC gadget
Input a list of student heights 34 23 56 77
48
Input a list of student scores 4 5 2 3 7
[4, 5, 2, 3, 7]
The highest score in the class is: 7
2550
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
