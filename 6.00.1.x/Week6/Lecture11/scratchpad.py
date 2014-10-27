class courseInfo(object):
    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"

    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))

    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade

class edx(object):

    def __init__(self, courses): # courses = ["6.00x","6.01x","6.02x"]
        self.myCourses = [] # a list containing courseinfo objects
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x"):

    # fill in code to set the grade
        for c in self.myCourses:
            if c.courseName == course:
                c.setGrade(grade)

    def getGrade(self, course="6.02x"):

    # fill in code to get the grade
        for c in self.myCourses:
            if c.courseName == course:
                return c.getGrade()
        return -1

    def setPset(self, pset, score, course="6.00x"):

    # fill in code to set the pset
        for c in self.myCourses:
            if c.courseName == course:
                c.setPset(pset, score)

    def getPset(self, pset, course="6.00x"):

    # fill in code to get the pset
        for c in self.myCourses:
            if c.courseName == course:
                return c.getPset(pset)
        return -1

edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(1,100)
edX.setPset(2,100,"6.00x")
edX.setPset(2,90,"6.00x")
edX.setGrade(100)
for c in ["6.00x","6.01x","6.02x"]:
    edX.setGrade(90,c)
print dir(edX)[18]
print edX.dir((edX)[24])(90)
