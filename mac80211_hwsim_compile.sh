extraversion=-041600-generic
mkdir -p ~/tmp/build/
cp /boot/config-`uname -r` ~/tmp/build/.config
cp /usr/src/linux-headers-4.16.0-041600-generic/Module.symvers ~/tmp/build/./
make EXTRAVERSION=-041600-generic O=~/tmp/build oldconfig
make EXTRAVERSION=-041600-generic O=~/tmp/build prepare
make EXTRAVERSION=-041600-generic O=~/tmp/build outputmakefile
make EXTRAVERSION=-041600-generic O=~/tmp/build archprepare
make EXTRAVERSION=-041600-generic O=~/tmp/build archprepare
make EXTRAVERSION=-041600-generic O=~/tmp/build scripts
make EXTRAVERSION=-041600-generic O=~/tmp/build modules SUBDIRS=drivers/net/wireless
sudo chown root:root ~/tmp/build/drivers/net/wireless/mac80211_hwsim.ko
sudo chmod 644 ~/tmp/build/drivers/net/wireless/mac80211_hwsim.ko
sudo mv ~/tmp/build/drivers/net/wireless/mac80211_hwsim.ko /lib/modules/4.16.0-041600-generic/kernel/drivers/net/wireless/
