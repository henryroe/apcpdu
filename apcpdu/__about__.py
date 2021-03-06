try:
    from astropy_helpers.git_helpers import get_git_devstr
    git_devstr = get_git_devstr(False)
except ImportError:
    git_devstr = ""
    
__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "apcpdu"
__summary__ = "Python module to control APC AP7900 PDU"
__uri__ = "https://github.com/henryroe/apcpdu"

# VERSION should be PEP386 compatible (http://www.python.org/dev/peps/pep-0386)
# pre-release of a version is, e.g. 0.2.1dev1  (0.2.1 is *newer* than 0.2.1dev1)
# post-release of a version is, e.g. 0.2.1-1  (0.2.1 is *older* than 0.2.1-1)
__version__ = "0.1.0dev1"

# Indicates if this version is a release version
RELEASE = 'dev' not in __version__

if not RELEASE:
    __version__ += git_devstr

__author__ = "Henry Roe"
__email__ = "hroe@hroe.me"

__license__ = "MIT License"
__copyright__ = "2016 %s" % __author__
