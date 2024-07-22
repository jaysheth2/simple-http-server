* Log into the VM
* sudo su
* git clone https://github.com/jaysheth2/simple-http-server.git /simple-http-server
* cp /simple-http-server/http-server.service /etc/systemd/system/
* systemctl daemon-reload
* systemctl start http-server
