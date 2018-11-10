import os
def instruction():
    print("**********************************************************************************")
    print("******Welcome to instruction Menu******")
    print("All the questions are related to programming language C and data structure")
    print("The instruction for attempting the test are as follows:")
    print(">>  1. There are only multiple questions present in the test ")
    print(">>  2. For every correct answer you will be rewarded with 5 points")
    print(">>  3. For every incorrect answer negative points are there 2 for each")
    print(">>  4. You cannot be able to skip any question, if you do marks will be deducted")
    input("Press any key to continue")
    os.system('cls')
    startTest()
def About():
    print("**********************************************************************************")
    print("This test is created and developed  by Mayank Kumar Prajapati")
    print("Student of CSE Department(G L Bajaj Group of Institutions)")
    input("Press any key to continue")
    os.system('cls')
    startTest()
def round1():
    ps=0
    ns=0
    print()
    print("***Welcome to first round***")
    print("You have to score greater than 25 points to clear this round...GoooD LuCk..")
    input("Press any key to start the round")
    os.system('cls')
    print("Q1. In which of the following case it is possible to obtain different result\nfor call by reference and call by name parameter??")
    print("A. Passing an expression as a parameter")
    print("B. Passing an array as a parameter")
    print("C. Passing a pointer as a paramter")
    print("D. Passing an array element as a parameter")
    x=input()
    if x=='D' or x=='d':
        print("Correct answer.. You got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong aswer")
        ns+=2
    input()
    os.system('cls')
    print("Q2. Heap allocation is required for languages")
    print("A. that supports recursion")
    print("B. that support dynamic data structure")
    print("C. that use dynamic scope rules")
    print("D. None of the above")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. ")
        ps+=5
    else:
        print("bad luck.. wrong answer..")
        ns+=2
    input()
    os.system('cls')
    print("Q3.A certain processor supports only the immediate and direct addressing mode\nWhich of the following programming language features cannot be\nimplemented on this processor??")
    print("A. Pointers")
    print("B. Arrays")
    print("C. Records")
    print("D. Recursive procedure with local variables")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
    print("Q4. Faster access to non local variables is achieved using an array of pointers\nto activation records called a")
    print("A. stack")
    print("B. heap")
    print("C. display")
    print("D. activation tree")
    x=input()
    if x=='D' or x=='d':
        print("Correct answer")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
    print("Q5. The following declarations\nstruct node{\nint i;\nfloat j;\n};\nstruct node *s[10];\ndefined s to be")
    print("A. An array, each element of which is a pointer to structre of type node")
    print("B. A structure of two fields, each field being a pointer to an array of 10 elements")
    print("C. A structure of 3 fields: an integer, a float and an array pf 10 elements")
    print("D. An array,each element of which is a structure of type node")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
    print("Q6. The most appropriate matching for the following pairs\nX. Indirect Addressing     1. Loops\nY. Immediate Addressing     2. Pointers\nZ. Auto decrement     3.Constants")
    print("A. X-3 Y-2 Z-1")
    print("B. X-1 Y-3 Z-2")
    print("C. X-2 Y-3 Z-1")
    print("D. X-3 Y-1 Z-2")
    x=input()
    if x=='C' or x=='c':
        print("Correct answer")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
        
    print("Q7. Consider the following C function definition\nint Trial(int a,int b,int c)\n{\nif((a>=b) && (c<b)) return b;\nelse if(a>=b) return Trial(a,c,b);\nelse return Trial(b,a,c);\n}")
    print("The function Trial")
    print("A. finds the maximum of a, b and c")
    print("B. finds the minimum of a, b and c")
    print("C. finds the middle of a, b and c")
    print("D. None of these")
    x=input()
    if x=='D' or x=='d':
        print("Correct answer")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2  
    input()
    os.system('cls')
        
    print("Q8. Aliasing in the context of programming languages refers to")
    print("A. multiple variables having the same memory location")
    print("B. multiple variables having the same value")
    print("C. multiple variables having the same identifier")
    print("D. multiple uses of same variable")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
    
    print("Q9. The value of j at the end of the execution of the following program is\n")
    print("int inr(int i){\nstatic int count=0;\ncount=count+i;\nreturn count;\n}\nmain(){\nint i,j;\nfor(i=0;i<=4;i++)\nj=inr(i);\n}")
    print("A. 10")
    print("B. 4")
    print("C. 6")
    print("D. 7")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
    
    print("Q10. Consider the following program in C language:")
    print("#include<stdio.h>\nmain(){\nint i;\nint *pi=&i")
    print("scanf(""%d"",pi);")
    print("printf(""%d"",i+5);\n}")
    print("Which of the following statement is True")
    print("A. Compilation fails")
    print("B. Execution result in a run time error")
    print("C. On execution, the value printed is 5 more than the address of variable i")
    print("D. On execution, the value printed is 5 more than the integer value entered")
    x=input()
    if x=='D' or x=='d':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2  
    input("Press Enter to see the result")
    os.system('cls')
    
    tot=ps-ns
    print("Your score is {} and required score is 30 for this round".format(tot))
    if tot<25:
        print("You have not cleared the first round")
        input("Press any key to restart the test")
        os.system('cls')
        startTest()
    else:
        print("Congrats... You have been selected for the second round")
        input("Press any key to enter in the second round")
        os.system('cls')
        round2()
