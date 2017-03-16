#coding:utf-8
import downloader, outputer,extract
     
def craws(root_url):
    global count
    datas={}
    try:#加入异常处理，有的网页打开没有数据 
        print count ,' %s' % (root_url)
        count=count+1
        cont = downloader.download(root_url) #获取完url，就要去下载它
        datas=extract.extract(cont, root_url)#下载新的数据，那么我们就要去处理它----核心
        outputer.output_html(datas)  
 
    except:
        count=count+1
        print (count,"Eor!")
             
                        
if __name__ == "__main__":
    count = 1
    fa = open("bbs_urls.txt", "r")  
    for line in fa: 
        root_url = line 
        craws(root_url)
    fa.close();