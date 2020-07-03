# Шаги по созданию самоустанавливающегося модуля

<code><br>
$ pip uninstall pyinstaller<br>
$ pip uninstall pyupdater<br>
$ pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip <br>
$ pip install pyupdater<br>
--$ pip install --upgrade git+https://github.com/Digital-Sapphire/PyUpdater.git@master <br>
$ pyupdater clean

$ pyupdater init<br>
$ cd ..<br>
$ pyupdater keys -c<br>
$ cd pyupdater-wx-demo-master<br>
$ mv ../keypack.pyu .<br>
$ pyupdater keys --import<br>
$ mv keypack.pyu ..<br>
$ pyupdater build --console --hidden-import=SocketServer --app-version 0.0.1 run.py<br>
$ pyupdater build --console --app-version 0.0.1 run.py<br>
$ pyupdater build --console --app-version 0.0.20 --add-data "../../pyupdatermywx/lua;pyupdatermywx/lua" run.py<br>
$ pyupdater pkg --process --sign<br>
$ pyupdater build --console --hidden-import=SocketServer --app-version 0.0.2 run.py<br>
$ pyupdater pkg --process --sign<br>

$ pyupdater archive --name assets --version 0.0.1 --keep assets.txt<br>
</code>
