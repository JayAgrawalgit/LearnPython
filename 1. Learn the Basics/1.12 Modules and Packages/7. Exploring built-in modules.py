# Check out the full list of built-in modules in the Python standard library here.
# Two very important functions come in handy when exploring modules in Python - the dir and help functions.
# If we want to import the module urllib, which enables us to create read data from URLs, we simply import the module:
# import the library
import urllib

# use it
urllib.urlopen(...)


# We can look for which functions are implemented in each module by using the dir function:


>>> import urllib
>>> dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__',
'__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies',
'_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost',
'_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters',
'_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook',
'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies',
'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os',
'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote',
'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport',
'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1',
'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode',
'urlopen', 'urlretrieve']


# When we find the function in the module we want to use, we can read about it more using the help function, inside the
# Python interpreter:
help(urllib.urlopen)
