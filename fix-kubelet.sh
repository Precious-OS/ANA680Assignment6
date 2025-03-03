#!/bin/bash
apt-get update
apt-get install -y libc6-amd64-cross
mkdir -p /lib64
ln -s /usr/x86_64-linux-gnu/lib/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2
systemctl enable kubelet
systemctl restart kubelet