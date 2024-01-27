import random, tempfile

countries = ["North Korea","Australia","New Zealand","Germany","France","Jamaica","Colombia","India","Bangladesh","Malaysia","Indonesia","Portugal","Iceland","USA","Canada","Japan","China","Morocco","Argentina","Spain"]

#1 opens and copies current matches.txt file to tempfile

fp = tempfile.TemporaryFile("w+t")
file = open("matches.txt","r")
for line in file:
    fp.write(line)
    fp.seek(0)
file.close()

#2 creates new matches.txt file and appends tempfile content

file = open("matches.txt","w")
file.write(f"{random.choice(countries)} - {random.choice(countries)}\n")
for line in fp:
  file.write(line)
fp.close()

#3 final matches.txt file is returned and cycle repeats

file.close()