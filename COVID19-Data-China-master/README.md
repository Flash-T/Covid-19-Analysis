## COVID-19-DATA(CN)

收集[丁香园]( https://ncov.dxy.cn/ncovh5/view/pneumonia?source= )和[腾讯](https://news.qq.com/zt2020/page/feiyan.htm) 相关网站发布的关于新型冠状病毒的数据，每天爬取一次。

> 从丁香园的爬取的数据文件后缀为DXY， 腾讯的为TX，丁香园的数据始于1月24日，仅限于中国的数据，腾讯的数据始于2月3日，包含国外的数据（不可用）数据并未将境外输入病例与国内病例区分，在此说明


### 部署

```bash
pip3 install -r requirements.txt
```

### 运行

```bash
python3 run.py
```
### 停止更新
由于2020-10-23 至2020-10-31之间数据缺失，数据缺失较多，同时由于项目部署在云服务器上，资源有限，故该项目停止更新
