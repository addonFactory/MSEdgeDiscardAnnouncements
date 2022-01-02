import config
import globalPluginHandler
import gui
import wx

confspec = {
    "PageLoading": "boolean(default=false)",
    "RefreshingPage": "boolean(default=false)",
}
config.conf.spec["MSEdgeDiscardAnnouncements"] = confspec

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    def __init__(self):
        super(GlobalPlugin, self).__init__()
        gui.NVDASettingsDialog.categoryClasses.append(MSEdgeDiscardAnnouncementsPanel)

    def terminate(self):
        try:
            gui.NVDASettingsDialog.categoryClasses.remove(MSEdgeDiscardAnnouncementsPanel)
        except:
            pass

class MSEdgeDiscardAnnouncementsPanel(gui.settingsDialogs.SettingsPanel):
    title = "Microsoft Edge discard announcements"

    def makeSettings(self, sizer):
        self.config = config.conf["MSEdgeDiscardAnnouncements"]
        helper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
        self.reportPageLoad = helper.addItem(wx.CheckBox(self, wx.ID_ANY, label=_("Announce loading of pages")))
        self.reportPageLoad.SetValue(self.config["PageLoading"])
        self.reportPageRefresh = helper.addItem(wx.CheckBox(self, wx.ID_ANY, label=_("Announce page refresh")))
        self.reportPageRefresh.SetValue(self.config["RefreshingPage"])

    def onSave(self):
        self.config["PageLoading"] = self.reportPageLoad.GetValue()
        self.config["RefreshingPage"] = self.reportPageRefresh.GetValue()
