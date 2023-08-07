import re

songtext = """Thank you

What you want
Baby, I got it
What′s you need?
You know I got it
All I'm askin′
Is for a little respect when you get home (just a little bit!)
Hey baby (just a little bit!)
When you get home (just a little bit!)
Mister (just a little bit!)

I ain't gonna do you wrong
While you're gone
I ain′t gonna do you wrong
Because I don′t wanna
All I'm askin′
Is for a little respect when you get home (just a little bit!)
Hey baby (just a little bit!)
When you get home (just a little bit!)
Mister (just a little bit!)

I'm about to give all of my money
And all I′m askin' in return, honey
You give me my profits when you get there (just a, just a, just a, just a...)
(Just a, just a, just a, just a...) Yeah baby, when you get home
(Just a little bit!) ooh, yeah, ooh (just a little bit!)

Your kiss is
Sweeter than honey
Guess what?
So is my money
All I need
Is for a little respect when you get home (re, re, re, re...)
Baby, when you get home (just a little bit)
Lay it on me (just a little bit)

R-E-S-P-E-C-T
Find out what it means to me
R-E-S-P-E-C-T
Take care, TCB

Oh, a little respect
Yeah, baby (just a little bit)
I want a little respect (just a little bit)
Now, I get tired (just a little bit)
But I keep on tryin′ (just a little bit)
Runnin' out foolin' (just a little bit)
I ain′t lyin′ (just a little bit)
Yes, respect (re, re, re, re...)
All I need (re, re, re, re...)
Is respect (respect, justa little bit)

All I want (just a little bit)
Oh yeah (just a little bit)
I want little respect (just a little bit)
Yeah, baby (just a little bit)
A little respect (just a little bit)
Oh honey (just a little bit)
Sock it to me (just a little bit)

All I want (just a little bit)
Lay it on me (just a little bit)
Oh, I want little respect (just a little bit)
Ladies and gentlemen
Thank you so much, for being so very wonderful to us here in Paris
Being so hospitable, so warm
Thank you! Thank you! Thank you!
Bye-bye, we love ya!

(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)
(Just a little bit)"""

text_alphnum = re.sub(r'\W+', '', songtext)
#text_alphnum = re.sub(r'\^a-zA-Z0-9', '', songtext)

words=text_alphnum.lower().split() # split uses space as separator by default

print(len(words)) # length of lists (which are words now)
print(words)

word_count = {}  #empty dictionary

for i in words:
  if i in word_count:  # if word is already in dictionary, counts up
    word_count[i] += 1
  else: 
    word_count[i] = 1 # if not, will get added

search=str(input("Which word would you like to look up?\n"))

try:                            # how to deal with result = None
  result=word_count[search]
except KeyError:
    result = 0                  # convert it into "0"

print(f"The word '{search}' is used {result} times")

#problem to solve = how to count words the same even if there is a symbol with it (e.g. "!")