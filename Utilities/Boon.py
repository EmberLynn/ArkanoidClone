# class for holding information on Boons

# A boon has a name (mandatory), a description (optional), and a bool (active) for if player currently has the boon

class Boon:
    def __init__(self, name, active, description):

        self.__name = name
        self.__active = active
        self.__description = description

    def set_name(self, name):
        self.__name=name
    def get_name(self):
        return self.__name
    name=property(get_name,set_name)

    def set_active(self, active):
        self.__active=active
    def get_active(self):
        return self.__active
    active=property(get_active,set_active)

    def set_description(self, description):
        self.__description=description
    def get_description(self):
        return self.__description
    active=property(get_description,set_description)