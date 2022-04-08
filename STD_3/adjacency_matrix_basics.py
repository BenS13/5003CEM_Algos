class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        print(self.adjMatrix)
        self.size = size

    def add_vertex(self):#Could rerun innit with new size but would lose data
        self.size+=1                      #Increase size of matrix by 1
        for row in self.adjMatrix:          #Add a 0 to the end of
            row.append(0)                   #each row
        self.adjMatrix.append(([0]*self.size))#add a new row with required amount of zeros
        

    def add_edge(self, vertex1, vertex2):
        if self.adjMatrix[vertex1-1][vertex2-1] == 1 and self.adjMatrix[vertex2-1][vertex1-1] == 1:
            print("Edge already exists between %d and %d" % (vertex1,vertex2))#Check to see if an edge already exists there
        elif vertex1 == 0 or vertex2 == 0:                                    #Make sure the entered vertex is greater than 0
            print("Vertices must have a value > 0")
        elif vertex1 == vertex2:                                              #Cannot connect a vertex to itself
            print("Error cannot connect a vertex to itself")
        else:
            #print("v1:",vertex1,"v2",vertex2)
            self.adjMatrix[vertex1-1][vertex2-1] = 1                          #Change the value in the corresponding space
            self.adjMatrix[vertex2-1][vertex1-1] = 1                          #To show to vertices are connected by and edge

    def remove_edge(self, vertex1, vertex2):
        if self.adjMatrix[vertex1-1][vertex2-1] == 0:                         #Check if there is an edge there or not
            print("Error there is no edge to remove here")
        else:
            self.adjMatrix[vertex1-1][vertex2-1] = 0                          #Set each vertex in the matrix to 0 thus removing the edge
            self.adjMatrix[vertex2-1][vertex1-1] = 0                          #that connected them

    
    def print_graph(self):
        print("   ",*range(1,self.size+1))                                    #Print the vertex values on y-axis of graph
        print("  ","-"*(self.size*2))
        row_count=0
        while row_count < self.size:
            '''list = self.adjMatrix[row_count]
            print(list)
            print(*list, sep ="")
            #print(no_c_and_b)'''
            no_commas = ''.join(str(self.adjMatrix[row_count]).split(','))#Remove commas from the matrix print out
            no_brackets = str(no_commas)[1:-1]                            #Remove square brackets from the matrix print out
            print(row_count+1,"|",no_brackets)                            #Print each row of the matrix with its corresponding row value at the start
            row_count+=1
            
           
    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here




#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
        g = Graph(5)
        g.print_graph()
        #g.add_edge(1,2)
        #g.print_graph()
        #g.print_graph()
        #g.remove_edge(1,2)
        #g.print_graph()
        g.add_vertex()
        g.add_vertex()
        g.print_graph()
        #g.add_edge(5,6)
        #g.print_graph()
            
if __name__ == '__main__':
   main()
