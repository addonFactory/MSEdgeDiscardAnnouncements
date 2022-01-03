import appModuleHandler
import config

class AppModule(appModuleHandler.AppModule):
    activityIDs = []

    def getActivityIDsFromConfig(self):
        edgeConf = config.conf["MSEdgeDiscardAnnouncements"]
        self.activityIDs = [k for k, v in edgeConf.items() if type(v) == bool and v == False]

    def event_appModule_gainFocus(self):
        self.getActivityIDsFromConfig()

    def event_UIA_notification(self, obj, nextHandler, activityId, **kwargs):
        if activityId in self.activityIDs: return
        nextHandler()
