#!/usr/bin/env python2.5
# -*-  coding: utf-8 -*-
#
#   Gmail Backup GUI
#   
#   Copyright © 2008, 2009, 2010 Jan Svec <honza.svec@gmail.com> and Filip Jurcicek <filip.jurcicek@gmail.com>
#   
#   This file is part of Gmail Backup.
#
#   Gmail Backup is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the Free
#   Software Foundation, either version 3 of the License, or (at your option)
#   any later version.
#
#   Gmail Backup is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#   more details.
#
#   You should have received a copy of the GNU General Public License along
#   with Gmail Backup.  If not, see <http://www.gnu.org/licenses/
#
#   See LICENSE file for license details


import os
import wx, sys, optparse
import xml.dom.minidom
import threading
import time
import imaplib
import base64
import hashlib

import wx
import wx.html
import wx.lib.dialogs
import wx.lib.newevent

import locale
import ctypes
import gettext


import settings

aboutText = """
<p align="center">
    <b>Gmail Backup</b> 
    <br>
    <br>
    revision %(revision)s (%(revisiondate)s)
</p>

<p>
The purpose of this program is to simplify 
the process of backing up, restoration, or  
migration of your emails from your Gmail Account.
</p>

<p>
Copyright (C) 2008,2009 by Jan Svec and Filip Jurcicek
</p>

<p>
See <a href="http://www.gmail-backup.com">www.gmail-backup.com</a>
</p>""" 

registerText = """
<p>
To register <b>Gmail Backup</b> and to unlock all features, you have to buy a license at <a href="http://www.gmail-backup.com/buy-now">www.gmail-backup.com/buy-now</a>. 
</p>
<p>
Consequently, you will recieve email with the "License owner" text and the "License code", which you can place into "License owner" text box and "License code" respectively.
</p>
<p>
Remeber! By using this program, you agree with this <a href="http://www.gmail-backup.com/license">license</a>.
</p>
<p>
More details about Gmail Backup can be found at 
<a href="http://www.gmail-backup.com/documentation">www.gmail-backup.com/documentation</a>.
</p>
""" 

class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())
        
class AboutBox(wx.Dialog):
    def __init__(self,  MAX_REVISION, MAX_DATE):
        wx.Dialog.__init__(self, None, -1, "About Gmail Backup",
            style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|
                wx.TAB_TRAVERSAL)

        colour = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
        self.SetBackgroundColour(colour)
        
        szrVertical = wx.BoxSizer(wx.VERTICAL)

        hwin = HtmlWindow(self, -1, size=(400,200))
        vers = {}
        vers["revision"] = MAX_REVISION
        vers["revisiondate"] = MAX_DATE
        hwin.SetPage(_(aboutText) % vers)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+20))
        self.SetClientSize(hwin.GetSize())

        self.btnOk = wx.Button(self,  wx.ID_OK,  _("Ok"))
        szrVertical.Add(hwin, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        szrVertical.Add(self.btnOk, 0, wx.ALIGN_CENTER|wx.BOTTOM, 15)
        
        self.SetSizer(szrVertical)
        self.SetAutoLayout(True)
        szrVertical.Fit(self)

        self.CentreOnParent(wx.BOTH)
        self.SetFocus()
