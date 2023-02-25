#!/usr/bin/env bash
set -Eeuo pipefail

apt-get update -yqq
apt-get install -yqq python3 python3-pip
pip3 debug --verbose | tee pip.log
