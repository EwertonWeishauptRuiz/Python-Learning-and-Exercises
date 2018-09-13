import datetime

class User():
    """
        Storing a name and a birthday of a user. We are splitting the name and returning
        the First and last name as parameters.
    """
    
    def __init__(self, full_name, birthday):
        self.name = full_name
        # The first birthday is the object where the variable will be stores and the second is the value passed to the init method
        self.birthday = birthday #yyyymmdd

        #Extract first and last names 
        name_pieces = full_name.split(" ") # Splits and store it in an array, chopping it every time there is a " " (espace)
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1] # Index -1 give always the last value in an array

    def age(self):
        """Return the age of the user in numbers"""
        today = datetime.datetime.now()
        # Gets the first 4 numbers of an int
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        date_of_birth = datetime.date(yyyy, mm, dd)
        age_in_days = (today - date_of_birth).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

""" To print valuable information about the classes on the shell"""
#print(help(User))
user1 = User("Ewerton Ruiz", 19880428)
print(user1.age())
