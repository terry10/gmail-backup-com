#!/bin/bash
#python2.5 -O /usr/lib/python2.5/py_compile.py gmail-backup-gui.py
#python2.5 -O /usr/lib/python2.5/py_compile.py gmail-backup.py
#python2.5 -O /usr/lib/python2.5/py_compile.py gmb.py
mkdir dist_SH
cp gmail-backup.py gmail-backup-gui.py gmb.py dist_SH
cp gmail-backup.sh gmail-backup-gui.sh gmb.gif gmb.ico dist_SH
cp gmail-backup.pot dist_SH
mkdir -p dist_SH/messages/cs_CZ/LC_MESSAGES
cp messages/cs_CZ/LC_MESSAGES/gmail-backup.mo dist_SH/messages/cs_CZ/LC_MESSAGES/gmail-backup.mo
cp messages/cs_CZ.po dist_SH/messages/cs_CZ.po
cd dist_SH
unzip ../svc.zip
