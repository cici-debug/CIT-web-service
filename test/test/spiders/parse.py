import lxml.html as lhtml
from lxml.html.clean import Cleaner
from StringIO import StringIO

def html_parse(site_string):

	# tmp = lhtml.parse(url_string)
	site = lhtml.parse(StringIO(site_string))
	cleaner = Cleaner(style=True, links=True, add_nofollow=True, page_structure=False, safe_attrs_only=False)
	html = cleaner.clean_html(site)
	body = html.getroot().cssselect('body')[0]
	
	for ele in body.cssselect('.header'):
		ele.drop_tree()
	for ele in body.cssselect('#header'):
		ele.drop_tree()
	for ele in body.cssselect(".ui-toolkit"):
		ele.drop_tree()
	for ele in body.cssselect('#footer'):
		ele.drop_tree()
	for ele in body.cssselect('nav'):
		ele.drop_tree()


	#exoscale
	for ele in body.cssselect('hgroup'):
		ele.drop_tree()
	#vircurex
	for ele in body.cssselect('.banner'):
		ele.drop_tree()
	#tyntec
	for ele in body.cssselect('.bar'):
		ele.drop_tree()
	#1linx
	for ele in body.cssselect('section'):
		ele.drop_tag()
	#one signal
	for ele in body.cssselect('#hub-header'):
		ele.drop_tree()
	for ele in body.cssselect('header'):
		ele.drop_tag()
	#clever tap
	for ele in body.cssselect('.doc-article__breadcrumb'):
		ele.drop_tree()



	for ele in body.iter():
		if 'div' == ele.tag:
			ele.drop_tag()
	if len(body.cssselect('h1')) > 0:
		for ele in body.cssselect('h1'):
			body = ele.getparent()
			break
	elif len(body.cssselect('h2')) > 0:
		for ele in body.cssselect('h2'):
			body = ele.getparent()
			break
	elif len(body.cssselect('h3')) > 0:
		for ele in body.cssselect('h3'):
			body = ele.getparent()
			break
	elif len(body.cssselect('h4')) > 0:
		for ele in body.cssselect('h4'):
			body = ele.getparent()
			break
	elif len(body.cssselect('h5')) > 0:
		for ele in body.cssselect('h5'):
			body = ele.getparent()
			break
	elif len(body.cssselect('h6')) > 0:
		for ele in body.cssselect('h6'):
			body = ele.getparent()
			break
	fo = open("what.txt", "w+")
	fo.write(lhtml.tostring(body))
	return body