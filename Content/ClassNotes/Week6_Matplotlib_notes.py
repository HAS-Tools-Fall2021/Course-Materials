# %%
import matplotlib.pyplot as plt
import matplotlib as mpl 



# Getting help
# https://matplotlib.org
# https://matplotlib.org/gallery/index.html
# %%
# Setting styles
plt.style.use('seaborn')

x = np.linspace(0,10,100)

#opens up an interactive plotting window for you
plt.plot(x, np.sin(x))

# By default in vscode your plot will show up when you say plot
# but if you want it to show up when you run from command line too
# you need to say plt.show after
# you only need to  include  this once at the end of all your plotting
# not after every plot
plt.show() 

# Saving figure to file 
fig = plt.figure()
plt.plot(x, np.sin(x))
fig.savefig('test.png')


# %%
# Easy plotting 
# plot and scatter

#changing color and line type
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed')
ax.plot(x, np.cos(x))

#changing the axes
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed')
ax.plot(x, np.cos(x))
ax.set_xlim(-1,5)
ax.set_ylim(-2,2)  # can also flip  order to plot axes in reverse

# Add a title
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed')
ax.plot(x, np.cos(x))
ax.set_title("my plot")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.set_xlim(-1,5)
ax.set_ylim(-2,2)  # cal also flip  order to plot axes in reverse

# Add a legend
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed', label = 'sinx')
ax.plot(x, np.cos(x), label='cosx')
ax.set_title("my plot")
ax.set_xlabel("y")
ax.set_ylabel("sin(x)")
ax.set_xlim(-1,5)
ax.set_ylim(-2,2)  # cal also flip  order to plot axes in reverse
ax.legend()
plt.show()

# Changing this to points rather than lines
# Others to try; 'O, ., , , x, +, v, ^, <, >, s, d
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), 'p', color= 'red')

# can combine with a line too
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), 'd', color= 'red', linestyle = 'solid')

# and  then you could go all sorts of crazy
# for all the details do help(plt.plot())
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-p', color= 'gray', 
        markersize=5, linewidth=1, 
        markerfacecolor='purple', markeredgecolor='red',
        markeredgewidth= '0.1')


#A better way to make scatter plots
# This is more powerful becauase you  can change the 
# properties of each point individually 
fig, ax = plt.subplots()
ax.scatter(x, np.sin(x), marker='o')

#for example having the color change with the x value
fig, ax = plt.subplots()
ax.scatter(x, np.sin(x), c=x, marker='o')

# or the size change with some random number
fig, ax = plt.subplots()
size=1000 * np.random.rand(len(x))
ax.scatter(x, np.sin(x), c=x, s=size,  marker=',')


# %%
# Note that all of the above can be done by just doing plot. rather than ax.plt
# for example: 
# set the 'gotcha's' on this link for more details: https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
plt.scatter(x, np.sin(x), c=x, s=size,  marker=',')

# %%
# other kids of plots
x=np.linspace(0,10,50)
dy = 0.8
y=np.sin(x) + dy*np.random.randn(50)
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=dy, fmt='.k')

#alternate approach using plt instead
plt.errorbar(x,y, yerr=dy, fmt='.k')

# or plot the error continuously as a line
fig, ax = plt.subplots()
ax.plot(x, y, 'or-')
ax.fill_between(x, y-dy, y+dy, color='grey',  alpha=0.2)

#same thing using plt instead
plt.plot(x,y , 'or-')
plt.fill_between(x, y-dy, y+dy, color='grey',  alpha=0.2)

# histograms
x1=np.random.normal(0,0.8,10000)
x1=np.random.normal(0,0.8,10000)
x2=np.random.normal(-2,1,10000)
x3=np.random.normal(3,2,10000)

myalpha = 0.7
plt.hist(x1, bins=10, alpha=myalpha, histtype='stepfilled',
        color='steelblue', edgecolor='purple')
plt.hist(x2, bins=10, alpha=myalpha, histtype='stepfilled',
        color='green', edgecolor='purple')    
plt.hist(x3, bins=10, alpha=myalpha, histtype='stepfilled',
        color='red', edgecolor='purple')   
plt.show()

# and we could combine the redundant stuff like this
kwargs = dict(bins=5, alpha=0.2, histtype='stepfilled',
         edgecolor='purple')
plt.hist(x1, **kwargs, color='blue')
plt.hist(x2, **kwargs, color='green')
plt.hist(x3, **kwargs, color='red')
plt.show()


# %%
# Figures and axes 
fig, ax = plt.subplots(figsize=(6, 6))
#or you can do this top step in two lines like this:
#fig = plt.figure(figsize=(6,6))
#ax = plt.axes()
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed', label = 'sinx')
ax.plot(x, np.cos(x), label='cosx')
ax.set_title("my plot")
ax.set_xlabel("y")
ax.set_ylabel("sin(x)")
ax.set_xlim(-1,5)
ax.set_ylim(-2,2) 
ax.legend()
plt.show()

# same as ab ove but combining all the axis set commands onto one line
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed', label = 'sinx')
ax.plot(x, np.cos(x), label='cosx')
ax.set(title="my plot", xlabel="y", ylabel="sin(x)",
             xlim=(-1,5), ylim=(-2,2)) 
ax.legend()
plt.show()

# %%
# Creating multi panel plots: 
# creating figue and Axes objects for a figure with 

# Easy example with two subplots 
fig,ax = plt.subplots(2,1)
# then we refer to these  objects when we want to do the plotting
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

#_________
# Examples of how to referencs subplots for a 2 by 2 grid
#1. Using the x,y locations
fig, ax = plt.subplots(2, 2)
ax[0,0].plot(x, np.sin(x))
ax[0,1].plot(x, np.cos(x))
ax[1,0].plot(x, np.sin(x))
ax[1,1].plot(x, np.cos(x))

# Flattening and just using the index number for the plot
fig,ax = plt.subplots(2,2)
ax = ax.flatten() 
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[2].plot(x, np.sin(x))
ax[3].plot(x, np.cos(x))

#Naming the axes when we create them then referring to them by name
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2,2)
ax1.plot(x, np.sin(x))
ax2.plot(x, np.cos(x))
ax3.plot(x, np.sin(x))
ax4.plot(x, np.cos(x))


# Alternate style using plt directly:
# Note this is a state type approach -- You activate a subplot and then
# plot things to it
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
# %%
# 4. Same question as 3 but without using loc
data = np.ones((7, 3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
q4 = data_frame
#q4.iloc[range(0,7,2),1] = 0
q4.iloc[range(1, 6, 2), :] = 0

q4[range(1, 6, 2), (0, 2)] = 0

q4.iloc[range(1, 6, 2), [0, 2]] = 0

