import urllib2
import simplejson as json
import random
import webbrowser

f = open('movie.txt', 'r')
final1=open('grid.html','w')
tt="""<head>\n<style>\ntd{text-align:center;}\n</style>\n
    </head>\n<body>\n<center>\n<h1>Your Movies</h1>\n<table style=\"width:100%\"><tr>\n"""
final1.write(tt)
data=f.read()
data=data.split('\n')
random.shuffle(data)
data_10=data
data_10=data_10[0:10]
data = [x for x in data if x not in data_10]


"""f1=open('json.txt','a')
for i in data:
    i=i.replace(" ","+")
    url="http://www.omdbapi.com/?t="+i+"&y=&plot=short&r=json"
    print url
    page =urllib2.urlopen(url)
    f1.write(page.read())
"""

#data_10=['Beauty and the Beast']
dic={}
cc=0
for i in data_10:
    i=i.replace(" ","+")
    url="http://www.omdbapi.com/?t="+i+"&y=&plot=short&r=json"
    page =urllib2.urlopen(url)
    data1 = json.load(page)
    #print data1['Title'],'->',data1['Genre']
    print data1['Title']
    ii=raw_input("Y/N ")
    ii=ii.lower()
    if ii=='y':
        titl=str(data1['Title'])
        genr=str(data1['Genre'])
        dic[titl]=genr
        if cc%3==0:
            final1.write("</tr>\n<br><tr>")
        final1.write("\n<td><img src=\""+data1["Poster"]+"\"><br><h3>"+data1['Title']+"</h3><br></td>")
        cc=cc+1
final1.write("\n</tr></table>\n<br>\n<h1>Our Predictions</h1>\n<table style=\"width:100%\"><tr>")
print
#print dic
print "Finding match for you. Please wait."
result = {}
for key,value in dic.items():
    if value not in result.values():
        result[key] = value
dic=result
#print dic
cc=0
for key,value in dic.items():
    c=0    
    flag=0
    lm=[]
    lm.append(key)
    print "Estimating ",cc+1
    #print key,"->",value
    for i in data:
        i=i.replace(" ","+")
        url="http://www.omdbapi.com/?t="+i+"&y=&plot=short&r=json"
        page =urllib2.urlopen(url)
        #print type(page)
        data1 = json.load(page)
        #print type(data1)
        #print data1['Title']
        if value==data1['Genre']:
            if data1['Title'] in lm:
                continue
            #print data1['Title'],'->',data1['Genre']
            if cc%3==0:
                final1.write("</tr>\n<br><tr>")
            final1.write("<td><img src=\""+data1["Poster"]+"\"><br><h3>"+data1['Title']+"</h3><br></td>\n")
            cc=cc+1
            lm.append(data1['Title'])
            c=c+1
            if c==3:
                flag=1
                break
    if (c<2 and flag!=1):
        g1=value       
        for i in data:
            i=i.replace(" ","+")
            url="http://www.omdbapi.com/?t="+i+"&y=&plot=short&r=json"
            page =urllib2.urlopen(url)
            data1 = json.load(page)
            dd=data1['Genre'].split(',')
            gg=g1.split(',')
            if "Animation" in gg:
                break
            #print dd
            #print gg
            ne=list(set(dd).intersection(gg))
            nn=len(ne)
            #print nn
            if g1 in data1['Genre'] or nn>=2:
                if data1['Title'] in lm:
                    continue
                #print "new1",data1['Title'],'->',data1['Genre']
                if cc%3==0:
                    final1.write("</tr>\n<br><tr>")
                final1.write("<td><img src=\""+data1["Poster"]+"\"><br><h3>"+data1['Title']+"</h3><br></td>\n")
                cc=cc+1
                lm.append(data1['Title'])
                c=c+1
                if c==3:
                    flag=1
                    break
    if(c<2 and flag!=1):
        if value=='Adventure, Drama, Thriller':
            g1='Adventure, Thriller'
        if value=='Horror, Sci-Fi':
            g1='Horror'
        elif value=='Adventure, Family, Fantasy':
            g1='Adventure, Fantasy'
        elif value=='Comedy, Romance' or value=='Drama, Romance, Sci-Fi':
            g1='Comedy, Drama, Romance'
        elif value=='Adventure, Drama, Sci-Fi':
            g1='Adventure, Sci-Fi'
        elif value=='Drama, Mystery, Sci-Fi':
            g1='Drama, Mystery'
        elif value=='Animation, Family, Fantasy' or value=='Animation, Adventure, Family':
            g1='Animation, Comedy, Family'
        elif value=='Animation, Comedy, Family':
            g1='Animation, Family, Fantasy'
        elif value=='Animation, Action, Comedy' or value=='Animation, Adventure, Drama' or value=='Animation, Action, Adventure':
            g1='Animation, Adventure'
        #print g1
        for i in data:
            i=i.replace(" ","+")
            url="http://www.omdbapi.com/?t="+i+"&y=&plot=short&r=json"
            page =urllib2.urlopen(url)
            data1 = json.load(page)
            if g1 in data1['Genre']:
                if data1['Title'] in lm:
                    continue
                #print "new2",data1['Title'],'->',data1['Genre']
                if cc%3==0:
                    final1.write("</tr>\n<br><tr>")
                final1.write("<td><img src=\""+data1["Poster"]+"\"<br><h3>"+data1['Title']+"</h3><br></td>\n")
                cc=cc+1
                lm.append(data1['Title'])
                c=c+1
                if c==3:
                    flag=1
                    break    
    print
final1.write("</table></center></body>")
final1.close()
url="grid.html"
webbrowser.open(url, new=0)
