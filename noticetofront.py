import hexchat

__module_name__ = "Notice to front"
__module_version__ = "0.1"
__module_description__ = "Prints notices to active window regardless of server"
__author__ = "Nathan (nathh_)"

def processNotice(word, word_eol, userdata):
	current_tab = hexchat.find_context()
	if not current_tab:
		return hexchat.EAT_NONE

	nick = word[0].split("!")[0].replace(":", "")
	noticecontent = word[3][1:len(word[3])]
	if nick and noticecontent:
		notice_network = hexchat.get_info("network")
		notice_host = hexchat.get_info("host")
		currenttab_network = current_tab.get_info("network")
		if notice_network == currenttab_network:
			current_tab.emit_print("Notice", nick, noticecontent)
		else:
			current_tab.emit_print("Notice", nick, "(%s / %s): %s" % (notice_network, notice_host, noticecontent))
	return hexchat.EAT_ALL
hexchat.hook_server("NOTICE", processNotice)

def addon_unloaded(userdata):
	print "\0034 %s (%s) unloaded." % (__module_name__, __module_version__)
hexchat.hook_unload(addon_unloaded)

print "\0034 %s (%s) loaded." % (__module_name__, __module_version__)