#  Multiple inheritane : where a child class can inherit from more than one parent

class Writer:
    def write(self):
        return "Writing"
    
class Programmer:
    def code(self):
        return "coding"
    
class TechLead(Writer, Programmer):
    def lead(self):
        return "Leading the team"
    
tech_lead = TechLead()

print(tech_lead.write())  # Output: Writing...
print(tech_lead.code())   # Output: Coding...
print(tech_lead.lead())  