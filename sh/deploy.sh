echo ${USER}
export PYUPDATER_FILESERVER_DIR=/home/asa/sites/deploy/pyupdatermywx
scp ./pyu-data/deploy/* asa@fileserver-staging.asa.ubuntu:${PYUPDATER_FILESERVER_DIR}