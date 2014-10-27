class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    if newFrob.myName() < atMe.myName():
        node = atMe.getBefore()
        if node==None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif newFrob.myName() > node.myName():
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            node.setAfter(newFrob)
            newFrob.setBefore(node)
        else:
            insert(node, newFrob)
    else:
        node = atMe.getAfter()
        if node == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif newFrob.myName() < node.myName():
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            node.setBefore(newFrob)
            newFrob.setAfter(node)
        else:
            insert(node, newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    # Your Code Here
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)


print (andrew.getAfter()).myName()
print (eric.getAfter()).myName()
print (fred.getAfter()).myName()
print (martha.getAfter()).myName()

print

print (ruth.getBefore()).myName()
print (martha.getBefore()).myName()
print (fred.getBefore()).myName()
print (eric.getBefore()).myName()

print

print (findFront(fred)).myName()