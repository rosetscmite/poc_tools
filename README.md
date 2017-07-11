# poc_tools Instructions
## 运行环境安装
运行环境：kali系统  
kali镜像下载地址：http://cdimage.kali.org/kali-2017.1/kali-linux-2017.1-amd64.iso  
下载镜像后，通过vmware或vbox安装kali系统。  

## 安装
kali系统下运行
```
git clone https://github.com/rosetscmite/poc_tools.git
cd 目录
./install.py
```
## 运行
主程序auto_attack.py  
目前支持的攻击方式：  
1.port scan                       (端口扫描)  
2.brute force                     (暴力破解攻击)  
3.Sqlinject                       (SQL注入)  
4.Web dir brute attack            (网站目录扫描)  
5.DOS attack                      (DOS攻击)  
6.Hot case             (热点事件复现)  
0.Exit                            (退出)  

攻击包回放程序pcap_review.py  
```
./pcap_review.py
```  

PS：使用中遇到问题或有新的需求，请联系jiaqiang_luo@hansight.com
