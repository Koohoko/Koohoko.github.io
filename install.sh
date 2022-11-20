#!/bin/bash

sudo apt-get update
sudo apt-get install tmux
curl -LO https://github.com/ClementTsang/bottom/releases/download/0.6.8/bottom_0.6.8_amd64.deb
sudo dpkg -i bottom_0.6.8_amd64.deb
rm bottom_0.6.8_amd64.deb
