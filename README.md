Clearclouds fetcher plugin

1.	The fetcher plugin published and supported by Clearclouds team.

2.	The fetcher plugin enables integrated monitoring of your Local Traffic Manager devices inside of New Relic.

3.	The fetcher plugin monitor items include:

a)	TCP

i.	Traffic

ii.	Latency

iii.	CloseStatus

iv.	New/Close connection

v.	Retransmited Rate

vi.	Attack

b)	Http

i.	Traffic

ii.	Latency

iii.	StateCode

iv.	Error Rate

v.	Apdex

c)	Transaction

i.	Avg respone time

ii.	Error Rate

iii.	Apdex

d)	Alert

	You can set most 5 alerting items about above all items,each alerting item have caution threhold and critical threhold ,when the item value more then Caution threhold,new relic platform raise a caution alerting in GUI,and when the item value more then critical threhold,new relic platform raise a critical alerting in GUI.
	
	Alerting frequency is once per 30 minute.
	
	New relic platform will send you a email when alert, if you configure this function.


4.	Requirement

	OS : CentOS6.2 64Bits or later
	
	Disk : more then 100G
	
	Memory : more then 4G
	

5.	IProbe.iso Download URL :

6.	About URL : http://www.clearclouds.com/about.htm

7.	Surport URL : http://www.clearclouds.com/surport.htm

8.	fetcher Download URL :

	http://pan.baidu.com/s/1kTyyt99
	
	or
	
	https://github.com/StevenLeee/fetcher2.git
	
9.	Install

a)	download file iProbe.iso

b)	after download file iProbe.iso,do something .

c)	after download file fetcher-0.1.linux-x86_64.tar.gz.

d)	enter download directory

e)	tar -zxvf fetcher-0.1.linux-x86_64.tar.gz

f)	cd fetcher-0.1.linux-x86_64

g)	chmod -R 777  ./*

h)	cp -R ./*  /

10.	configuration

a)	run fetcher only once:

		fetcher  -d datadir  -n pluginid  -k newrelickey
		
		here :
		
		datadir  :  your data directory
		
		pluginid  :  your plugin name,generally server name
		
		newrelickey  :  your license key from your New Relic account.
		
b)	e.g :

		fetcher -d /home/juyun/datafile/nfcap  -n ClearClouds -k 19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6
		
	or
	
		fetcher  -n ClearClouds
		
		fetcher  -d /home/juyun/datafile/nfcap
		
		fetcher  -k 19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6
		
	until print message as below:
	
		datadir= home/juyun/datafile
		
		pluginid= ClearClouds
		
		newrelickey=19e5cb7a2ec9c43a7a90cec3360fb7b5868d08d6

11.	Execute fetcher

	fetcher -r
