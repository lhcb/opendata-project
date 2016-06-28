#! /bin/bash
#
# This script will store a single file on the user's CERNBOX
# storage space.
#
#

if test $# -ne 2 ; then
  echo "cb-put.sh: needs two arguments <source> <destination>"
  exit 1
fi

LOCAL_FNAME=$1
REMOTE_FNAME=$2

set -e
function error_exit
{
  echo "$1" 1>&2
  exit 1
}


# Tell user to get a kerberos token and exit
klist &> /dev/null || error_exit "run 'kinit <username>@CERN.CH' first to obtain a kerberos token"

NAME=`klist | awk '/Default principal/{split($3, u, "@"); print u[1]}'`
EOSPATH=//eos/user/${NAME:0:1}/$NAME/$REMOTE_FNAME
EOSHOST=root://eosuser.cern.ch

xrdfs "$EOSHOST" stat "$EOSPATH" &> /dev/null && error_exit $EOSPATH" already exists"
xrdcp "$LOCAL_FNAME" "$EOSHOST/$EOSPATH"
