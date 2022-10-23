#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2010      Jakim Friant
# Copyright (C) 2022      Christopher Horn
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
LastModified Gramplet Registration
"""

#------------------------------------------------------------------------
#
# LastModified Gramplet Registration
#
#------------------------------------------------------------------------
register(
    GRAMPLET,
    id="LastModified",
    name=_("Last Modified"),
    description=_("List the most recent records that have been modified"),
    status=STABLE,
    version="0.99",
    fname="last_modified.py",
    authors=["Jakim Friant", "Christopher Horn"],
    authors_email=["jmodule@friant.org"],
    height=170,
    gramplet="LastModified",
    gramps_target_version="5.1",
    gramplet_title=_("Last Modified"),
    help_url="Addon:Last_Modified",
)
