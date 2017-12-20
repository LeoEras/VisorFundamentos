#!/bin/bash
for branch in `git branch -a | grep remotes | grep -v HEAD | grep -v master `; do
   git clone http://est_espol:gPw19KX3_@200.10.150.91/est_espol/Fundamentos.git --branch ${branch#remotes/origin/} ${branch#remotes/origin/}
done