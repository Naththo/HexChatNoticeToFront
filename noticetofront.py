from pprint import pprint
from string import Template
import hexchat

__module_name__ = "Notice to front"
__module_version__ = "0.1"
__module_description__ = "Prints notices to active window regardless of server"
__author__ = "Nathan (nathh_)"


current_tab = ""

def processNotice(word, word_eol, userdata):
	global current_tab
	current_tab_name = current_tab.get_info
	if not current_tab:
		return hexchat.EAT_NONE

	nick = word[0].split("!")[0].replace(":", "")
	noticecontent = word[3][1:len(word[3])]
	if nick and noticecontent:
		current_tab.emit_print("Notice", nick, "(%s / %s): %s" % (hexchat.get_info("network"), hexchat.get_info("host"), noticecontent))
	return hexchat.EAT_ALL
hexchat.hook_server("NOTICE", processNotice)

def focusedTab(word, word_eol, userdata):
	global current_tab
	current_tab = hexchat.find_context(hexchat.get_info("network"))
hexchat.hook_print("Focus Tab", focusedTab)

def addon_unloaded(userdata):
	print "\0034 %s (%s) unloaded." % (__module_name__, __module_version__)
hexchat.hook_unload(addon_unloaded)

print "\0034 %s (%s) loaded. You may need to reselect the tab of your choice to activate the plugin." % (__module_name__, __module_version__)