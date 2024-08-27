#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/../_common.sh
set -uo pipefail

PUREPYINDI_COMMIT_ISH=master
orgname=magao-x
reponame=purepyindi
parentdir=/opt/MagAOX/source
clone_or_update_and_cd $orgname $reponame $parentdir || exit 1
git checkout $PUREPYINDI_COMMIT_ISH || exit 1

cd $parentdir/$reponame
sudo -H /opt/conda/bin/pip install -e .[all] || exit 1
python -c 'import purepyindi' || exit 1
