#!/usr/bin/env bash
nohup python proxyPool.py server &
python proxyPool.py schedule & 