#!/usr/bin/python2.7

"""Program to Compute SLR table and validate grammar
@author: Aadesh Neupane
"""

LEN_TOKEN =3
MAX_NUM_GRAMMAR=10
MAX_NUM_SYMBOLS=10
MAX_NUM_ITEMS=20
terms=[]
nonterms=[]
no_term=0
no_nonterm=0
no_lines=0
grammar=[]
updated_grammar=[]
firstset={}

def read_grammar():
    #Opening grammar file
    global grammar
    global no_lines
    no_lines=3
    file=open('grammar1.txt','r')
    if file is None:
        print "Error opening grammar.txt"
        exit(0)
    else:
        i=0
        while i<no_lines:
            lines=file.readline()
            lines=lines.rstrip('\n\r\t')
            left,right=lines.rsplit('->')
            #print left, right
            grammar.append(left+'>'+right)
            i=i+1
        #print grammar
        #return grammar
    
def input_info():
    global no_term,no_nonterm,no_lines
    no_term=raw_input("Enter the number of terminals")
    for i in range(0,no_term):
        terms.append(raw_input("Enter the terminal symbols:\t"))
    no_nonterm=raw_input("Enter the number of non-terminals")
    for i in range(0,no_nonterm):
        nonterms.append(raw_input("Enter the non-terminal symbols:\t"))
    no_lines=raw_input("Enter the number of productions in file grammar.txt")
    
def newgrammar():
    #pseudo code to calculate first
    #print grammar
    global updated_grammar
    for i in grammar:
        a=removeLeftRec(i)
        if a is not None:
            updated_grammar.append(a[0])
            updated_grammar.append(a[1])
        else:
            updated_grammar.append(i)
        #print updated_grammar
    #return updated_grammar

def first(nonterminal):
    j=0
    for i in updated_grammar:
        lhspos=i.find('>')
        if nonterminal in i[:lhspos]:
            break
        j=j+1
    #print j   
    #print updated_grammar 
    betapos=updated_grammar[j].find('|')
    #print betapos
    #print updated_grammar[j]
    rhs=updated_grammar[j][betapos+1:]   
    #print rhs
    betapos=updated_grammar[j].find('>')
    #print updated_grammar[j][betapos+1] 
    if (updated_grammar[j][betapos+1] or rhs) in terms:
        print updated_grammar[j][betapos+1]
        print rhs
        global firstset
        firstset[nonterminal]=(updated_grammar[j][betapos+1],rhs)
    else:
        #print updated_grammar[j][betapos+1]
        first(updated_grammar[j][betapos+1])    

def removeLeftRec(grammar):
    #print grammar[0][0]
    #print grammar[0][2]
    if grammar[0] ==grammar[2]:
        betapos=grammar.find('|')
        beta=grammar[betapos+1:]
        #print beta
        alpha=grammar[3:betapos]
        firstLine=grammar[0] +'>'+beta +grammar[0]+'`'
        secondLine=grammar[0]+'`'+'>'+alpha+grammar[0]+'`'+'|e'
        return firstLine,secondLine
        
def main():
    gram=read_grammar()
    #print gram
    #input_info()
    gram1=newgrammar()
    #print gram1
    global terms
    terms=['+','(',')','id','$','e','*']
    first('E`')
    print firstset

if __name__=='__main__':
    main()