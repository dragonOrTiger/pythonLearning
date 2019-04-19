#!/usr/bin/python3
"""
write(text, /) method of _io.TextIOWrapper instance
Write string to stream.
Returns the number of characters written (which is always equal to the length of the string).
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
flush() method of _io.TextIOWrapper instance
Flush write buffers, if applicable.
This is not implemented for read-only and non-blocking streams.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
close() method of _io.TextIOWrapper instance
Flush and close the IO object.
This method has no effect if the file is already closed.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
read(size=-1, /) method of _io.TextIOWrapper instance
Read at most n characters from stream.
Read from underlying buffer until we have n characters or we hit EOF.
If n is negative or omitted, read until EOF.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
seek(cookie, whence=0, /) method of _io.TextIOWrapper instance
Change stream position.
Change the stream position to the given byte offset. The offset is interpreted relative to the position indicated by whence.
Values for whence are:
* 0 -- start of stream (the default); offset should be zero or positive
* 1 -- current stream position; offset may be negative
* 2 -- end of stream; offset is usually negative
Return the new absolute position.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
fileno() method of _io.TextIOWrapper instance
Returns underlying file descriptor if one exists.
OSError is raised if the IO object does not use a file descriptor.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
readline(size=-1, /) method of _io.TextIOWrapper instance
Read until newline or EOF.
Returns an empty string if EOF is hit immediately.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
readlines(hint=-1, /) method of _io.TextIOWrapper instance
Return a list of lines from the stream.
hint can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
tell() method of _io.TextIOWrapper instance
Return current stream position.
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
truncate(pos=None, /) method of _io.TextIOWrapper instance
Truncate file to size bytes.
File pointer is left unchanged.  Size defaults to the current IO position as reported by tell().  Returns the new size.
"""
fx = open("fileOperation.txt", "x")
fx.write("Hello Runoob!!")
fx.flush()
fx.close()
fx = open("fileOperation.txt", "r+")
fx.write("菜鸟!!")
fx.flush()
fx.seek(0)
print(fx.read())
fx.close()
fx = open("fileOperation.txt", "r+")
print(fx.read())
fx.write("菜鸟!!")
fx.flush()
fx.seek(0)
print(fx.read())
fx.close()
fx = open("fileOperation.txt", "w+")
fx.write("Google!!")
fx.flush()
fx.seek(0)
print(fx.read())
fx.close()
fx = open("fileOperation.txt", "w+")
print(fx.read())
fx.write("Google!!")
fx.flush()
fx.seek(0)
print(fx.read())
fx.close()
fx = open("fileOperation.txt", "a+")
fx.seek(0)
print(fx.read())
fx.write("Tmall!!")
fx.flush()
fx.seek(0)
print(fx.read())
fx.close()
fx = open("fileOperation.txt", "a+")
fx.write("Tmall!!")
fx.flush()
fx.seek(0)
print(fx.read())
fx.close()
fx = open("fileOperation.txt", "r+")
fx.truncate(6)
print(fx.read())
fx.close()
