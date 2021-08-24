#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports


# In[3]:


class Edge:
    def __init__(self, to, st, en, string=""):
        self.to = to
        self.st = st
        self.en = en
        self.string = string #Just for debugging

class Point:
    def __init__(self, node, edge, length):
        self.node = node
        self.edge = edge
        self.length = length


# In[4]:


def toStr(a, b):
    tmp = b
    anis = ""
    if b == '#':
        tmp = step
    for i in range(a, tmp+1):
        anis += s[i]
    return anis

def show():
    for i in range(len(v)):
        print("\n I :", i, "starting at", startInd[i])
        for u in v[i]:
            print("  ", u.to, " (", u.st, ',', u.en, ")", toStr(u.st, u.en))
            
def debug():
    for i in range(len(v)):
        print(" V[", i, "]", " size: ", len(v[i]))
        for u in v[i]:
            print("   ", "to", u.to, "sten", u.st, u.en, toStr(u.st, u.en))
            
def find(x):
    global v, s
    point = Point(0, -1, 0)
    p = 0
    while (p < len(x)):
        if point.edge == -1: #Must choose
            for u in range(len(v[point.node])):
                if s[v[point.node][u].st] == x[p]:
                    point.edge = u
                    point.length = 1
                    p += 1
                    break
            if point.edge == -1:
                return -1 #False
            continue
        
        if point.length == v[point.node][point.edge].en-v[point.node][point.edge].st+1:
            point.node = v[point.node][point.edge].to
            point.length = 0
            point.edge = -1
            continue
        
        if x[p] != s[v[point.node][point.edge].st+point.length]:
            return -1 #False
        p+=1
        point.length+=1
        continue
        
    anis = point.node
    if point.length != 0:
        anis = v[point.node][point.edge].to
    return anis

def dfs(st):
    global startInd
    anis = []
    for u in v[st]:
        anis = anis+dfs(u.to)
    
    if startInd[st] != -1:
        return [startInd[st]]
    
    return anis

def wordPair(x): #Returns a tuple of word index and st index
    global words, startWords
    ind = 0
    while ind < len(words):
        if x >= startWords[ind]:
            ind+=1
        else:
            break
    ind -=1
    
    return (ind, x-startWords[ind])
            
    
def phase1(x):
    subTree = find(x)
    if subTree == -1:
        return []
    anis = []
    Dfs = dfs(subTree)
    for u in Dfs:
        anis.append(wordPair(u))
    return anis


# In[17]:


#Preprocess
words = []
startWords = []
s = ""
v = [] #Neighbourhood
link = [] #Suffix Links
thisStepAdded = []
startInd = []

v.append([]) #root
link.append(0)

active = Point(0, -1, 0) # ! indicates NULL
remainder = 0

#Building
step = 0
lastStep = -1

