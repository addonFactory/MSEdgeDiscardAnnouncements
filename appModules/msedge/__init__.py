import appModuleHandler
import config

class AppModule(appModuleHandler.AppModule):

    def getActivityIDSFromConfig(self):
        edgeConf = config.conf["MSEdgeDiscardAnnouncements"]
        activityIDS = [i[0] for i in edgeConf.items() if type(i[1]) == bool and i[1] == False]
        return activityIDS

    def event_UIA_notification(self, obj, nextHandler, activityId, **kwargs):
        activityIDS = self.getActivityIDSFromConfig()
        if activityId in activityIDS: return
        nextHandler()
