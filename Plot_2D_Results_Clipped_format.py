# -*- coding: utf-8 -*-
"""
Created on Jul 27 2021

@author: Jujar Panesar

Code reads in time stamped data results. E.g. 12.0000.plt, 14.0000.plt, etc
Results have format x, y, variable_1, variable_2, variable_3, etc, 
where x and y are grid positions

The code plots a time stamped color map of a variable
mapped onto the 2D grid positions

E.g. Plot variable_1 on grid positions x and y at time 14.0000

N.b. The data file does not need to have headers, but you need to know the 
data structure. E.g. column 1 is x, column 2 is y, column 3 x velocity etc.

"""
import matplotlib.pyplot as plt                                         #Matplotlib toolkit
import numpy as np                                                      #Numpy toolkit
import pandas as pd                                                     #Pandas toolkit
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from mpl_toolkits.axes_grid1.colorbar import colorbar
import collections as cl                                                #Use specialized container datatypes
import re                                                               #Import regular expression operations
import os                                                               #import operating system interfaces

###################################################
################SEARCH WD FOR FILES################
###################################################

curDir = os.getcwd()                                                    #Stores current work dir as a string

for subdir, dirs, files in os.walk(curDir):                             #Loop through subdirectories
    for file in files:                                                  #Loop through the files
        filepath = subdir + os.sep + file                               #Convert filepaths to string
        if filepath.endswith(".yplt"):                                   #Isolate .plt results files only

####################################################
############ISOLATE TIME VALUE FROM FILE############
####################################################

            time=re.findall('\d*\.?\d+',filepath)                       #store integers and incl period for item in list
            time=[float(i) for i in time]                               #float the time
            time=int(time[0])                                           #Isolate item 0 in time list

################################################
################READ IN THE DATA################
################################################

            data = pd.read_table(filepath,sep="\s+",header = None,
                                 names = ["x","z","ux","uy","uz"])      #Import data from .plt as a pandas table

            x = data["x"].values                                        #Assign variable name
            y = data["z"].values                                        #Assign variable name
            xy_ux = data["ux"].values                                   #Assign variable name
            xy_uy = data["uy"].values                                   #Assign variable name
            xy_uz = data["uz"].values                                   #Assign variable name

################################################
################REORDER THE DATA################
################################################

            extentx=cl.Counter(np.array(x))                             #Makes x a numpy array so we can identify the grid size
            gridsizex = extentx[0]                                      #Identifies the grid size in x
            extenty=cl.Counter(np.array(y))                             #Makes y a numpy array so we can identify the grid size
            gridsizey = extenty[0]                                      #Identifies the grid size in y
            
            xy_ux = xy_ux.reshape(gridsizex,gridsizey,order='F')        #reshape the variables using fortran ordering
            xy_uy = xy_uy.reshape(gridsizex,gridsizey,order='F')        #reshape the variables using fortran ordering
            xy_uz = xy_uz.reshape(gridsizex,gridsizey,order='F')        #reshape the variables using fortran ordering

##################################################
############WHAT DO YOU WANT TO PLOT?#############
##################################################

            var=xy_uz                                                   #Which variable do you want to plot?

##################################################
################GRAPHING OPTIONS##################
##################################################
            
            gridx=list(extentx)                                         #List of grid points in x (regular or irregular spaced)
            gridy=list(extenty)                                         #List of grid points in y (regular or irregular spaced)
            newX,newY=np.meshgrid(gridx,gridy)                          #Create the meshgrid

            fig, ax1 = plt.subplots(1,1, figsize=(10,10), sharey=True)  #Create a graph space
            fig.subplots_adjust(wspace=0.2)                             #Whitespace around graph
   
            vartit = ax1.set_title('$U_x$', fontsize=16)                #graph title title
            vartit.set_position([0.5,1.05])
            ax1.set_ylabel('Number of nodes. Domain size in $z$ is $2\pi$ units.')      #x axis title
            ax1.set_xlabel('Number of nodes. Domain size in $x$ is $4\pi$ units.')      #y axis title
            plt.yticks(np.arange(0, 32 ,2))
            plt.xticks(np.arange(0, 64 ,4))
           
            time=int(time)                                              #Convert time to an integer
            ttl=fig.suptitle('time = ' '%1.4f' ' units' % time, 
                             fontsize=16)                               #text for time ticker
            ttl.set_position([0.5, 0.25])                               #Position the title         
            ax1.tick_params(direction='out', which='both', top=True,
                            right=True)                                 #Tick parameters
            ax1.minorticks_on()                                         #Minor ticks on graph
            ax1.set_aspect('equal')                                     #Set aspect ratio
            divider = make_axes_locatable(ax1)                          #Needed to make colorbar manageable
            cax = divider.append_axes("right", size="5%", pad=0.3)      #Colorbar size and padding
            pos_neg_clipped = ax1.imshow(var, cmap='RdBu', vmin=-0.1, vmax=0.1,
                             interpolation='spline16')                  #Color properties          
            cbar = fig.colorbar(pos_neg_clipped, ax=ax1,
                                cax=cax, extend='both')                 #Colorbar properties                       
            plt.savefig('%s.png' % (str(time)))                         #Save the figure
            plt.show()                                                  #Show the figure