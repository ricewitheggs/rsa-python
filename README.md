<<<<<<< HEAD
#RSA Algorithm

[TOC]

##Sourcefile Tree

	cipher
	│  cipher.txt
	│  ekey.txt
	│  nkey.txt
	│  plain.txt
	│  README.md
	│  rsa.py
	│  setup.py
	│
	├─keys
	│      d.txt
	│      e.txt
	│      n.txt
	│      p.txt
	│      q.txt
	│
	└─lib
			key.py
			key.pyc
			prime.py
			prime.pyc
			__init__.py
			__init__.pyc

###File Description

* Files listed above are mostly established and edited during the coding stage
* Folder 'lib' contains modules writen to generate keys
* Folder 'keys' contains default paths of files to save keys
* File 'rsa.py' works as the main program
* File 'setup.py' transfers the whole program from '*.py' into 'rsa.exe'

##Usage

    rsa [-h] -p PLAINFILE [-n NFILE] [-e EFILE] [-d DFILE] -c CIPHERFILE

	optional arguments:

		-h,--help ==> show help instrutions
		-p ==> choose plainfile path
		[-n] ==> choose nkey path
		[-e] ==> choose ekey path
		[-d] ==> choose dkey path
		-c ==> choose cipherfile path

###Mode

choose one of the following  modes for what U want

	'enc':encryption	generates all keys needed and decodes plainfile with unicode before encryption
	'tes':testing	   encrypt with keys all given 
	'dec':decryption	decrypt with private keys given


##Packaged Version

