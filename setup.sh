#!/bin/bash

/bin/cp watchgit.py /usr/sbin
/bin/cp watchgit.conf /etc
/bin/cp debian/init.d /etc/init.d/watchgit
/bin/chmod +x /etc/init.d/watchgit
echo "Watchgit installed"