def CreateSuffixTree():
    global v, link, thisStepAdded, startInd, v, link, active, remainder, step, lastStep, s
    
    active = Point(0, -1, 0) # ! indicates NULL
    remainder = 0
    step = 0
    lastStep = -1
    while step < len(s):
        if lastStep != step:
            remainder +=1
            lastStep = step

        sharp = s[step]
        #print("\nStep:", step, " char:", s[step], "remainder:", remainder)
        #print("Active node", active.node, "edge:", active.edge, "len:", active.length )
        #if active.edge != -1:
            #print("Valid edge from", active.node, "to:", v[active.node][active.edge].to)
        #debug()


        if active.node == 0 and active.length == 0: #If at root and NULL edge
            #print("#At root Null edge")
            #root has the edge?
            flag = -1
            for u in range(len(v[0])):
                if s[v[0][u].st] == s[step]:
                    flag = u

            if flag != -1: #root had the edge
                #print("#Root had the edge. choosing the edge")
                active.edge = flag
                active.length = 1

                #print("End of the chosen edge for ROOT already?")
                if v[active.node][active.edge].en != '#' and v[active.node][active.edge].st+active.length > v[active.node][active.edge].en:
                    #print("Yes. switching to", v[active.node][active.edge].to)
                    active.node = v[active.node][active.edge].to
                    active.length = 0
                    active.edge = -1

                step+=1
                continue


            #root didn't have the edge. ADD the edge
            #print("#Root didn't have the edge. addind the edge")
            tmp = len(v)
            v.append([])
            link.append(0)
            v[0].append(Edge(to=tmp, st=step, en='#'))
            #print("Edge added from root to ", tmp)
            #active.edge = len(v[0])-1
            active.edge = -1
            active.length = 0 #was 1 before

            startInd[tmp] = step-remainder+1
            remainder -= 1
            step += 1
            continue

        if active.edge == -1:  #Active edge not defined
            #print("#Edge was not defined")
            flag = -1
            for u in range(len(v[active.node])):
                if s[v[active.node][u].st] == s[step]:
                    flag = u

            if flag != -1: #active node had the edge
                #print("#Active node had the edge. choosing the edge. edge to", v[active.node][flag].to, " was chosen")
                active.edge = flag
                active.length = 1
                #print("End of the chosen edge for active node already?")
                if v[active.node][active.edge].en != '#' and v[active.node][active.edge].st+active.length > v[active.node][active.edge].en:
                    #print("Yes. switching to", v[active.node][active.edge].to)
                    active.node = v[active.node][active.edge].to
                    active.length = 0
                    active.edge = -1

                step+=1
                continue

            #Active node didn't have the required edge. so should be added... Shouldn't happen... apparently!
            #That was a lie
        New = -1
        if active.edge == -1: 
            #print("Edge doesn't exist.")
            tmp = len(v)
            v.append([])
            link.append(0)
            v[active.node].append(Edge(to=tmp, st=step, en='#'))
            #print("Edge added from", active.node," to ", tmp)
            active.edge = -1
            #active.length = 0
            New = active.node
            #print("Some kind of slip!")

            startInd[tmp] = step-remainder+1
            remainder -= 1

        #If the edge can support the next character
        else:
            #print("#Can Continue the edge?")
            if s[v[active.node][active.edge].st+active.length] == s[step]:
                active.length+=1
                #print("Yes. At the end of the edge?")
                if v[active.node][active.edge].en != '#' and v[active.node][active.edge].st+active.length > v[active.node][active.edge].en:
                    #print("Yes. Changing active node")
                    active.node = v[active.node][active.edge].to
                    active.length = 0
                    active.edge = -1

                step+=1
                continue

            #Need to split the edge!
            #print("No. Should slip the edge")
            helper = v[active.node][active.edge].to
            New = len(v)
            v.append([])
            link.append(0)

            #print("adding node between ", active.node, "and ", helper)
            v[New].append(Edge(to=helper, st=v[active.node][active.edge].st+active.length, en=v[active.node][active.edge].en))
            v[active.node][active.edge].to = New #Adding the edge between active node and the new one
            v[active.node][active.edge].en = v[active.node][active.edge].st+active.length-1
            #print("Added node:", New, "edge from active", active.node, " to this :", toStr(v[active.node][active.edge].st, v[active.node][active.edge].en))
            #print("Added from new:", New, "and ", helper, "sten",  v[New][len(v[New])-1].st, v[New][len(v[New])-1].en, " STR:", toStr(v[New][len(v[New])-1].st,v[New][len(v[New])-1].en))
            tmp = len(v)
            v.append([])
            link.append(0)
            v[New].append(Edge(to=tmp, st=step, en='#'))
            #print("And one more edge from new to", tmp, " with sten:", v[New][len(v[New])-1].st, v[New][len(v[New])-1].en, " STR:", toStr(v[New][len(v[New])-1].st,v[New][len(v[New])-1].en))

            startInd[tmp] = step-remainder+1
            remainder -= 1

        if thisStepAdded[step] != -1: #Rule 2
            #print("Acting as Rule 2 guids")
            link[thisStepAdded[step]] = New
            #print("Created suffix link from", thisStepAdded[step], "to", New)
        thisStepAdded[step] = New

        #Rule 1
        #Rule 3
        #Rule 4. The real rule is this.
        #So active node wasn't the root
        #print("Acting as the real Rule guids")
        #print(remainder, " remaind:", toStr(step-remainder+1, step))

        if link[active.node] == 0:
            #print("Active node didn't have the suffix link.")
            st, en = step-remainder+1, step-1
            #print("dfs from sten", st, en, ":", toStr(st, en))
            active.node = 0
            if (st > en):
                #print("No need to cruse!")
                active.edge = -1
                active.length = 0
                continue
            while (True):
                #print("New active point:", active.node, "still need to create:", toStr(st, en))
                for u in range(len(v[active.node])):
                    if s[v[active.node][u].st] == s[st]:
                        active.edge = u
                        break;
                #print("Founded edge:", v[active.node][active.edge].to, "is it long enough?")
                if v[active.node][active.edge].en == '#' or (v[active.node][active.edge].en-v[active.node][active.edge].st+1) > (en-st+1):
                    #print("Yes. Quiting dfs")
                    active.length = en-st+1
                    break;
                if v[active.node][active.edge].en == '#' or (v[active.node][active.edge].en-v[active.node][active.edge].st+1) == (en-st+1):
                    #print("Exactly the same.")
                    active.node = v[active.node][active.edge].to
                    active.edge = -1
                    active.length = 0
                    break

                #print("No. going one step deeper")
                st += (v[active.node][active.edge].en-v[active.node][active.edge].st+1)
                active.node = v[active.node][active.edge].to

            continue

        if link[active.node] != 0: #If it had a suffix link.
            st, en = v[active.node][active.edge].st, v[active.node][active.edge].st+active.length-1
            #print("active node had a valid suffix link")
            active.node = link[active.node]
            while (True):
                #print("New active point:", active.node, "still need to create:", toStr(st, en))
                for u in range(len(v[active.node])):
                    if s[v[active.node][u].st] == s[st]:
                        active.edge = u
                        break;
                #print("Founded edge:", v[active.node][active.edge].to, "is it long enough?")
                if v[active.node][active.edge].en == '#' or (v[active.node][active.edge].en-v[active.node][active.edge].st+1) > (en-st+1):
                    #print("Yes. Quiting dfs")
                    break;
                if v[active.node][active.edge].en == '#' or (v[active.node][active.edge].en-v[active.node][active.edge].st+1) == (en-st+1):
                    #print("Exactly the same.")
                    active.node = v[active.node][active.edge].to
                    active.edge = -1
                    active.length = 0
                    break

                #print("No. going one step deeper")
                st += (v[active.node][active.edge].en-v[active.node][active.edge].st+1)
                active.length -= (v[active.node][active.edge].en-v[active.node][active.edge].st+1)
                active.node = v[active.node][active.edge].to
            continue #No need to increment step


    step = len(s)-1
    for u in v:
        for t in u:
            if t.en == '#':
                t.en = step