def round2():
    ps=0
    ns=0
    print()
    print("***Welcome to second round***")
    print("Most of the questions here are from stack and queue...")
    print("You have to gain more than 30 marks for opening the gate of final round.. Good luck..")
    input("Press any key to start the round2")
    os.system('cls')
    print("Q1. A common property of logic programming languages and functional programming languages is")
    print("A. both are procedural language")
    print("B. both are on lambda calculus")
    print("C. both are declarative")
    print("D. all of the above")
    x=input()
    if x=='C' or x=='c':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
    
    print("Q2. An abstract datatype is")
    print("A. a datatype that cannot be instantiated")
    print("B. same as an abstract class")
    print("C. a datatype for which only the operations defined on it can be used, but noone else")
    print("D. all of the above")
    x=input()
    if x=='C' or x=='c':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q3. Early binding refers to a binding performed at compile time and late binding refers to a binding refers to a binding performed at execution time. Consider the following statements:")
    print(" (i) Static scope facilitates w1 binding")
    print(" (ii) Dynamic scope requires w2 binding")
    print(" (iii) Early binding w3 execution efficiency")
    print(" (iv) Late bindings w4 execution efficiency")
    print("The right choices w1,w2,w3 and w4(in the order) are")
    print("A. early, late, decrease, increase")
    print("B. late, early, increase, decrease")
    print("C. late, early, decrease, increase")
    print("D. early, late, increase, decrease")
    x=input()
    if x=='D' or x=='d':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q4. Which of the following is essential for cinverting an infix expression to the postfix form efficiently?")
    print("A. an operator stack")
    print("B. an operand stack")
    print("C. an operand stack and an operator stack")
    print("D. a parse tree")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2  
    input()
    os.system('cls')
    
    print("Q5. The best data structure to check whether an arithmetic expression has balanced parenthesis is a")
    print("A. queue")
    print("B. stack")
    print("C. tree")
    print("D. list")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q6. A program attempts too generate as many permutations as possible of the string, 'abcd' by pushing the character a,b,c,d in the same order onto a stack,but it may pop off the top character at any time. Which one of the following string CANNOT be generated using this program")
    print("A. abcd")
    print("B. dcba")
    print("C. cbad")
    print("D. cabd")
    x=input()
    if x=='D' or x=='d':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q7. The following postfix expression with single digit operands in evaluated using a stack")
    print("8 2 3 ^ / 2 3 * + 5 1 * -")
    print("Note that ^ is the exponentiation operator.The top two elements of the stack after the first * is evaluated are ")
    print("A. 6,1")
    print("B. 5,7")
    print("C. 3,2")
    print("D. 1,5")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q8. The result evaluating the postfix expression:")
    print("10 5 + 60 6 / * 8 - is")
    print("A. 284")
    print("B. 213")
    print("C. 142")
    print("D. 71")
    x=input()
    if x=='C' or x=='c':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input()
    os.system('cls')
    
    print("Q9. A queue is implemented using an array such that ENQUEUE and DEQUEUE operations are performed efficiently. Which one of the following is correct")
    print("A. Both operations can be performed in O(1) time")
    print("B. At most one operation can be performed in O(n) time but the worst case time for the other operation will be omega(n)")
    print("C. The worse case time complexity for both the operation will be omega(n)")
    print("D. Worst case time complexity for both operations will be omega(logn)")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q10. A circularly linked list is used to represent a queue. A single variable p is used to access the queue. To which node should p point such that both the operations ENQUEUE and DEQUEUE can be performed in constant time??")
    print("A. rear node")
    print("B. front node")
    print("C. not possible with a single pointer")
    print("D. node next to front")
    x=input()
    if x=='C' or x=='c':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    tot=ps-ns
    input("Press Enter to see the result")
    os.system('cls')
    
    print("Your score in second round is {} and required is more than 30".format(tot))
    
    if tot<30:
        print("You have not cleared the round 2")
        print("Press any key to restart the test")
        input()
        os.system('cls')
        startTest()
    else:
        print("Congratulations:: Great effort.. You have qualified for the final round")
        input("Press any key to enter in the final round")
        os.system('cls')
        finalRound()
        
        
