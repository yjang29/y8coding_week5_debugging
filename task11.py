print("READY FOR THE QUIZ? I WILL ASK YOU TWO QUESTIONS!")
input()
lang = input("Q1: What programming language are we studying?")

pts = 0

if lang == "Python":
    pts += 1
    print("That's right!")

else:
    print("That was wrong!")
    print("Next question coming up...")
    print("Q2: When there's a problem with the order of the symbols in code... this is:")
    error = input()
    if error == "syntax error":
        pts += 1
        print("That's right!")
    else:
        print("That was wrong!")


### What was wrong ?
### DISCUSS HERE:
###
### Was this a... syntax, logical or runtime error?

### logical