# In[21]:


from tkinter import *
from tkinter import filedialog

root = Tk() 
root.geometry("400x940") 
root.title("Phase 1") 

inputFile = ""
RealOutput = ""
def browsefunc():
    global inputFile
    filename = filedialog.askopenfilename()
    
    inputFile = filename
    print(inputFile)
    browsed.config(text="browsed:"+filename)
    mainInput.delete('1.0', END)
    Disable(mainInput)
    Disable(browsebutton)

def Disable(obj):
    obj["state"] = "disabled"

def Enable(obj):
    obj["state"] = "normal"

def createSuffix():
    global inputFile
    global v, link, thisStepAdded, startInd, v, link, active, remainder, step, lastStep, s, startWords, words
    words = []
    startWords = []
    s = ""
    v = [] #Neighbourhood
    link = [] #Suffix Links
    thisStepAdded = []
    startInd = []
    
    v.append([]) #root
    link.append(0)
    
    Disable(browsebutton)
    Disable(mainInput)
    Disable(bSuffix)
    Disable(t1)
    Disable(t2)
    
    sprime = ""
    if len(inputFile) > 1:
        print("Reading from file", inputFile)
        file1 = open(inputFile, 'r') 
        Lines = file1.readlines() 
        
        for line in Lines: 
            if line.split()[0] != '>':
                words.append(line.split()[0])
                startWords.append(len(sprime)-1)
            sprime += line.split()[0]
            
                
            
    else:
        print("Reading from txt box")
        Lines=mainInput.get('1.0', END)
        for line in Lines.split('\n'):
            if len(line) > 0 and line[0] != '>':
                words.append(line)
                startWords.append(len(sprime)-1)
            sprime += line
        print(sprime)
    
    if sprime[0] == '>':
        sprime = sprime[1:]
    
    sprime += '$'
    print("sprime:", sprime)
    
    s = sprime
    print (words)
    print(startWords)
    
    
    thisStepAdded = [-1 for i in range(len(s)+5)]
    startInd = [-1 for i in range(2*len(s) +10)]

    
    
    CreateSuffixTree() #CREATE SUFFIX TREE
    suffixStatus.config(text="Suffix Tree Created\n")
    Enable(t3)
    print("Suffix Tree Created")
    
    Enable(tPattern)
    Enable(bFind)