###File Tree

	cipher:.
	│  cipher.txt
	│  ekey.txt
	│  fileTree.txt
	│  nkey.txt
	│  plain.txt
	│  README.html
	│  README.md
	│  rsa.py
	│  RSA实验报告.doc
	│  setup.py
	│  
	├─build
	│  └─bdist.win32
	│      └─winexe
	│          ├─bundle-2.7
	│          │      python27.dll
	│          │      
	│          ├─collect-2.7
	│          │  │  abc.pyo
	│          │  │  argparse.pyo
	│          │  │  atexit.pyo
	│          │  │  base64.pyo
	│          │  │  bdb.pyo
	│          │  │  bz2.pyd
	│          │  │  calendar.pyo
	│          │  │  cmd.pyo
	│          │  │  codecs.pyo
	│          │  │  collections.pyo
	│          │  │  copy.pyo
	│          │  │  copy_reg.pyo
	│          │  │  difflib.pyo
	│          │  │  dis.pyo
	│          │  │  doctest.pyo
	│          │  │  dummy_thread.pyo
	│          │  │  fnmatch.pyo
	│          │  │  functools.pyo
	│          │  │  genericpath.pyo
	│          │  │  getopt.pyo
	│          │  │  gettext.pyo
	│          │  │  hashlib.pyo
	│          │  │  heapq.pyo
	│          │  │  inspect.pyo
	│          │  │  io.pyo
	│          │  │  keyword.pyo
	│          │  │  linecache.pyo
	│          │  │  locale.pyo
	│          │  │  ntpath.pyo
	│          │  │  opcode.pyo
	│          │  │  optparse.pyo
	│          │  │  os.pyo
	│          │  │  os2emxpath.pyo
	│          │  │  pdb.pyo
	│          │  │  pickle.pyo
	│          │  │  posixpath.pyo
	│          │  │  pprint.pyo
	│          │  │  quopri.pyo
	│          │  │  random.pyo
	│          │  │  re.pyo
	│          │  │  repr.pyo
	│          │  │  select.pyd
	│          │  │  shlex.pyo
	│          │  │  sre.pyo
	│          │  │  sre_compile.pyo
	│          │  │  sre_constants.pyo
	│          │  │  sre_parse.pyo
	│          │  │  stat.pyo
	│          │  │  string.pyo
	│          │  │  StringIO.pyo
	│          │  │  stringprep.pyo
	│          │  │  struct.pyo
	│          │  │  subprocess.pyo
	│          │  │  tempfile.pyo
	│          │  │  textwrap.pyo
	│          │  │  threading.pyo
	│          │  │  token.pyo
	│          │  │  tokenize.pyo
	│          │  │  traceback.pyo
	│          │  │  types.pyo
	│          │  │  unicodedata.pyd
	│          │  │  UserDict.pyo
	│          │  │  warnings.pyo
	│          │  │  weakref.pyo
	│          │  │  zipextimporter.pyo
	│          │  │  _abcoll.pyo
	│          │  │  _hashlib.pyd
	│          │  │  _strptime.pyo
	│          │  │  _threading_local.pyo
	│          │  │  _weakrefset.pyo
	│          │  │  __future__.pyo
	│          │  │  
	│          │  ├─encodings
	│          │  │      aliases.pyo
	│          │  │      ascii.pyo
	│          │  │      base64_codec.pyo
	│          │  │      big5.pyo
	│          │  │      big5hkscs.pyo
	│          │  │      bz2_codec.pyo
	│          │  │      charmap.pyo
	│          │  │      cp037.pyo
	│          │  │      cp1006.pyo
	│          │  │      cp1026.pyo
	│          │  │      cp1140.pyo
	│          │  │      cp1250.pyo
	│          │  │      cp1251.pyo
	│          │  │      cp1252.pyo
	│          │  │      cp1253.pyo
	│          │  │      cp1254.pyo
	│          │  │      cp1255.pyo
	│          │  │      cp1256.pyo
	│          │  │      cp1257.pyo
	│          │  │      cp1258.pyo
	│          │  │      cp424.pyo
	│          │  │      cp437.pyo
	│          │  │      cp500.pyo
	│          │  │      cp720.pyo
	│          │  │      cp737.pyo
	│          │  │      cp775.pyo
	│          │  │      cp850.pyo
	│          │  │      cp852.pyo
	│          │  │      cp855.pyo
	│          │  │      cp856.pyo
	│          │  │      cp857.pyo
	│          │  │      cp858.pyo
	│          │  │      cp860.pyo
	│          │  │      cp861.pyo
	│          │  │      cp862.pyo
	│          │  │      cp863.pyo
	│          │  │      cp864.pyo
	│          │  │      cp865.pyo
	│          │  │      cp866.pyo
	│          │  │      cp869.pyo
	│          │  │      cp874.pyo
	│          │  │      cp875.pyo
	│          │  │      cp932.pyo
	│          │  │      cp949.pyo
	│          │  │      cp950.pyo
	│          │  │      euc_jisx0213.pyo
	│          │  │      euc_jis_2004.pyo
	│          │  │      euc_jp.pyo
	│          │  │      euc_kr.pyo
	│          │  │      gb18030.pyo
	│          │  │      gb2312.pyo
	│          │  │      gbk.pyo
	│          │  │      hex_codec.pyo
	│          │  │      hp_roman8.pyo
	│          │  │      hz.pyo
	│          │  │      idna.pyo
	│          │  │      iso2022_jp.pyo
	│          │  │      iso2022_jp_1.pyo
	│          │  │      iso2022_jp_2.pyo
	│          │  │      iso2022_jp_2004.pyo
	│          │  │      iso2022_jp_3.pyo
	│          │  │      iso2022_jp_ext.pyo
	│          │  │      iso2022_kr.pyo
	│          │  │      iso8859_1.pyo
	│          │  │      iso8859_10.pyo
	│          │  │      iso8859_11.pyo
	│          │  │      iso8859_13.pyo
	│          │  │      iso8859_14.pyo
	│          │  │      iso8859_15.pyo
	│          │  │      iso8859_16.pyo
	│          │  │      iso8859_2.pyo
	│          │  │      iso8859_3.pyo
	│          │  │      iso8859_4.pyo
	│          │  │      iso8859_5.pyo
	│          │  │      iso8859_6.pyo
	│          │  │      iso8859_7.pyo
	│          │  │      iso8859_8.pyo
	│          │  │      iso8859_9.pyo
	│          │  │      johab.pyo
	│          │  │      koi8_r.pyo
	│          │  │      koi8_u.pyo
	│          │  │      latin_1.pyo
	│          │  │      mac_arabic.pyo
	│          │  │      mac_centeuro.pyo
	│          │  │      mac_croatian.pyo
	│          │  │      mac_cyrillic.pyo
	│          │  │      mac_farsi.pyo
	│          │  │      mac_greek.pyo
	│          │  │      mac_iceland.pyo
	│          │  │      mac_latin2.pyo
	│          │  │      mac_roman.pyo
	│          │  │      mac_romanian.pyo
	│          │  │      mac_turkish.pyo
	│          │  │      mbcs.pyo
	│          │  │      palmos.pyo
	│          │  │      ptcp154.pyo
	│          │  │      punycode.pyo
	│          │  │      quopri_codec.pyo
	│          │  │      raw_unicode_escape.pyo
	│          │  │      rot_13.pyo
	│          │  │      shift_jis.pyo
	│          │  │      shift_jisx0213.pyo
	│          │  │      shift_jis_2004.pyo
	│          │  │      string_escape.pyo
	│          │  │      tis_620.pyo
	│          │  │      undefined.pyo
	│          │  │      unicode_escape.pyo
	│          │  │      unicode_internal.pyo
	│          │  │      utf_16.pyo
	│          │  │      utf_16_be.pyo
	│          │  │      utf_16_le.pyo
	│          │  │      utf_32.pyo
	│          │  │      utf_32_be.pyo
	│          │  │      utf_32_le.pyo
	│          │  │      utf_7.pyo
	│          │  │      utf_8.pyo
	│          │  │      utf_8_sig.pyo
	│          │  │      uu_codec.pyo
	│          │  │      zlib_codec.pyo
	│          │  │      __init__.pyo
	│          │  │      
	│          │  ├─lib
	│          │  │      key.pyo
	│          │  │      prime.pyo
	│          │  │      __init__.pyo
	│          │  │      
	│          │  ├─logging
	│          │  │      __init__.pyo
	│          │  │      
	│          │  └─unittest
	│          │          case.pyo
	│          │          loader.pyo
	│          │          main.pyo
	│          │          result.pyo
	│          │          runner.pyo
	│          │          signals.pyo
	│          │          suite.pyo
	│          │          util.pyo
	│          │          __init__.pyo
	│          │          
	│          └─temp
	├─dist
	│  │  rsa.exe
	│  │  w9xpopen.exe
	│  │  
	│  └─keys
	│          d.txt
	│          e.txt
	│          n.txt
	│          p.txt
	│          q.txt
	│          
	├─keys
	│      d.txt
	│      e.txt
	│      n.txt
	│      p.txt
	│      q.txt
	│      
	└─lib
			key.py
			key.pyc
			prime.py
			prime.pyc
			__init__.py
			__init__.pyc

Just in case that U don't have a python compiler on your PC,the whole program was packaged into an independent executable 'rsa.exe' file in the 'dist' folder,which means that U can use the program as the following:

	>cd dist/
	>rsa[.exe] [-h] -p PLAINFILE [-n NFILE] [-e EFILE] [-d DFILE] -c CIPHERFILE
		tes/enc/dec
=======
# rsa-python
rsa cryption writen with python
>>>>>>> 57f87d96ab08220bf4ffe256254319217f22015c
