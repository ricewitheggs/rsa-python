import argparse
import lib.key
import codecs

__author__="wcf,wxm,ff & xc"

def modeChoose():
	def printMessage():
		print "Please choose your mode:"
		print "	type \'dec\' for decryption"
		print "	type \'enc\' for encryption"
		print "	type \'tes\' for testing"
	printMessage()
	while True:
		mode=raw_input()
		if mode in ['dec','enc','tes']:
			print "You have chosen mode",mode
			return mode
		else:
			print "Error:you have chosen wrong mode!"
			printMessage()
			continue

def cryption(sourceText,k,n):
	return pow(sourceText,k,n)

def groupPlainText(plainfile,n):
	left=0
	right=len(n)
	while True:
		plainText=plainfile[left:right]
		left+=len(n)
		right=left+len(n)
		if int(plainText,16)>int(n,16):
			plainText=plainText[:-1]
			left-=1
			right-=1
		yield int(plainText,16)
		try:
			k=plainfile[right-1]
			continue
		except IndexError:
			try:
				k=plainfile[left]
				right=None
				continue
			except IndexError:
				break


def groupCipher(cipherfile,n):
	left=0
	right=len(n)
	while True:
		cipherText=cipherfile[left:right]
		left+=len(n)
		right=left+len(n)
		yield cipherText
		try:
			k=cipherfile[right-1]
			continue
		except IndexError:
			try:
				k=cipherfile[left]
				right=None
				continue
			except IndexError:
				break

if __name__=='__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument('-p',action="store",dest="plainfile",required=True)
	parser.add_argument('-n',action="store",dest="nfile" )#""",required=True""")
	parser.add_argument('-e',action="store",dest="efile")
	parser.add_argument('-d',action="store",dest="dfile")
	parser.add_argument('-c',action="store",dest="cipherfile",required=True)
	getArgs=parser.parse_args()
	plainFile=getArgs.plainfile
	nFile=getArgs.nfile
	cipherFile=getArgs.cipherfile
	eFile=getArgs.efile
	dFile=getArgs.dfile
	mode=modeChoose()
	if mode=='enc':
		keys=lib.key.genKey(eFile,dFile,nFile)
		with open('keys/n.txt','r') as nf:
			n=nf.read()
		with codecs.open(plainFile,'r','utf8') as f:
			plainTexts=f.read()
			print plainTexts
			encodedPlainTexts=plainTexts.encode('utf8').encode('hex')
			print encodedPlainTexts
		plainText=groupPlainText(encodedPlainTexts,hex(keys['n'])[2:-1])
		for plain in plainText:
			print 'p',hex(plain)[2:-1]
			cipher=hex(cryption(plain,keys['e'],keys['n']))[2:]
			cipherText=cipher if cipher[-1]!='L' else cipher[:-1]
			print 'n',n
			if len(cipherText)<len(n):
				cipherText='0'*(len(n)-len(cipherText))+cipherText
			with open(cipherFile,'a') as c:
				print 'c',cipherText
				c.write(cipherText)
	if mode=='tes':
		with open(eFile,'r') as eKey:
			e=eKey.read()
		with open(nFile,'r') as nKey:
			n=nKey.read()
		with open(plainFile,'r') as f:
			plainTexts=f.read()
		plainText=groupPlainText(plainTexts,n)
		for plain in plainText:
			cipher=hex(cryption(plain,int(e,16),int(n,16)))[2:]
			cipherText=cipher if cipher[-1]!='L' else cipher[:-1]
			with open(cipherFile,'a') as f:
				f.write(cipherText)
	if mode=='dec':
		with open(dFile,'r') as dKey:
			d=dKey.read()
		with open(nFile,'r') as nKey:
			n=nKey.read()
		with open(cipherFile,'r') as f:
			cipherTexts=f.read()
			print cipherTexts
		cipherText=groupCipher(cipherTexts,n)
		plainTexts=''
		for cipher in cipherText:
			print 'c',cipher
			plain=hex(cryption(int(cipher,16),int(d,16),int(n,16)))[2:]
			plainText=plain if plain[-1]!='L' else plain[:-1]
			print 'p',plainText
			plainTexts+=plainText
		print plainTexts
		plainTexts=plainTexts.decode('hex').decode('utf8')
		with codecs.open(plainFile,'a','utf8') as f:
			f.write(plainTexts)
