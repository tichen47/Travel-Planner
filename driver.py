from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont

from Views.TravelMenu.menuChild import menuChild  # importing our generated file
from Views.TravelMenu.waitingChild import waitingChild
from Views.TravelMenu.testingChild import testingChild
from yelpapi import YelpAPI
app = QtWidgets.QApplication([])


#test = testingChild()
#test.show()

views = list()

views.append(menuChild())
views.append(waitingChild())

# for i in range(10):
views.append(testingChild())

views[0].listener(views)


app.exec()

