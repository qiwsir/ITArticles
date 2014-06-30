#python标准模块和第三方库

##数学计算：

    numbers — Numeric abstract base classes
    math — Mathematical functions
    cmath — Mathematical functions for complex numbers
    decimal — Decimal fixed point and floating point arithmetic
    fractions — Rational numbers
    random — Generate pseudo-random numbers
    itertools — Functions creating iterators for efficient looping
    functools — Higher-order functions and operations on callable objects
    operator — Standard operators as functions

##文件和目录访问：

    os.path — Common pathname manipulations
    fileinput — Iterate over lines from multiple input streams
    stat — Interpreting stat() results
    statvfs — Constants used with os.statvfs()
    filecmp — File and Directory Comparisons
    tempfile — Generate temporary files and directories
    glob — Unix style pathname pattern expansion
    fnmatch — Unix filename pattern matching
    linecache — Random access to text lines
    shutil — High-level file operations
    dircache — Cached directory listings
    macpath — Mac OS 9 path manipulation functions

##数据持久化:

    pickle — Python object serialization
    cPickle — A faster pickle
    copy_reg — Register pickle support functions
    shelve — Python object persistence
    marshal — Internal Python object serialization
    anydbm — Generic access to DBM-style databases
    whichdb — Guess which DBM module created a database
    dbm — Simple “database” interface
    gdbm — GNU’s reinterpretation of dbm
    dbhash — DBM-style interface to the BSD database library
    bsddb — Interface to Berkeley DB library
    dumbdbm — Portable DBM implementation
    sqlite3 — DB-API 2.0 interface for SQLite databases


##通用操作系统服务:

    os — Miscellaneous operating system interfaces
    io — Core tools for working with streams
    time — Time access and conversions
    argparse — Parser for command-line options, arguments and sub-commands
    optparse — Parser for command line options
    getopt — C-style parser for command line options
    logging — Logging facility for Python
    logging.config — Logging configuration
    logging.handlers — Logging handlers
    getpass — Portable password input
    curses — Terminal handling for character-cell displays
    curses.textpad — Text input widget for curses programs
    curses.ascii — Utilities for ASCII characters
    curses.panel — A panel stack extension for curses
    platform — Access to underlying platform’s identifying data
    errno — Standard errno system symbols
    ctypes — A foreign function library for Python

##可选的操作系统服务:

    select — Waiting for I/O completion
    threading — Higher-level threading interface
    thread — Multiple threads of control
    dummy_threading — Drop-in replacement for the threading module
    dummy_thread — Drop-in replacement for the thread module
    multiprocessing — Process-based “threading” interface
    mmap — Memory-mapped file support
    readline — GNU readline interface
    rlcompleter — Completion function for GNU readline


##进程间通信和网络:

    subprocess — Subprocess management
    socket — Low-level networking interface
    ssl — TLS/SSL wrapper for socket objects
    signal — Set handlers for asynchronous events
    popen2 — Subprocesses with accessible I/O streams
    asyncore — Asynchronous socket handler
    asynchat — Asynchronous socket command/response handler


##互联网数据处理:

    email — An email and MIME handling package
    json — JSON encoder and decoder
    mailcap — Mailcap file handling
    mailbox — Manipulate mailboxes in various formats
    mhlib — Access to MH mailboxes
    mimetools — Tools for parsing MIME messages
    mimetypes — Map filenames to MIME types
    MimeWriter — Generic MIME file writer
    mimify — MIME processing of mail messages
    multifile — Support for files containing distinct parts
    rfc822 — Parse RFC 2822 mail headers
    base64 — RFC 3548: Base16, Base32, Base64 Data Encodings
    binhex — Encode and decode binhex4 files
    binascii — Convert between binary and ASCII
    quopri — Encode and decode MIME quoted-printable data
    uu — Encode and decode uuencode files


##结构化标记处理工具:

    HTMLParser — Simple HTML and XHTML parser
    sgmllib — Simple SGML parser
    htmllib — A parser for HTML documents
    htmlentitydefs — Definitions of HTML general entities
    XML Processing Modules
    XML vulnerabilities
    xml.etree.ElementTree — The ElementTree XML API
    xml.dom — The Document Object Model API
    xml.dom.minidom — Minimal DOM implementation
    xml.dom.pulldom — Support for building partial DOM trees
    xml.sax — Support for SAX2 parsers
    xml.sax.handler — Base classes for SAX handlers
    xml.sax.saxutils — SAX Utilities
    xml.sax.xmlreader — Interface for XML parsers
    xml.parsers.expat — Fast XML parsing using Expat


