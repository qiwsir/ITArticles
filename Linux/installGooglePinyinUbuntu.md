#Install Googlepinyin on Ubuntu

1. To install the dependencies, you can run:

    sudo apt-get install cmake build-essential opencc mercurial ibus

2. download libgooglepinyin: https://libgooglepinyin.googlecode.com/files/libgooglepinyin-0.1.2.tar.bz2

3. run next step:

    tar -jxvf libgooglepinyin-0.1.2.tar.bz2
    cd libgooglepinyin
    mkdir build; cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr

    make
    sudo make install

4. reload ibus

    pkill -f ibus-daemon ; ibus-daemon -d -x

5. add Googlepinyin in "System Settings-Text Entry"
