import appModuleHandler
import config

class AppModule(appModuleHandler.AppModule):
    activityIDs = []

    def getActivityIDsFromConfig(self):
        edgeConf = config.conf["MSEdgeDiscardAnnouncements"]
        self.activityIDs = [i[0] for i in edgeConf.items() if type(i[1]) == bool and i[1] == False]

    def event_appModule_gainFocus(self):
        self.getActivityIDsFromConfig()

    def event_UIA_notification(self, obj, nextHandler, activityId, **kwargs):
        if activityId in self.activityIDs: return
        nextHandler()
