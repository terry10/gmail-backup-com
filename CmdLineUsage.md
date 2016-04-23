# Description #

Program for backup and restore of your GMail mailbox. You will need to activate
the IMAP access to your mailbox, to do so, please open your GMail settings and
under POP/IMAP tab activate this option.

The messages are stored in the local directory in files which names follow the
format YYYYMMDD-hhmmss-nn.eml where YYYY is the year, MM the month number, DD
is the day number, hh are hours, mm are minutes and ss are seconds when the
e-mail was SENT. For the case there is more emails with the same timestamp
there is the number nn which starts with value 1. Label assignment is stored in
the file labels.txt which is the plain text file and it pairs the emails stored
in the file described above with the assigned labels.

## Examples: ##

To perform full backup of your GMail account into directory dir, use:

```
gmail-backup.exe backup dir user@gmail.com password
```

To specify time interval, you can add additional date specification in the
format YYYYMMDD. The second date can be ommited in which case the backup is
from the first date to now:

```
gmail-backup.exe backup dir user@gmail.com password 20070621 20080101
```

You can do multiple backups into the same directory. The labels.txt is updated
according the new e-mails not in the previous backup.

To restore your backup use the restore command. To restore your GMail account
from the previous backup in the directory dir, use for example:

```
gmail-backup.exe restore dir user@gmail.com password
```

You can also use the extra feature of GMail backup. It allows the user to
completely clear his mailbox (for example if the user wants to end using the
GMail). All messages are permanently deleted (of course the email can be stored
somewhere deep in the Google company). To do so, execute the command:

```
gmail-backup.exe clear user@gmail.com password
```

The program will ask you to repeat the username, so you have the chance to
cancel your mistake.

## Backups with timestamp: ##

Since 0.10 release GMail Backup has great feature - it stores the date of the
last backup for future usage. The date is stored in the backup directory in the
file "stamp". If there is no starting date (20070621 in the example above), the
stored stamp is used. The "stamp" is updated to be the latest date from the
stored emails during the last backup.

To use this feature, simple use the --stamp command line flag:

```
gmail-backup.exe backup dir user@gmail.com password --stamp
```

## Note: ##

Under Linux, you have to use the "gmail-backup.py" script distributed in
gmail-backup-**.tar.gz file instead of the Windows binary "gmail-backup.exe".**


## Error reporting: ##

If you want to report some errors in this software, please use our user support
mailing list:

gmail-backup-com-users@googlegroups.com

To speed up the solution of your problem, please run the program with --debug
command line option and include full traceback of the error. Include also the
version of GMail Backup you have used.
Thanks.