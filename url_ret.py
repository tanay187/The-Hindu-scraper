import re
import urllib
import os
import urllib2
map = {}
day = ''
month = '' 
year = ''
map[1]='Front Page'
map[2]='NATIONAL'
map[3]='INTERNATIONAL'
map[4]='OPINION'
map[5]='BUSINESS'
map[6]='SPORT'
#to add new topics to the map: map[i]='<topic>'
def get_date():
	global day,month,year
	day = raw_input('Enter day(dd):')
	month = raw_input('Enter month(mm):')
	year = raw_input('Enter year(yyyy):')
	url_str = "http://www.thehindu.com/archive/print/"+str(year)+"/"+str(month)+"/"+str(day)+"/"
	return url_str

def choices():
	topics = []
	print "1:Front Page\n2:National\n3:International\n4:Opinion\n5:Business\n6:Sport"	
	print "Enter choices separated by a space e.g 1 3 4"
	topic = raw_input().split()
	for top in topic:
		topics.append(int(top))
	return topics

def get_articles(text,topic):
	end_pos = text.find('<div class="line"></div>')
	text = text[:end_pos]
	links = re.findall(r'<a href=\"(.*)\">(.*)</a>',text)
	print 'Topic: '+str(map[topic])
	for link in links:
		path = 'Articles\\'+str(day)+'-'+str(month)+'-'+str(year)+'\\'+map[topic]+'\\'
		if not os.path.exists(path):
			os.makedirs(path)
		file = ''
		for char in link[1]:
			if char >='a' and char <= 'z' or char >='A' and char <= 'Z' or char == ' ':
				file = file + str(char)
		file_path = os.path.join(path,file+".html")	
		urllib.urlretrieve(link[0],file_path)
		print file
	
def parse(text,topics):
	for topic in topics:
		pos = text.find(map[topic])
		links = text[pos:]
		get_articles(links,topic)
		
		
def url_ret():
	url = get_date()
	file = urllib.urlopen(url)
	text = file.read()
	return text
	
def main():
	text = url_ret()
	topics = choices()
	parse(text,topics)
if __name__ == '__main__':
	main()
	