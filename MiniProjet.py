import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window =  Tk()
window.title("Mini Projet")

window.geometry('450x200')

lbl = Label(window, text="Donner les valeurs de parametres !")
lbl.grid(column=0, row=0)

lbla = Label(window, text="valeur de a :")
lbla.grid(column=0, row=1)


a = Entry(window,width=10)
#user.pack()

a.grid(column=1, row=1)

lblb = Label(window, text="valeur de b :")
lblb.grid(column=0, row=2)

b = Entry(window,width=10)
b.grid(column=1, row=2)

lbln = Label(window, text="valeur de n :")
lbln.grid(column=0, row=3)

n = Entry(window,width=10)
n.grid(column=1, row=3)

###############################**methode trapez#################################
class Trapezoidal(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            plt.plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)#plot de f(x)
        plt.plot(xl, yl,"cs")#point support
        plt.ylabel('f(x)')  

#######################################################################
          
class Simpson(object):
    def __init__(self, a, b, n, f): #initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)#les pts supports
        self.f = f
        self.n = n #nombre de subdivision

    def integrate(self,f):#calculer la somme ((b-a)/6*n)*[f(a)+2*sum(xi)+4*sum(mi)+f(b)]
        x=self.x #les points supports xi #x(0)=a-->x(n)=b
        y=f(x) #yi variable local y(o)=f(xo)-->y(n)
        h = float(x[1] - x[0])#pas h=(b-a)/2*n
        n = len(x) - 1#nombre subdivision
        if n % 2 == 1:#si le reste de la division =1 impaire
            n -= 1#☺nombre de sub ywali paire
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        #y[1:-1:2] min impaire loulla m0 lil 9bal likhrania 5ater 3anna deja y(n) par pas de 2== mi
        #calculer la somme
        #T(-1] dernier valeur dans le tableau)
        return h * s / 3.0
    def Graph(self,f,resolution=1001):#1000 points 1001 résolution juste pour dessiner f
        xl = self.x #pt support
        yl = f(x) #yi
        xlist_fine=np.linspace(self.a, self.b, resolution)
        # pour le graph de la fonction f #intervalle ab subdiviser en 1000 poitns
        for i in range(self.n):#range intervalle 0 à n
            xx=np.linspace(x[i], x[i+1], resolution)
            #pour chaque subdivisuion  on doit dessiner polynome dnc on doit aussi le subdiviser
            m=(xl[i]+xl[i+1])/2#pt milieu
            a=xl[i]#borne gauche
            b=xl[i+1]#borne droite
            l0 = (xx-m)/(a-m)*(xx-b)/(a-b)
            l1 = (xx-a)/(m-a)*(xx-b)/(m-b)
            l2 = (xx-a)/(b-a)*(xx-m)/(b-m)
            P = f(a)*l0 + f(m)*l1 + f(b)*l2#fonction dde polynome
            plt.plot(xx,P,'m')#dessiner polynome d'interpolation
        yflist_fine = f(xlist_fine)#fontion f
        plt.plot(xlist_fine, yflist_fine,'g')
        plt.plot(xl, yl,'wp')#point support en bleu rond
        
        plt.ylabel('f(x)')
        plt.title('Simpson')      
#######################################################################
class Rectangle(object): #class rectange 
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x# contiens les xi
        y=f(x)#les yi 
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        return h * s
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i]  , 0     , 0   ] # ordonnees des sommets
            plt.plot(x_rect, y_rect,"g")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)
        plt.plot(xl, yl,"rd")
  
        plt.ylabel('f(x)')
        plt.title('Rectangle')
#######################################################################
class Milieu(object): #class rectange 
    def __init__(self, a, b, n, f):#initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x# contiens les xi
        h = float(x[1] - x[0])
        s=0
        for i in range(self.n):
            s=s+f((x[i]+x[i+1])*0.5)
        return h*s
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl=f(xl);
        xlist_fine=np.linspace(self.a, self.b, resolution)
        
        for i in range(self.n):
            
            m=(xl[i]+xl[i+1])/2
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , f(m), f(m)  , 0     , 0   ] # ordonnees des sommets
            plt.plot(x_rect, y_rect,"b")
            yflist_fine = f(xlist_fine)
            plt.plot(xlist_fine, yflist_fine)
            plt.plot(m,f(m),"y*")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Milieu') 
#######################################################################

#S = Simpson(a, b, n, f)
#R = Rectangle(a, b, n, f)
#M = Milieu(a,b,n,f)
################################################################################
var1 = tk.IntVar()
chk1 = tk.Checkbutton(window, text='methode de trapez', variable=var1)
chk1.place(relx = 0.1, rely = 0.5)
###############################**methode simpson#####################################

var2 = tk.IntVar()
chk2 = tk.Checkbutton(window, text='methode de simpson', variable=var2)
chk2.place(relx = 0.5, rely = 0.5)

###############################**methode rectangle#####################################
var3 = tk.IntVar()
chk3 = tk.Checkbutton(window, text='methode de rectangle', variable=var3)
chk3.place(relx = 0.1, rely = 0.6)
###############################**methode milieu#####################################

var4 = tk.IntVar()
chk4 = tk.Checkbutton(window, text='methode de milieu', variable=var4)
chk4.place(relx = 0.5, rely = 0.6)
####################################################################

# TSB button function
###############################
def TSBClicked():
    print(a.get())
    A = float(a.get())
    B = float(b.get())
    N = int(n.get())
    B = B*math.pi
    x = np.linspace(A, B, N+1)
    def f(x):
        return math.sin(x)
    f2 = np.vectorize(f)

    T = Trapezoidal(A, B, N, f)
    S = Simpson(A, B, N, f)
    R = Rectangle(A, B, N, f)
    M = Milieu(A,B,N,f)
    
    #from matplotlib.figure import Figurefrom matplotlib.figure 
  #  ************************ connection to oracle ***************************
       
    # **************QUERIES EXECUTION ********************************** 
    # ***************if tablespace checkbox is checked ******************
    if(var1.get()==1):  

        
        T.Graph(f2)
  

        
    # ***************if users checkbox is checked ************************   
    if(var2.get()==1):
        S.Graph(f2)
     
    
    if(var3.get()==1):  

        
        R.Graph(f2)
  

        
    # ***************if users checkbox is checked ************************   
    if(var4.get()==1):
        M.Graph(f2)
    
######################################
TSB = Button(window, text="AFFICHER",bg="orange", fg="red", command=TSBClicked)
TSB.place(relx = 0.5, rely = 0.8, anchor = CENTER, width=80)
#TSB.grid(column=0, row=5)

window.mainloop()




cursor.close()
cursor2.close()
con.close()
