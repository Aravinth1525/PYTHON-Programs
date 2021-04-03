import pyqrcode
Msg= 'https://1.bp.blogspot.com/-IO4xROpdoLw/YCF79K5MVKI/AAAAAAAADO8/cPlcKBjm4vwbgz3YcYGqfbS2xTIcfpwoACLcBGAsYHQ/s2048/IMG_2342.jpg'
x=pyqrcode.create(Msg)
x.png('Blog.png',scale=20)