class SYBCAstudents:
    #static variable
    classroom = 506
    type = "UG"
    co_ordinator = "Anushree S."

    def __init__(self, name,roll_no,elective):
        #instance variable
        self.name = name
        self.roll_no = roll_no
        self.elective = elective

    #instance function
    def display_obj(self):
        print("Name :",self.name)
        print("Roll No :",self.roll_no)
        print("Elective :",self.elective)

    #static function
    def show_info():
        print("Classroom :",SYBCAstudents.classroom)
        print("Co-ordinator :",SYBCAstudents.co_ordinator)
        print("Programme Type :",SYBCAstudents.type)

s1 = SYBCAstudents("Shravani", 678, "Virtual Reality")
s1.display_obj()
SYBCAstudents.show_info()