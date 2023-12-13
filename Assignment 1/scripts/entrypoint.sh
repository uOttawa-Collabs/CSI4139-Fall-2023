#!/bin/bash
set -e -x

/scripts/start_snmp_server.sh &
/scripts/start_snort.sh

