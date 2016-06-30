#! /bin/bash
#
# This script will get a single file from the user's CERNBox
# storage space.
#
#

if test $# -ne 2 ; then
  echo "cb-get.sh: needs two arguments <source> <destination>"
  exit 1
fi

REMOTE_FNAME=$1
LOCAL_FNAME=$2

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

xrdfs "$EOSHOST" stat "$EOSPATH" &> /dev/null || error_exit $REMOTE_FNAME" does not exist on your CERNBox"

LOCAL_DIR=$(dirname "${LOCAL_FNAME}")
if [ ! -d "$LOCAL_DIR" ]; then
  echo "Local directory "$LOCAL_DIR" does not exist, please create it first"
  exit 1
fi
xrdcp "$EOSHOST/$EOSPATH" "$LOCAL_FNAME"
