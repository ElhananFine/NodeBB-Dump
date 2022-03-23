#!/bin/bash
cp -rf systemd/system/nodebb-dump.service /etc/systemd/system/
systemctl daemon-reload
systemctl restart nodebb-dump
systemctl enable nodebb-dump