def finalRound():
    ps=0
    ns=0
    print()
    print()
    print("****Welcome to final round******")
    print("You have to score more than 35 points to clear this round")
    print("Most of the questions are from tree data structure in this round")
    input("Press any key to start this round")
    os.system('cls')
    
    print("Q1 What value would the follwing function return for the input x=95?")
    print("function fun(x:integer):integer;")
    print("Begin")
    print("if x>100 then fun=x-10")
    print("else fun:=fun(fun(x+11))")
    print("End;")
    print("A. 89")
    print("B. 90")
    print("C. 91")
    print("D. 92")
    x=input()
    if x=='C' or x=='c':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')

    
    print("Q2. In a circular linked list organisatio insertion of a record involves modification of")
    print("A. one pointer")
    print("B. two pointer")
    print("C. multiple pointer")
    print("D. no pointer")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q3. Linked list are not suitable data structure of whoch one of the following problem?")
    print("A. Insertion sort")
    print("B. binary search")
    print("C. radix sort")
    print("D. polynomial manupulation")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q4. In the worst case, the number of comparisons needed to search singly linked list of length n for a given element is")
    print("A. logn")
    print("B. n/2")
    print("C. logn-1")
    print("D. n")
    x=input()
    if x=='D' or x=='d':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q5. A binary tree T has n leaf nodes. The number of nodes of degree 2 in T is")
    print("A. logn")
    print("B. n-1")
    print("C. n")
    print("D. pow(2,n)")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q6. A binary search tree is generated by inserting in order of the following integer: 50,15,62,5,20,58,91,3,8,37,60,24. The number of nodes in the left subtree and the right subtree of the root respectively is")
    print("A. 4,7")
    print("B. 7,4")
    print("C. 8,3")
    print("D. 3,8")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q7. A binary search tree is used to locate the number 43. Which of the following probe sequences is not possible??")
    print("A. 61 52 14 17 40 43")
    print("B. 10 65 31 48 37 43")
    print("C. 2 3 50 40 60 43")
    print("D. 81 61 52 14 41 43")
    x=input()
    if x=='C' or x=='c':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q8. A datastructure is required  for storing a set of integers such that each of the following operations can be done in O(logn) time, where n is the number of elements in the set.")
    print("1. Deletion of the smallest element")
    print("2. Insertion of an element if it is not already present in the set")
    print("Which of the following data structure can be used for this purpose?")
    print("A. A heap can be used but not a balnaced binary search tree.")
    print("B. A balanced bnary search tree can be used but not a heap")
    print("C. Both balanced binary search tree and heap can be used")
    print("D. Neither balanced binary search tree or heap can be used")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q9. What is the maximum height of any AVL tree with 7 nodes? Assume that the height of a tree with a single node is 0.")
    print("A. 2")
    print("B. 3")
    print("C. 4")
    print("D. 5")
    x=input()
    if x=='B' or x=='b':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2 
    input()
    os.system('cls')
    
    print("Q10. The height of a tree is the length of the longest root to leaf path in it.The maximum and minimum number of nodes in a binary tree of height 5 are")
    print("A. 63,6")
    print("B. 64,5")
    print("C. 32,6")
    print("D. 31,5")
    x=input()
    if x=='A' or x=='a':
        print("Correct answer.. you got 5 points")
        ps+=5
    else:
        print("bad luck.. wrong answer")
        ns+=2
    input("Press enter to see the result")
    os.system('cls')
    tot=ps-ns
    print("Your score is",tot," points")
    if tot<35:
        print("You have tried well.. But not cleared the final round")
        input("Press any key to restart the test")
        os.system('cls')
        startTest()
    else:
        print("You have successfully cleared all the round.. Good luck for your future..")
        input("Press any key to leave the test now...")
if __name__ == '__main__':
    def startTest():
        print("********Test for programming and data structure********")
        print("*******************************************************")
        print(">>  Enter I for instruction menu")
        print(">>  Enter A for knowing about developer of this test")
        print(">>  Enter S for starting the Test")
        print(">>  Enter L for leave the test ")
        c=input()
        os.system('cls')
        if c in ['I','i']:
            instruction()
        elif c in ['A','a']:
            About()
        elif c in ['L','l']:
            print("You have successfully leaved the test.. Close your window")
        elif c in ['s','S']:
            round1()
    startTest()
