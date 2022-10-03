import tempfile

print (tempfile.gettempdir()) # prints the current temporary directory

f = tempfile.TemporaryFile()
f.write(b'something on temporaryfile')
f.seek(0) # return to beginning of file
print (f.read()) # reads data back from the file
f.close() # temporary file is automatically deleted here