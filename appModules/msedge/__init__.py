import appModuleHandler

class AppModule(appModuleHandler.AppModule):

    def event_UIA_notification(self, obj, nextHandler, activityId, **kwargs):
        if activityId in ["PageLoading", "RefreshingPage"]: return
        nextHandler()
