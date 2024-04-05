# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


class Patient:
    """Form a patient fills out at doctors office.  Enter as string."""
    def __init__(self, name, d_o_b, address, symptoms):
        self.name = name
        self.d_o_b = d_o_b
        self.address = address
        self.symptoms = symptoms

    def __str__(self):
        return f"{self.name}, {self.d_o_b}, {self.address}, {self.symptoms}"
    
    def __repr__(self):
        return f"Patient(name={self.name}, d_o_b={self.d_o_b}, address={self.address}, symptoms={self.symptoms})"
    

pat1 = Patient("Jane Doe", "5/10/85", "main street", "upset stomach")
pat2 = Patient("Joe Smith", "1/5/87", "1st Ave.", "broken finger")

print(pat1.d_o_b)
print(pat2.symptoms)