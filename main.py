from pyscript import document

class favoritesubject:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        return f"Hello, my name is {self.name} from section {self.section}. My favorite subject is {self.subject}"

classmates = []

def addClassmate(event):
    user = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value
    new_classmate = favoritesubject(name=user, section=section, subject=subject)
    classmates.append(new_classmate)
    document.getElementById("notif").innerHTML = "Classmate added successfully!"  # type: ignore
    
    document.getElementById("notif").innerHTML = ""  # type: ignore

def showList(event):
    """Display the list of classmates and their introductions"""
    output = ""
    for classmate in classmates:
        output += classmate.introduce() + "<br>"
    
    document.getElementById("classmate-list").innerHTML = output  # type: ignore