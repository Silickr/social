# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re

def getPicture(page):
    req = urllib2.Request('http://www.budejie.com/pic/%s'%page)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    html = urllib2.urlopen(req).read()
    reg_picture = r'(j-r-list-c-img">\n\s*<a.*\n\s.*<img.*\s*class="lazy"\s*.+title)'
    pictureNameTxt = "picture.txt"
    content = re.findall(reg_picture,html)
    file_Obj = open(pictureNameTxt,'a')
    for i in content:
        pictureUrl = i.split('"')[8]
        pictureName = pictureUrl.split("/")[-1]
        file_Obj.writelines(pictureUrl+'\n')
#        urllib.urlretrieve(pictureUrl,"picture/%s" %pictureName)
        print pictureName
    file_Obj.close()
#    print "write successful!"

for i in range(0,5):
    getPicture(i)
print "over!"