from datetime import date


class TravelCriteria:
    def __init__(self):
        self.cities = list()
        self.states = list()
        self.interests = list()
        self.budget = 0.00
        self.beginDate = None
        self.endDate = None

    def add_city(self, city):
        self.cities.append(city)

    def get_cities(self):
        return self.cities

    def add_states(self, state):
        self.states.append(state)

    def get_states(self):
        return self.states

    def addInterest(self, interest):
        self.interests.append(interest)

    def get_interests(self):
        return self.interests

    def set_budget(self, budget):
        self.budget = budget

    def get_budget(self):
        return self.budget

    def set_beginDate(self, beginDate):
        self.beginDate = beginDate

    def get_beginDate(self):
        return self.beginDate

    def set_endDate(self, endDate):
        self.endDate = endDate

    def get_endDate(self):
        return self.endDate

    def days_staying(self):
        return self.endDate - self.beginDate

place_lists = list()

def set_place_lists(PL):
    global place_lists
    place_lists = PL

def get_place_lists():
    global place_lists
    return place_lists