pyupdater build --console --app-version `./sh/getversion.sh` --add-data "../../pyupdatermywx/lua;pyupdatermywx/lua" run.py
pyupdater pkg --process --sign
