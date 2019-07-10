def sortStudents(students):
    students.sort(key= lambda x : x.split(' ')[-1] )
    return students

"""
You are given a list of students who want to apply to the internship at CodeFights.
For the ith student you know their full name students[i], which can consist of up to 5 words (where a word is a set of consecutive letters).
It is guaranteed that the surname is always the last name of student's full name.

Your task is to sort the students [lexicographically] by their surnames.
If two students happen to have the same surname, their order in the result should be the same as in the original list.

[lexicographically] 
String A is lexicographically smaller than string B either if A is a prefix of B (and A ≠ B), or if there exists such index i (0 ≤ i < min(A.length, B.length)), that Ai < Bi, and for any j (0 ≤ j < i) Aj = Bj.
The lexicographic comparison of strings is implemented by operator < in modern programming languages.

Example:

students = ["John Smith", "Jacky Mon Simonoff", 
            "Lucy Smith", "Angela Zimonova"]

the output should be

sortStudents(students) = ["Jacky Mon Simonoff", "John Smith", 
                          "Lucy Smith", "Angela Zimonova"]
"""
