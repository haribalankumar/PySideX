
__version__ = '0.1.2'

try:
    import PySide2
    pyside2_available = True
except ImportError:
    pyside2_available = False
    try:
        import PySide
        pyside_available = True
    except ImportError:
        pyside_available = False
        raise ImportError("Neither 'PySide' nor 'PySide2' is available.")

if pyside2_available:
    from PySide2 import QtCore
    from PySide2 import QtWidgets
    from PySide2 import QtOpenGL
else:
    from PySide import QtCore
    from PySide import QtGui as QtWidgets
    from PySide import QtOpenGL
