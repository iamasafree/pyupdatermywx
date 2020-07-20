export PYUPDATER_FILESERVER_DIR=/home/asa/sites/deploy/pyupdatermywx
scp -v -o StrictHostKeyChecking=no ./pyu-data/deploy/* asa@fileserver-staging.asa.ubuntu:${PYUPDATER_FILESERVER_DIR}