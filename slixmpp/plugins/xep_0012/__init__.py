"""
    Slixmpp: The Slick XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of Slixmpp.

    See the file LICENSE for copying permission.
"""

from slixmpp.plugins.base import register_plugin

from slixmpp.plugins.xep_0012.stanza import LastActivity
from slixmpp.plugins.xep_0012.last_activity import XEP_0012


register_plugin(XEP_0012)


# Retain some backwards compatibility
xep_0004 = XEP_0012
