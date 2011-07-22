#!/usr/bin/env python

if True:
    print "This is True."

should_say_hello = True
if should_say_hello:
    print "Hello!"

print "\n"

first_thing = False
second_thing = False
if first_thing:
    print "The first thing is True!"
elif second_thing:
    print "The second thing is True!"
else:
    print "Neither thing is True."

print "\n"

print "The first thing is True" if first_thing else "The first thing is not True."

print "\n"

i = 0
while i < 10:
    print i
    i += 1

print "\n"

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print i

print "\n"

for i in range(10):
    print i

