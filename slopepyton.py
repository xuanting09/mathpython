print('y-y1=m(x-x1)')
x,y=map(int,input('point1(x,y):').split(','))
x2,y2=map(int,input('point2(x1,y1):').split(','))
xrange=x-x2
yrange=y-y2
slope=yrange/xrange
if yrange<0 and xrange<0:
    yrange=yrange*-1
    xrange=xrange*-1   
print('m=',yrange,'/',xrange,'=',slope)
