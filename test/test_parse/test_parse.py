import lxml.html as lhtml
from lxml.html.clean import Cleaner

def html_parse(url_string):
	tmp = lhtml.parse('http://api.eventful.com/docs/events/new')
	cleaner = Cleaner(style=True, links=True, add_nofollow=True, page_structure=False, safe_attrs_only=False)
	html = cleaner.clean_html(tmp)
	body = html.getroot().cssselect('body')[0]
	for ele in body.cssselect('#header'):
		ele.drop_tree()
	for ele in body.cssselect('#footer'):
		ele.drop_tree()
	for ele in body.cssselect('nav'):
		ele.drop_tree()
	for ele in body.iter():
		if 'div' == ele.tag:
		# if len(ele) == 1 and ele.tag != 'body':
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
	# print lhtml.tostring(body)
	return body