#! /bin/bash
#
# This script will store the current state of $HOME/analysis
# on the user's CERNBOX storage space. The directory on CERNBOX
# will be named after the following pattern `everware-$date-$time`
#
#

set -e
function error_exit
{
  echo "$1" 1>&2
  exit 1
}


# Tell user to get a kerberos token and exit
klist &> /dev/null || error_exit "run 'kinit <username>@CERN.CH' first to obtain a kerberos token"

NAME=`klist | awk '/Default principal/{split($3, u, "@"); print u[1]}'`
DIRNAME=`date +everware-%d%m%Y-%H%M`
EOSPATH=//eos/user/${NAME:0:1}/$NAME/$DIRNAME
EOSHOST=root://eosuser.cern.ch

xrdfs $EOSHOST stat $EOSPATH &> /dev/null && error_exit $EOSPATH" already exists"
xrdfs $EOSHOST mkdir $EOSPATH
xrdcp -r --parallel 4 $HOME/analysis/ $EOSHOST/$EOSPATH