def goFind():
    global RealOutput
    t = tPattern.get()
    Disable(tPattern)
    Disable(bFind)
    print(t)
    
    tLog.config(font=("Courier", 13))
    tLog.config(text="Processing...\n")
    
    L = sorted(phase1(t))
    if len(L) > 0:
        RealOutput += "In "+str(L[0][0])+"th word: " +words[L[0][0]]+" at: "+str(L[0][1])
        for i in range(1, len(L)):
            if L[i][0] == L[i-1][0]:
                RealOutput += ", "+str(L[i][1])
            else:
                RealOutput += "\nIn "+str(L[i][0])+"th word: " +words[L[i][0]]+" at: "+str(L[i][1])
    """
    for (x, y) in sorted(phase1(t)):
        print("In", words[x], "at", y)
        RealOutput += "In "+words[x]+" at " + str(y) +'\n'
    """
    
    tLog.config(text="Finished.\n")
    Enable(bShow)
    Enable(tSave)
    Enable(bSave)
    Enable(tAdSave)

def showOutput():
    global RealOutput
    Enable(tOutput)
    tOutput.delete('1.0', END)
    tOutput.insert(END, RealOutput) #THE OUTPUT
    Disable(tOutput)

def saveOutput():
    #Saving the output
    adr = tAdSave.get()
    print(adr)
    f = open(adr, "w")
    f.write(RealOutput)
    f.close()
    tSaved.config(text="Saved at "+adr)
    

bigSpace = Label(text = " ", font=("Courier", 28))
bigSpace1 = Label(text = " ", font=("Courier", 23))
smallSpace = Label(text = " ", font=("Courier", 8)) 
smallSpace1 = Label(text = " ", font=("Courier", 8)) 
smallSpace2 = Label(text = " ", font=("Courier", 8)) 

title = Label(text = "Phase 1", font=("Courier", 18))
des = Label(text = "finding a pattern in\nsome main strings.", font=("Courier", 15))

t1 = Label(text = "Type the main strings:") 

mainInput = Text(root, height = 10, width = 45, bg = "light yellow")
t2 = Label(text = "Or browse an input file:") 

browsebutton = Button(root, text="Browse", command=browsefunc)
browsed = Label(text = " ", font=("Courier", 8)) 

bSuffix = Button(root, text = "Create Suffix Tree", command = createSuffix) 
suffixStatus = Label(text = "\n") 

t3 = Label(text = "Pattern:") 
Disable(t3)
tPattern = Entry(bd=2, width = 45)
bFind = Button(root, text = "Find pattern", command =goFind) 
Disable(tPattern)
Disable(bFind)

tLog = Label(text = "\n\n", font=("Courier", 9)) 

tOutput = Text(root, height = 8, width = 45, bg = "light cyan") 
Disable(tOutput)
  
bShow = Button(root, height = 2, width = 15, text ="Show output", command = showOutput) 
Disable(bShow)

tSave = Label(root, text = "Address of the file to save to:") 
tAdSave = Entry(bd=2, width = 45)
Disable(tAdSave)
bSave = Button(root, text = "Save output", command =saveOutput) 
Disable(bSave)
tSaved = Label(root, text = "")

bExit = Button(root, text = "Exit",command = root.destroy)  


title.pack()
des.pack()
bigSpace.pack()

t1.pack() 
mainInput.pack()
t2.pack()
browsebutton.pack()
browsed.pack()
bSuffix.pack()
suffixStatus.pack()

t3.pack()
tPattern.pack()
bFind.pack()

tLog.pack()

bShow.pack() 
tOutput.pack() 

smallSpace1.pack()
tSave.pack()
tAdSave.pack()
bSave.pack()
tSaved.pack()

smallSpace2.pack()
bExit.pack() 
  
mainloop() 


# In[131]:


#show()


# In[ ]:




