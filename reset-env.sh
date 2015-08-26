#!/bin/bash

set -ex

PDIR=env/util-test

echo "Reseting '$PDIR'"

rm -rf "$PDIR"

virtualenv --no-site-packages "$PDIR"
source "$PDIR"/bin/activate
pip install --no-deps -r requirements_test.txt

set +ex
echo "It's dangerous to go alone. Take these:"
echo "source '$PDIR/bin/activate'"
echo "nosetests"
