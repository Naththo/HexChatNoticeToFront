import hexchat

__module_name__ = "Notice to front"
__module_version__ = "0.1"
__module_description__ = "Prints notices to active window regardless of server"
__author__ = "Nathan (nathh_)"

def addon_unloaded(userdata):
	print "\0034 %s (%s) unloaded." % (__module_name__, __module_version__)

hexchat.hook_unload(addon_unloaded)

print "\0034 %s (%s) loaded." % (__module_name__, __module_version__)