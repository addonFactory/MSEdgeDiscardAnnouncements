from collections import OrderedDict
import config
import globalPluginHandler
import gui
import wx

confspec = {
    "PageLoading": "boolean(default=false)",
    "RefreshingPage": "boolean(default=false)",
    "ClosingTab": "boolean(default=false)",
    "OpeningNewTab": "boolean(default=false)",
    "OpeningWindow": "boolean(default=false)",
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
    settings = OrderedDict({
        "PageLoading": {
            "label": _("Announce loading of pages")
        },
        "RefreshingPage": {
            "label": _("Announce page refresh")
        },
        "ClosingTab": {
            "label": _("Announce closing of tab")
        },
        "OpeningNewTab": {
            "label": _("Announce Opening of new tab")
        },
        "OpeningWindow": {
            "label": _("Announce window opening")
        },
    })

    def makeSettings(self, sizer):
        self.config = config.conf["MSEdgeDiscardAnnouncements"]
        self.helper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
        for k, v in self.settings.items():
                widget = self.helper.addItem(wx.CheckBox(self, label=v["label"], name=k))
                widget.SetValue(self.config[k])

    def onSave(self):
        for child in self.helper.sizer.GetChildren():
            widget = child.GetWindow()
            if isinstance(widget, wx.CheckBox):
                self.config[widget.Name] = widget.IsChecked()
