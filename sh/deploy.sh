export PYUPDATER_FILESERVER_DIR=/home/asa/sites/deploy/pyupdatermywx
scp -i C:/Users/asa/.ssh/id_rsa ./pyu-data/deploy/* asa@fileserver-staging.asa.ubuntu:${PYUPDATER_FILESERVER_DIR}