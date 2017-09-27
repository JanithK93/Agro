class arr(list):
    def __setitem__(self, id, initialArea):
        if id >= len(self):
            self.extend([None] * (id + 1 - len(self)))
        list.__setitem__(self, id, initialArea)


    def calculateChangeInArea(self,arr,id,newArea):
        if (newArea > arr[id]):
            changedRate = ((float(newArea) - float(arr[id])) / abs(arr[id])) * 100.00
            return changedRate
        elif (newArea < arr[id]):
            changedRate = ((float( arr[id]) - float(newArea)) / abs(arr[id])) * 100.00
            return changedRate






