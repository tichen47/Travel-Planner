from Views.TravelMenu.menuChild import menuChild  # importing our generated file
from Views.TravelMenu.waitingChild import waitingChild

class Controller:
    def __init__(self):
        self.viewList = list()
        waiting = waitingChild()
        travel_menu = menuChild()
        self.viewList.append(waiting)
        self.viewList.append(travel_menu)

    def startTravel(self):
        self.viewList[0].listener(self)

    def startWait(self):
        self.viewList[0].hide()
        self.viewList[1].start()