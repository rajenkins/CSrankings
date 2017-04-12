#!/bin/sh
echo "updating DBLP"
make update-dblp
echo "updating our databases from new DBLP"
make