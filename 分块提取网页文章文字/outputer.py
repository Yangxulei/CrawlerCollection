#coding:utf-8
        
def output_html(datas):
   
    fout=open("resualt.txt","w")
    fout.write(datas['url']+'\n')
    fout.write("{'post':")
    fout.write(datas['content'])
    fout.write(",title:")
    fout.write(datas['title'])
    fout.write(",publish_data:")
    fout.write(datas['time'])
    fout.write("'replys':["+'\n')
    fout.write("{'content':")
    fout.write(datas['replys'])
    fout.write("}]}"+'\n')
    fout.close()

