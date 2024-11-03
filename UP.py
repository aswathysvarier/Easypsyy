import sys
import time
def text(t):
    for char in t:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

count=0
print("\nEASYPSYY\n********\n\nHey Student!\nAre you confused about going to class today?")
print("We are here to help you to decide whether you should attend classes or not")
ch=input(Are you feeling lazy today?(yes/no)\n")
if(ch=="no"):
    print("\nWork hard and have a nice day\n")
        
else:
    print("\nLet us help you then\n")
    w=int(input("\nwhat's the weather today?(in Celsius)\t"))
    if(w<=24 or w>=30):
        count=count+1
    p=input("\nDo you have any physical problems?(y/n)\t")
    if(p=="n"):
        print("\nKeep up the good health\n")
    else:
        d=input("\nAre you on the verge of dying?(y/n)\t")
        if(d=="y"):
            print("\nWe think you can skip classes today\n")
            count=count+10
        r=input("\nDo you have other physical ailments?(y/n)\t")
        if(r=="y"):
            n=int(input("\nHow bad is it(1-10)\n(1-->can bear  10-->unbearable)\t"))
            count=count+n
    h=int(input("\nHow many subjects do you hate today?(1-5)\nplease note:Don't add all subjects\t"))
    count=count+h
if(count>10):
    print("\nSkip classes and enjoy\n")
else:
    text("\nEducation is the most vital part of our life.\nIt decides our career and our future so go to class,study hard and become successful.\n")

        

        


