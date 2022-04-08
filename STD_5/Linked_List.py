class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:                              #Define class   
    def __init__(self):
        self.headval = None

    def listprint(self):                         #Function to print the linked list
        printval = self.headval                  #Store the head(first) val in printval
        while printval is not None:              #While printval is not empty
            print (printval.dataval)             #print the value of the node
            printval = printval.nextval          #move onto to next node
            
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):                     #Function to add the last value to the linked list
        NewNode = Node(newdata)                   #Create a node with with new data  
        if self.headval is None:                  #If there is no head (first) node becomes head
            self.headval = NewNode
            return
        last = self.headval                       #store first value(headval) in var last
        while(last.nextval):                      #Go through list
            last = last.nextval                   #to find 2nd to last value
        last.nextval = NewNode                    #node just created becomes last value
        
    def insert(self, prev_val, next_val, new_data):#Method when you know the previous and next value
        if prev_val == None:
            print("No node to insert after")
        else:
            new_val = Node(new_data)               #Create a new node with the new_data("Weds")
            prev_val.nextval = new_val             #Previous value links to the new value
            new_val.nextval = next_val             #new value links to the next value

    def Insert(self, val_before, new_data):        #Method when you know only the previous value
        if val_before == None:
            print("No node to insert after")
        else:
            new_val = Node(new_data)               #Create a new node with the new data
            next_val = val_before.nextval          #store the next value after val_before
            val_before.nextval = new_val           #Link val_before to new_val("Weds")
            new_val.nextval = next_val             #Link the new val("Weds") to next_val

list = SLinkedList()                               #Initalise class object
list.headval = Node("Mon")                         #Crate head node
e2 = Node("Tue")                                   #Create next nodes
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2                          #Link head node to next node
e2.nextval = e3                                    #Link each node to its next node
e3.nextval = e4
e4.nextval = e5
list.AtEnd("Sun")                                  #Create last node in list

#list.listprint()                                  #Print list to screen
#list.insert(e2,e3,"Weds")                         #Insert using prev and next val
list.Insert(e2, "Weds")                            #Insertusing only prev val
list.listprint()                                   #Print list to screen