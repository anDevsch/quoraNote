import urllib.request
import re
import urllib.error
for i in range(1,10):
    pageurl="http://www.58pic.com/"
    data=urllib.request.urlopen(pageurl).read().decode("utf-8","ignore")
    pat='<a class="thumb-box".*?src="(.*?)'
    imglist=re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        try:
            thisimg=imglist[j]
            thisimgurl=thisimg+"_1024.jpg"
            file="F:/"+str(i)+str(j)+".jpg"
            urllib.request.urlretrieve(thisimgurl,filename=file)
            print("第"+str(i)+"页"+str(j)+"个图片爬取成功")
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
        except Exception as e:
            print(e)
