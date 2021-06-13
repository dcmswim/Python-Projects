

'''In this example, the __updateSoftware method is private and cannot be
    accessed outside of the class. _restart is a protected method so it can be
    accessed outside of the laptop class.
    '''
class laptop:
    def __init__(self):
        self.__updateSoftware()
        
    #protected method
    def _restart(self):
        print('restarting')

    #private method
    def __updateSoftware(self):
        print('updating...')

x = laptop()
x._restart()

'''In the above example, if x._restart() was instead x.__updateSoftware(),
    an error would occur because the __updateSoftware method cannot be directly
    accessed by an outside object.
'''



