# Шаги по созданию самоустанавливающегося модуля

Устанавливаем pyinstaller/updater

    $ pip uninstall pyinstaller
    $ pip uninstall pyupdater
    $ pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip 
    $ pip install pyupdater
    $ #pip install --upgrade git+https://github.com/Digital-Sapphire/PyUpdater.git@master 

Готовим репозиторий
    
    $ pyupdater clean
    $ pyupdater init

Генерируем ключ

    $ cd ..
    $ pyupdater keys -c
    $ cd myfolder    
    $ cp ../keypack.pyu .
    $ pyupdater keys --import
    $ rm keypack.pyu

Собираем версию/патч

    $ pyupdater build --console --app-version 0.0.1 run.py
    
... или так, если есть файлы ресурсов
    
    $ pyupdater build --console --app-version 0.0.20 --add-data "../../pyupdatermywx/lua;pyupdatermywx/lua" run.py

Подписываем

    $ pyupdater pkg --process --sign

# Демо доступ к QUIK

    <https://arqatech.com/ru/support/demo/>