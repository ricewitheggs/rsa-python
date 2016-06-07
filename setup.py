from distutils.core import setup
import glob
import py2exe
options={"py2exe":{"compressed":1,"optimize":2,"bundle_files":1}}
setup(console=["rsa.py"],options=options,zipfile=None,data_files=[("keys",glob.glob("keys\\*.txt")),(".",glob.glob("*.txt"))])
