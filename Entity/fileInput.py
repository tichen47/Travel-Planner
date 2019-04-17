
class fileInput():
    def getStates(self):
        statesList = list()
        fo = open("states.csv", "r")

        while(1):
            line = fo.readline(2)
            if len(line) == 0:
                break

            if len(line) > 1:
                spot = len(line)
                x = ""
                x += line[0]
                x += line[1]
                statesList.append(x)

        return statesList