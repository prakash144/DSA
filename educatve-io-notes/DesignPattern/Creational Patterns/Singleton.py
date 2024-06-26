class ApplicationState:
    _instance = None
    
    def __init__(self):
        self.isLoggedIn = False
        
    @staticmethod
    def getAppState():
        if ApplicationState._instance is None:
            ApplicationState._instance = ApplicationState()
            
        return ApplicationState._instance
    
appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn)
print(appState2.isLoggedIn)
        
    