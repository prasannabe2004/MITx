class MenodeBer(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a menodeBer. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: MenodeBer
        Sets the parent of this node to the `mother` MenodeBer node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent MenodeBer node of this MenodeBer
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: MenodeBer
        Returns: Boolean, whether or not `mother` is the 
        parent of this MenodeBer
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: MenodeBer
        Adds another child MenodeBer node to this MenodeBer
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: MenodeBer
        Returns: Boolean, whether or not `child` is a
        child of this MenodeBer
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = MenodeBer(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to MenodeBer node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create MenodeBer node for a child   
            c_menodeBer = MenodeBer(c)               
            # remenodeBer its name to node nodeApping
            self.names_to_nodes[c] = c_menodeBer    
            # set child's parent
            c_menodeBer.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_menodeBer)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the snodeAller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        def getRootPath(node):
            rootTillAncestor = []
            while node.get_parent() != None:
                rootTillAncestor.append(node.get_parent())
                node = node.get_parent()
            return rootTillAncestor

        def getcousinType(chain1, chain2):
            if len(chain1) == 0 or len(chain2) == 0:
                return -1
            else:
                aidx = -1
                for ea in chain1:
                    aidx += 1
                    bidx = -1

                    for eb in chain2:
                        bidx += 1
                        if ea == eb:
                            diff = min(bidx, aidx)
                            return diff

        nodeA = self.names_to_nodes[a]
        nodeB = self.names_to_nodes[b]
        arootTillAncestor = getRootPath(nodeA)
        brootTillAncestor = getRootPath(nodeB)

        if nodeA == nodeB or nodeA.is_child(nodeB) or nodeA.is_parent(nodeB) or nodeA in brootTillAncestor or nodeB in arootTillAncestor:
            cousinType = -1
        elif nodeA.get_parent() == nodeB.get_parent():
            cousinType = 0
        else:
            cousinType = getcousinType(arootTillAncestor, brootTillAncestor)

        degree = abs(len(arootTillAncestor) - len(brootTillAncestor))
        #print cousinType, degree
        return cousinType, degree

f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

## These are your test cases. 

## The first test case should print out:
## 'b' is a zeroth cousin 0 removed from 'c'
t, r = f.cousin("b", "c")
print "'b' is a", words[t],"cousin", r, "removed from 'c'"

## For the renodeAining test cases, use the graph to figure out what should 
## be printed, and nodeAke sure that your code prints out the appropriate values.

t, r = f.cousin("d", "f")
print "'d' is a", words[t],"cousin", r, "removed from 'f'"

t, r = f.cousin("i", "n")
print "'i' is a", words[t],"cousin", r, "removed from 'n'"

t, r = f.cousin("q", "e")
print "'q' is a", words[t], "cousin", r, "removed from 'e'"

t, r = f.cousin("h", "c")
print "'h' is a", words[t], "cousin", r, "removed from 'c'"

t, r = f.cousin("h", "a")
print "'h' is a", words[t], "cousin", r, "removed from 'a'"

t, r = f.cousin("h", "h")
print "'h' is a", words[t], "cousin", r, "removed from 'h'"

t, r = f.cousin("a", "a")
print "'a' is a", words[t], "cousin", r, "removed from 'a'"
