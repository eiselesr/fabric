setup:
	sudo apt-get install -y arp-scan
	make atom
	pip3 install Fabric3
	sudo apt-get install -y tmux
	sudo pip3 install python-dotenv
	sudo apt-get install -y libcurl4-openssl-dev
	sudo pip3 install pycurl
	sudo pip3 install influxdb
	sudo timedatectl set-timezone UTC
	cp .tmux.conf ~/
	git config --global core.editor "vim"

atom:
	wget https://atom.io/download/deb -O 'atom.deb'
	sudo apt -y install ./*.deb
	rm *.deb
