import os

class ElementNode(object):
	def __init__(self, ele_tag, ele_text, ele_tail, ele_class, ele_id, ele_style, ele_href, this_tree_node):
		self.__setattr__('tag', ele_tag)
		self.__setattr__('text', ele_text)
		self.__setattr__('tail', ele_tail)
		self.__setattr__('class', ele_class)
		self.__setattr__('id', ele_id)
		self.__setattr__('style', ele_style)
		self.__setattr__('href', ele_href)
		self.__setattr__('tree_node', this_tree_node)

	def __repr__(self):
		tabs = ""
		for i in range(0, self.__getattribute__('tree_node').__getattribute__('layer')):
			tabs += "\t\t\t"
		string = tabs + "\tElement:" + self.__getattribute__('tag') 
		if None != self.__getattribute__('text') and '' != self.__getattribute__('text'):
			string += "\n\t\t" + tabs + self.__getattribute__('text').encode("utf-8")
		if None != self.__getattribute__('tail') and '' != self.__getattribute__('tail'):
			string += "\n\t\t" + tabs + self.__getattribute__('tail').encode("utf-8")
		return string

class TreeNode(object):
	def __init__(self, father_node, node_style, layer):
		self.__setattr__('parent', father_node)
		self.__setattr__('layer', layer)
		self.__setattr__('element', [])
		self.__setattr__('children', [])
		self.__setattr__('style', node_style)

	def __repr__(self):
		tabs = ""
		for i in range(0, self.__getattribute__('layer')):
			tabs += "\t\t\t"
		string = tabs + "Node:\n"+ tabs + "(type) "+ self.__getattribute__('style') + "\n" + tabs + "(layer)" + str(self.__getattribute__('layer')) + "\n" 
		for ele in self.__getattribute__('element'):
			string += repr(ele) + "\n"
		return string

def init_tree():
	tree_root = TreeNode(None, "root", -1)
	return tree_root

def insert_node(father_node, node_style, layer):
	tree_node = TreeNode(father_node, node_style, layer)
	return tree_node

def append_element(tree_node, element_node):
	tree_node.__getattribute__('element').append(element_node)

def append_children(tree_node, children_node):
	tree_node.__getattribute__('children').append(children_node)

def find_children(tree_node, children_node):
	return tree_node.__getattribute__('children').index(children_node)

def insert_children(tree_node, children_node, index):
	tree_node.__getattribute__('children').insert(index, children_node)

def change_layer(tree_node, old_father_node, new_father_node, layer):
	old_father_node.__getattribute__('children').remove(tree_node)
	new_father_node.__getattribute__('children').append(tree_node)
	tree_node.parent = new_father_node
	tree_node.layer = layer

def modify_tree_node(tree_ele, layer):
	father_tree_ele = tree_ele.__getattribute__('parent')
	new_tree_ele = insert_node(father_tree_ele, "c", tree_ele.__getattribute__('layer'))
	index = find_children(father_tree_ele, tree_ele)
	insert_children(father_tree_ele, new_tree_ele, index)
	index += 1
	change_layer(father_tree_ele.children[index], father_tree_ele, new_tree_ele, layer)
	while index < len(father_tree_ele.children) and False == has_h_tree_node(father_tree_ele.children[index], layer):
		change_layer(father_tree_ele.children[index], father_tree_ele, new_tree_ele, layer)

def has_h_tree_node(tree_ele, layer):
	if len(tree_ele.element) > 0 and tree_ele.layer != layer:
		for node_ele in tree_ele.element:
			if -1 != str(node_ele.tag).find("h"+str(layer)):
				return True
		return False
	return False

def check_tree_node(tree_ele, layer):
	if has_h_tree_node(tree_ele, layer):
		modify_tree_node(tree_ele, layer)

def pass_through(tree_ele, layer):
	check_tree_node(tree_ele, layer)
	if len(tree_ele.children) > 0:
		for tree_ele_child in tree_ele.children:
			if "c" == tree_ele_child.style:
				pass_through(tree_ele_child, layer)

def pass_through_print(tree_ele, fo):
	fo.write(repr(tree_ele))
	if len(tree_ele.children) > 0:
		for tree_ele_child in tree_ele.children:
			pass_through_print(tree_ele_child, fo)

def construct_and_save_tree(body, url, name): 
	gfather_tree_node = None
	father_tree_node = None
	this_tree_node = None
	find_h_element = None
	tree_root = init_tree()
	layer = 1
	find_h = False

	while False == find_h:
		for ele in body.iter():
			if -1 != str(ele.tag).find("h" + str(layer)):
				find_h = True
				break
		if False == find_h:
			layer += 1

	# print "num of layer" + str(layer)

	for ele in body.iter():
		if None == this_tree_node:
			new_tree_node = insert_node(tree_root, "c", 0)
			append_children(tree_root, new_tree_node)
			this_tree_node = new_tree_node
		elif -1 != str(ele.tag).find("h" + str(layer)):
			gfather_tree_node = father_tree_node
			father_tree_node = this_tree_node
			new_tree_node = insert_node(father_tree_node, "h" + str(layer), layer)
			append_children(father_tree_node, new_tree_node)
			this_tree_node = new_tree_node
			find_h_element = ele
		elif None == find_h_element:
			continue
			# new_tree_node = insert_node(this_tree_node, "c", layer)
			# append_children(this_tree_node, new_tree_node)
			# father_tree_node = this_tree_node
			# this_tree_node = new_tree_node
		elif ele.getparent() == find_h_element.getparent():
			new_tree_node = insert_node(father_tree_node, "c", layer)
			append_children(father_tree_node, new_tree_node)
			this_tree_node = new_tree_node
		if None != ele.text:
			ele.text = ' '.join(ele.text.split())
		if None != ele.tail:
			ele.tail = ' '.join(ele.tail.split())
		this_ele_node = ElementNode(ele.tag, ele.text, ele.tail, ele.get('class'), ele.get('id'), ele.get('style'), ele.get('href'), this_tree_node)
		append_element(this_tree_node, this_ele_node)

	layer += 1

	while layer < 7:
		pass_through(tree_root, layer)
		layer += 1
	# print url
	if -1 != url.find("com/"):
		# print "here"
		filename = url.split("com/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")
	elif -1 != url.find("io/"):
		filename = url.split("io/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("net/"):
		filename = url.split("net/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("tv/"):
		filename = url.split("tv/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("ly/"):
		filename = url.split("ly/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("co/"):
		filename = url.split("co/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("edu/"):
		filename = url.split("edu/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("info/"):
		filename = url.split("info/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("org/"):
		filename = url.split("org/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	elif -1 != url.find("ch/"):
		filename = url.split("ch/")[1].replace("/", "_").replace(".", "_").replace("#", "_").replace("+", "_").replace("?", "_").replace("=", "_")	
	
	else:
		filename = url.replace("/", "_")
	if not os.path.exists(os.getcwd() + "\\" + name):
		os.makedirs(os.getcwd() + "\\" + name)
		# print "here"
	fo = open(os.getcwd() + "\\" + name + "\\" + filename + ".txt", "w+")

	pass_through_print(tree_root.children[0], fo)
