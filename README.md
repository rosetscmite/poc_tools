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
5.DOS attack                      (DOS攻击)  （不建议使用，经过测试Enterprise接收不了突发大量数据）  
99.Hot case             (热点事件复现)   
0.Exit                            (退出)    

## 触发告警需要的日志和事件
- port scan  
  - 接入日志：防火墙会话日志/防火墙访问日志  
  - 事件：网络连接  
- brute force   
  - 接入日志：系统登陆日志/应用认证日志（ps：ftp等）  
  - 事件：账号登陆/ssh登陆/ftp登陆等  
- sqlinject  
  - 接入日志：web应用日志/WAF日志/IDS日志等  
  - 事件：web访问/websql注入攻击/webxss攻击等（Enterprise内置WAF自动生成内部事件）  
- web dir brute attack  
  - 接入日志：web应用日志/WAF日志/IDS日志等  
  - 事件：web访问
- DOS attack  
  - 接入日志：防火墙会话日志  
  - 事件：网络连接  
- host case  
  - Wanacry  
   - 接入日志：DNS服务器解析日志/Hansight NTA/防火墙会话日志  
   - 事件：DNS查询/网络连接  

攻击包回放程序pcap_review.py  
```
./pcap_review.py
```  

PS：使用中遇到问题或有新的需求，请联系jiaqiang_luo@hansight.com
