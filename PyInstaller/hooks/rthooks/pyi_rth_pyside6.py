#-----------------------------------------------------------------------------
# Copyright (c) 2021, PyInstaller Development Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

import os
import sys

# The path to Qt's components may not default to the wheel layout for
# self-compiled PySide6 installations. Mandate the wheel layout. See
# ``utils/hooks/qt.py`` for more details.
if sys.platform.startswith('win'):
    pyqt_path = os.path.join(sys._MEIPASS, 'PySide6')
else:
    pyqt_path = os.path.join(sys._MEIPASS, 'Qt', 'PySide6')
os.environ['QT_PLUGIN_PATH'] = os.path.join(pyqt_path, 'plugins')
os.environ['QML2_IMPORT_PATH'] = os.path.join(pyqt_path, 'qml')
