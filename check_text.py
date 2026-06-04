python : Traceback (most recent call last):
位於 線路:22 字元:1
+ python -c "
+ ~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (Traceback (most recent call last)::String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
  File "C:\Users\FH01\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymupdf\__init__.py", line 3009, in __i
nit__
    doc = mupdf.fz_open_document(filename)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\FH01\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymupdf\mupdf.py", line 50790, in fz_op
en_document
    return _mupdf.fz_open_document(filename)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pymupdf.mupdf.FzErrorFormat: code=7: no objects found

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<string>", line 3, in <module>
  File "C:\Users\FH01\AppData\Local\Programs\Python\Python311\Lib\site-packages\pymupdf\__init__.py", line 3012, in __i
nit__
    raise FileDataError(f'Failed to open file {filename!r}.') from e
pymupdf.FileDataError: Failed to open file 'pdfs/test-original.pdf'.
