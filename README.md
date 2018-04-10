# mac80211_hwsim

* Download linux-4.16.0 from kernel.org
* Copy compile script to linux-4.16.0 root directory
* Modify drivers/net/wireless/Makefile to just compile mac80211_hwsim
* Verify compilation paths in compilation script
* Install libelf-dev, bison, build-essential, linux-headers-generic, dkms (maybe more)
* Run script. There may be errors run "make mrproper" in linux root. Or make scripts.
* Test new driver: modprobe mac80211_hwsim
