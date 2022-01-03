from collections import namedtuple
import config
import globalPluginHandler
import gui
import wx

Settings = namedtuple("Settings", "configKey, label, defaultValue")
settingItems = [
    Settings("PageLoading", _("Announce loading of pages"), "boolean(default=false)"),
    Settings("RefreshingPage", _("Announce page refresh"), "boolean(default=false)"),
    Settings("ClosingTab", _("Announce closing of tab"), "boolean(default=false)"),
    Settings("OpeningNewTab", _("Announce Opening of new tab"), "boolean(default=false)"),
    Settings("OpeningWindow", _("Announce window opening"), "boolean(default=false)")
    ]

config.conf.spec["MSEdgeDiscardAnnouncements"] = {setting.configKey: setting.defaultValue for setting in settingItems}

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
        self.helper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
        for setting in settingItems:
                widget = self.helper.addItem(wx.CheckBox(self, label=setting.label, name=setting.configKey))
                widget.SetValue(self.config[setting.configKey])

    def onSave(self):
        for child in self.helper.sizer.GetChildren():
            widget = child.GetWindow()
            if isinstance(widget, wx.CheckBox):
                self.config[widget.Name] = widget.IsChecked()
