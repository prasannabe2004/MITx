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


root = None

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    if newFrob.myName() < atMe.myName():
        #If atMe is root
        if atMe.getBefore() == None:
            global root
            print 'root is empty'
            newFrob.setBefore(None)
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            root = newFrob
        #if atMe is mode in between
        elif atMe.getBefore().myName() < newFrob.myName():
            atMe.getBefore().setAfter(newFrob)
            newFrob.setBefore(atMe.getBefore)
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        #if atMe is the last node
        else:
            insert(atMe.getBefore(), newFrob)

abc = Frob('abc')
hij = Frob('hij')
ghi = Frob('ghi')

insert(hij, abc)
printFrob(root)