##互联网协议和技术支持:

    webbrowser — Convenient Web-browser controller
    cgi — Common Gateway Interface support
    cgitb — Traceback manager for CGI scripts
    wsgiref — WSGI Utilities and Reference Implementation
    urllib — Open arbitrary resources by URL
    urllib2 — extensible library for opening URLs
    httplib — HTTP protocol client
    ftplib — FTP protocol client
    poplib — POP3 protocol client
    imaplib — IMAP4 protocol client
    nntplib — NNTP protocol client
    smtplib — SMTP protocol client
    smtpd — SMTP Server
    telnetlib — Telnet client
    uuid — UUID objects according to RFC 4122
    urlparse — Parse URLs into components
    SocketServer — A framework for network servers
    BaseHTTPServer — Basic HTTP server
    SimpleHTTPServer — Simple HTTP request handler
    CGIHTTPServer — CGI-capable HTTP request handler
    cookielib — Cookie handling for HTTP clients
    Cookie — HTTP state management
    xmlrpclib — XML-RPC client access
    SimpleXMLRPCServer — Basic XML-RPC server
    DocXMLRPCServer — Self-documenting XML-RPC server

##第三方常用的50个库

    Graphical interface     wxPython     http://wxpython.org    
    Graphical interface     pyGtk     http://www.pygtk.org    
    Graphical interface     pyQT     http://www.riverbankcomputing.co.uk/pyqt/    
    Graphical interface     Pmw     http://pmw.sourceforge.net/    
    Graphical interface     Tkinter 3000     http://effbot.org/zone/wck.htm    
    Graphical interface     Tix     http://tix.sourceforge.net/    
           
    Database     MySQLdb     http://sourceforge.net/projects/mysql-python    
    Database     PyGreSQL     http://www.pygresql.org/    
    Database     Gadfly     http://gadfly.sourceforge.net/    
    Database     SQLAlchemy     http://www.sqlalchemy.org/    
    Database     psycopg     http://www.initd.org/pub/software/psycopg/    
    Database     kinterbasdb     http://kinterbasdb.sourceforge.net/    
    Database     cx_Oracle     http://www.cxtools.net/default.aspx?nav=downloads    
    Database     pySQLite     http://initd.org/tracker/pysqlite    
           
    MSN Messenger     msnlib     http://auriga.wearlab.de/~alb/msnlib/    
    MSN Messenger     pymsn     http://telepathy.freedesktop.org/wiki/Pymsn    
    MSN Messenger     msnp     http://msnp.sourceforge.net/    
    Network     Twisted     http://twistedmatrix.com/    
    Images     PIL     http://www.pythonware.com/products/pil/    
    Images     gdmodule     http://newcenturycomputers.net/projects/gdmodule.html    
    Images     VideoCapture     http://videocapture.sourceforge.net/    
                
    Sciences and Maths     scipy     http://www.scipy.org/    
    Sciences and Maths     NumPy     http://numpy.scipy.org//    
    Sciences and Maths     numarray     http://www.stsci.edu/resources/software_hardware/numarray    
    Sciences and Maths     matplotlib     http://matplotlib.sourceforge.net/    
               
    Games     Pygame     http://www.pygame.org/news.html    
    Games     Pyglet     http://www.pyglet.org/    
    Games     PySoy     http://www.pysoy.org/    
    Games     pyOpenGL     http://pyopengl.sourceforge.net/    
               
    Jabber     jabberpy     http://jabberpy.sourceforge.net/    
               
    Web     scrape     http://zesty.ca/python/scrape.html    
    Web     Beautiful Soup     http://crummy.com/software/BeautifulSoup    
    Web     pythonweb     http://www.pythonweb.org/    
    Web     mechanize     http://wwwsearch.sourceforge.net/mechanize/    
               
    Localisation     geoname.py     http://www.zindep.com/blog-zindep/Geoname-python/    
               
    Serial port     pySerial     http://pyserial.sourceforge.net/    
    Serial port     USPP     http://ibarona.googlepages.com/uspp    
           
    Parallel Port     pyParallel     http://pyserial.sourceforge.net/pyparallel.html    
           
    USB Port     pyUSB     http://bleyer.org/pyusb/    
           
    Windows     ctypes     http://starship.python.net/crew/theller/ctypes/    
    Windows     pywin32     http://sourceforge.net/projects/pywin32/    
    Windows     pywinauto     http://www.openqa.org/pywinauto/    
    Windows     pyrtf     http://pyrtf.sourceforge.net/    
    Windows     wmi     http://timgolden.me.uk/python/wmi.html    
               
    PDA/GSM/Mobiles     pymo     http://www.awaretek.com/pymo.html    
    PDA/GSM/Mobiles     pyS60     http://sourceforge.net/projects/pys60    
               
    Sound     pySoundic     http://pysonic.sourceforge.net/    
    Sound     pyMedia     http://pymedia.org/    
    Sound     FMOD     http://www.fmod.org/    
    Sound     pyMIDI     http://www.cs.unc.edu/Research/assist/developer.shtml    
           
    GMail     libgmail     http://libgmail.sourceforge.net/    
    Google     pyGoogle     http://pygoogle.sourceforge.net/    
    Expect     pyExpect     http://pexpect.sourceforge.net/    
    WordNet     pyWordNet     http://osteele.com/projects/pywordnet/    
    Command line     cmd     http://blog.doughellmann.com/2008/05/pymotw-cmd.html    
    Compiler backend     llvm-py     http://mdevan.nfshost.com/llvm-py/    
    3D     VPython     http://vpython.org

来源：http://www.qy7788.com.cn/shiyongxinxi/shiyongxinxi209.html

