""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    4th Ed. by RH Landau, MJ Paez, and CC Bordeianu (D)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2024. 
    Please respect copyright & acknowledge our work."""                                                  

# EasyMatPlot.py:                 Simple use of matplotlib's plot command 

from pylab import *                                   # Load Matplotlib

Xmin = -5.;   Xmax = +5.;  Npoints= 500
DelX = (Xmax - Xmin) / Npoints                                      
x = arange(Xmin, Xmax, DelX)        
y =  sin(x) * sin(x*x)                                # F(x array)
print ('arange => x[0], x[1],x[499]=%8.2f %8.2f %8.2f' %(x[0],x[1],x[499]))
print ('arange => y[0], y[1],y[499]=%8.2f %8.2f %8.2f' %(y[0],y[1],y[499]))
print ("\n Now doing the plotting thing, look for Figure 1 on desktop" )                                                                                       
xlabel('x');      ylabel('f(x)');     title(' f(x) vs x')         
text(-1.75,  0.75, 'MatPlotLib \n Example')            # Text on plot
plot(x, y, '-', lw=2)                                                      
grid(True)                                             # Form grid
show()                                                  