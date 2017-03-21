import test_parse
import test_block_tree

url = 'http://api.eventful.com/docs/events/new'
body = test_parse.html_parse(url)
test_block_tree.construct_and_save_tree(body, url)
