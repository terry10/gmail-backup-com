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
import time
import pickle
import collections

# in this dictionary we store all settings
settings = collections.defaultdict(str)

def settingsFn():
    """Generate a platform dependent config file."""
    c_dir = os.path.dirname(sys.argv[0])
    c_cfg = os.path.join(c_dir, 'gmail-backup-gui.cfg')
    if os.path.isfile(c_cfg):
        return c_cfg

    if os.name == 'nt':
        appdata = os.environ['APPDATA']
        fn = os.path.join(appdata, 'Gmail Backup')
    else:
        fn = os.path.expanduser(os.path.join('~', '.gmb'))
    fn = os.path.join(fn, 'settings')
    return fn

def settingsMakedirs():
    """Create needed directries to store the config file."""
    
    fn = settingsFn()
    dn = os.path.dirname(fn)
    if not os.path.isdir(dn):
        os.makedirs(dn)

def save():
    """Save the settings dictionary by pickle module."""
    
    try:
        settings_fn = settingsFn()
        settingsMakedirs()
        fl = open(settings_fn, "wb")
        pickle.dump(settings, fl)
        fl.close()
    except:
        pass
    
def load():
    """Load the settings dictionary by pickle module."""
    global settings
    
    try:
        settings_fn = settingsFn()
        settingsMakedirs()
        fl = open(settings_fn, "rb")
        settings = pickle.load(fl)
        fl.close()
    except:
        # no settings yet
        pass
       
