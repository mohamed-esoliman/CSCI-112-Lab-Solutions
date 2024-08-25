"""
Name: Mohamed Soliman
File: roster.py
Resources to manage a roster of students.
"""

from student import Student
from random import randint


class Roster(object):
    """Represents a roster of students."""

    def __init__(self, students=None, numberOfScores=3):
        """Can use an optional list of students."""
        self.numberOfScores = numberOfScores
        self.roster = {}
        if students:
            for student in students:
                self.roster[student.getName()] = student

    def getNumberOfScores(self):
        """Returns the number of scores in any student's info."""
        return self.numberOfScores

    def getNames(self):
        """Returns a sorted list of student names."""
        return sorted(self.roster.keys())

    def __len__(self):
        """Returns the number of students in the roster."""
        return len(self.roster)

    def isEmpty(self):
        """Returns True if the roster is empty, or False otherwise."""
        return len(self.roster) == 0

    def get(self, studentName):
        """Returns the student with the given name,
        or None otherwise."""
        return self.roster[studentName] if studentName in self.roster else None

    def add(self, newStudent):
        """Adds a student to the roster."""
        self.roster[newStudent.getName()] = newStudent

    def remove(self, studentName):
        """Removes and returns the student with the given name,
        or None otherwise."""
        return self.roster.pop(studentName, None)

    def __str__(self):
        """Returns the string representation of roster."""
        return "\n".join(map(lambda name: str(self.roster[name]), self.getNames()))


def createRoster(numberOfScores=3):
    """Creates a roster for testing purposes."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Juan", "Bill", "Stacy", "Maria", "Charley")
    for name in names:
        s = Student(name, numberOfScores)
        for index in range(numberOfScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    roster = Roster(students=students, numberOfScores=numberOfScores)
    return roster


def main():
    """Tests sorting."""
    # Print the contents
    roster = createRoster(8)
    print("The roster of students:")
    print(roster)
    print()
    print("The number of scores:")
    print(roster.getNumberOfScores())
    print()
    print("The students' names: ")
    print(roster.getNames())
    print()
    print("The length of the roster:")
    print(len(roster))
    print()
    print("Is the roster empty?:")
    print(roster.isEmpty())
    print()
    print("Maria is in the list:")
    print(roster.get("Maria"))
    print()
    print("Mohamed is not in the list:")
    print(roster.get("Mohamed"))
    print()
    roster.add(Student("Mohamed", 8))
    print("Mohamed is now in the list:")
    print(roster.get("Mohamed"))
    print()
    roster.remove("Maria")
    print("Maria is not in the list now:")
    print(roster.get("Maria"))


if __name__ == "__main__":
    main()
