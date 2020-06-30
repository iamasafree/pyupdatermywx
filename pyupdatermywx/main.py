"""
A simple wxPython application which displays its version number
in a static text widget on the application's main frame.
"""
import os
import pathlib
import sys

import wx

from pyupdatermywx import __version__
from softwareupdate import SoftwareUpdate


class PyUpdaterMyWxApp(wx.App, SoftwareUpdate):
    """
    A simple wxPython application which displays its version number
    in a static text widget on the application's main frame.
    """

    def __init__(self, file_server_port, redirect=False, filename=None, debug=False):
        SoftwareUpdate.__init__(self, file_server_port=file_server_port, debug=debug)
        wx.App.__init__(self, redirect, filename)

        self.SetAppDisplayName("PyUpdater&MyWxPython")

        self.check_for_updates(debug)

        self.frame = wx.Frame(None, title="PyUpdater&MyWxPython")
        self.frame.Bind(wx.EVT_CLOSE, self.OnCloseFrame)
        self.panel = wx.Panel(self.frame)

        self.frame.SetSize(wx.Size(500, 150))
        self.statusBar = wx.StatusBar(self.frame)
        self.statusBar.SetStatusText("STATUS")
        self.frame.SetStatusBar(self.statusBar)
        self.sizer = wx.BoxSizer()

        luafile = pathlib.Path().absolute() / './pyupdatermywx/lua/script.lua'
        data = pathlib.Path(luafile).read_text()

        self.sizer.Add(
            wx.StaticText(self.frame, label=f"\n\
                        File: {data}\n\
                        Version: {__version__}\n")
        )
        self.panel.SetSizerAndFit(self.sizer)

        self.frame.Show()

    def OnCloseFrame(self, event):
        """
        Closing the main frame will cause the wxPython application to shut down.
        We should not terminate the file server process at this point.
        """
        event.Skip()
