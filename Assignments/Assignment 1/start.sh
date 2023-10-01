#!/bin/bash
entrypoint="/scripts/entrypoint.sh"

if [ ! "$@" = "" ]
then
	entrypoint=$@
fi

truncate -s 0 logs/alert.log
truncate -s 0 logs/snmp.log

docker run --rm -it \
	--mount "type=bind,source=$PWD/config/snort.conf,target=/etc/snort/snort.conf,readonly" \
	--mount "type=bind,source=$PWD/config/local.rules,target=/etc/snort/rules/local.rules,readonly" \
	--mount "type=bind,source=$PWD/config/black_list.rules,target=/etc/snort/rules/black_list.rules,readonly" \
	--mount "type=bind,source=$PWD/logs/alert.log,target=/var/log/snort/alert" \
	--mount "type=bind,source=$PWD/logs/snmp.log,target=/var/log/snmp.log" \
	--mount "type=bind,source=$PWD/scripts,target=/scripts,readonly" \
	-p 127.0.0.1:161:161/udp \
	csi4139/docker-snort \
	$entrypoint

