#-----------------------------------------------------------------------------
# Copyright (c) 2021, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------
from PyInstaller.utils.hooks.qt import add_qt6_dependencies, \
    pyside6_library_info, get_qt_network_ssl_binaries

hiddenimports, binaries, datas = add_qt6_dependencies(__file__)
binaries += get_qt_network_ssl_binaries(pyside6_library_info)
