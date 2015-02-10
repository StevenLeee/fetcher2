
The ClearClouds Fetcher Plugin Published and supported by New Relic Platform Team

The ClearClouds Fetcher Plugin enables integrated monitoring  inside of New Relic, include:

一、	Requirement
OS : Red Hat6.2 64bits or later / CentOS6.2 64bits or later
Disk : more then 500G

二、	Tcp
Tcp_Throughput
Tcp_Latency
Tcp_Attack
Tcp_Retransmit
Tcp_CloseState

三、	Http
Http_Latency
Http_StatusCode

四、	Transactions
Transactions_Apdex
Transactions_Error rate
Transactions_Average response time

五、	Alert
most 5 alerting to above items




六、	ISO Download URL :

七、	fetcher Download URL :
http://pan.baidu.com/s/1kTyyt99
or
https://github.com/StevenLeee/fetcher2.git


八、	Install
after download file fetcher-0.1.linux-x86_64.tar.gz, enter download directory
tar -zxvf fetcher-0.1.linux-x86_64.tar.gz
cd fetcher-0.1.linux-x86_64
chmod -R 777  ./*
cp -R ./*  /



九、	configuration

run only once:

fetcher  -d datadir  -n pluginid  -k newrelickey

here :

datadir : your data directory

pluginid : your plugin name,generally server name

newrelickey : your license key from your New Relic account.

e.g :

fetcher -d /home/juyun/datafile/nfcap  -n ClearClouds -k 19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6

or

fetcher  -n ClearClouds

fetcher  -d /home/juyun/datafile/nfcap

fetcher  -k 19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6

until print message as below:
datadir= home/juyun/datafile/nfcap
pluginid= ClearClouds
newrelickey=19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6

十、	Execute fetcher

fetcher -r









