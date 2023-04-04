import addonHandler
import gui
import os.path
import sys

addon = addonHandler.getCodeAddon()
addonName = addon.name
addonDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "appModules", "msedge"))
sys.path.append(addonDir)
from donate_dialog import requestDonations
sys.path.remove(sys.path[-1])
import wx

addonHandler.initTranslation()

def onInstall():
    gui.mainFrame.prePopup()
    wx.CallAfter(requestDonations, addonName, gui.mainFrame)
    gui.mainFrame.postPopup()
