# fxtek_GUI-Code
GUI Code v18_1.1 解决了Windows上出现的错误：
1.Email setting面板下的default file is corrupted
2.Save功能的异常
3.send GUI trace
4.test功能异常
如需调试，请可以查看Documents目录下的GUI Code description V1.0CN/Eng.docx文档


修改代码如下：
Email setting面板下的default file is corrupted 修复：
DisplayMenubar.py 1574行：h.update(f.read().replace("\r",'')) #compatible Windows 7

send GUI trace异常修复：
ControlDiag.py  157行：LX_zip_files=[]      #用来存放LX...zip
ControlDiag.py  173-179为新加代码
ControlDiag.py  181行 file_to_send = newest_file.replace('/', ' ').replace('\\',' ').split()[-1]
ControlEmail.py  156行，新增fp.close() 

Save功能的异常修复：
DisplayMenubar.py 1672行：h.update(f.read().replace("\r",'')) #fix save button 

Test功能异常修复：
ControlEmail.py 48行新增   TO =[recipent for recipent in TO if recipent.replace(" ","")] 
ControlEmail.py 114行新增   TO =[recipent for recipent in TO if recipent.replace(" ","")] 