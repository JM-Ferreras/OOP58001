class Person:
  def __init__(attr, std, pre, mid, fin):
    attr.__std=std
    attr.__prelim=pre
    attr.__midterm=mid
    attr.__final=fin
  def display(attr):
    print("The Prelim grade of Student", attr.__std, "is", attr.__prelim,)
    print("The Prelim grade of Student", attr.__std, "is", attr.__midterm)
    print("The Prelim grade of Student", attr.__std, "is", attr.__final)
  def Grade(attr):
    print("Your average is", int((attr.__prelim + attr.__midterm + attr.__final)/3))

student1=Person(1,92,84,89)
student2=Person(2,84,74,89)
student3=Person(3,89,91,85)
student1.display()
student1.Grade()

student2.display()
student2.Grade()

student3.display()
student3.Grade()