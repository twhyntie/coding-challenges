#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

#...for the MATH.
import numpy as np

#...for the plotting.
import pylab as plt

#...for the colours.
from matplotlib import colorbar, colors

#...for setting the axes ticks.
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def addRadiusCircle(figax, x, y, r):
    """ Draws a circle representing the cluster radius. """

    # Adjust the centre coordinates to account foe the pixel size.
    x_c = x + 0.5; y_c = y + 0.5

    # Set the size of the "cross-hairs".
    rl = 1.5

    # Add the "cross-hairs" to the plot.
    figax.plot([x_c-rl,x_c+rl], [y_c-rl,y_c+rl], 'k-', lw=1)
    figax.plot([x_c-rl,x_c+rl], [y_c+rl,y_c-rl], 'k-', lw=1)

    # Add the circle representing the cluster radius to the plot.
    figax.add_patch(plt.Circle((x_c,y_c),r,fill=False,lw=3.0))
    figax.add_patch(plt.Circle((x_c,y_c),r,fc='k',alpha=0.1,lw=3.0))
    figax.add_patch(plt.Circle((x_c,y_c),r,fill=False,lw=1.0,ec='g'))

def addLineOfBestFit(figax, m, c):
    """ Adds a line of best fit to the cluster image. """

    ## The x values.
    xs = np.arange(0.0,256.0,0.1)

    ## The y values.
    ys = m*(xs - 0.5) + c + 0.5

    figax.plot(xs, ys, 'k-', lw=3)
    figax.plot(xs, ys, 'g-', lw=1)


def make_kluster_image(kl):
    """ Create the kluster image. """

    # FIXME: Make configurable.

    pixels = kl.get_pixel_dict()

    x_min = kl.getXMin()

    x_max = kl.getXMax()

    y_min = kl.getYMin()

    y_max = kl.getYMax()

    w = kl.getWidth()

    h = kl.getHeight()

    C_max = kl.getMaxCountValue()

    x_bar = kl.getXUW()

    y_bar = kl.getYUW()

    radius = kl.getRadiusUW()

    m, c, sumR = kl.getLineOfBestFitValues()

    # Create the figure.
    plt.close('all')

    ## The figure size.
    figsize = 5.0

    ## The figure for the cluster image.
    blobfig = plt.figure(1, figsize=(figsize*1.27, figsize), dpi=150, facecolor='w', edgecolor='w')

    # Set the beyond-frame background colour.
    blobfigax = blobfig.add_subplot(111, axisbg='#222222')

    # Add the frame background (blue).
    blobfigax.add_patch(plt.Rectangle((0,0),256,256,facecolor='#82bcff'))

    # Add a grid.
    plt.grid(1)

    # Select the "hot" colour map for the pixel counts.

    cmap = plt.cm.hot

    colax, _ = colorbar.make_axes(plt.gca())

    col_max = 10*(np.floor(C_max/10.)+1)

    colorbar.ColorbarBase(colax,cmap=cmap,norm=colors.Normalize(vmin=0,vmax=col_max))

    # Add the line of best fit.
    addLineOfBestFit(blobfigax, m, c)

    # Add the radius circle.
    addRadiusCircle(blobfigax, x_bar, y_bar, radius)

    # Loop over the pixels and plot them.
    for X, C in pixels.iteritems():
        x = X % 256; y = X / 256
        scaled_C = float(C)/float(col_max)
        blobfigax.add_patch(plt.Rectangle((x,y),1,1,facecolor=cmap(scaled_C)))

    # Set the axis limits based on the cluster radius.
    b = 3 # border

    xlim_min = x_bar - (np.floor(radius)+b)
    xlim_max = x_bar + (np.floor(radius)+b)
    ylim_min = y_bar - (np.floor(radius)+b)
    ylim_max = y_bar + (np.floor(radius)+b)

    blobfigax.set_xlim([xlim_min, xlim_max])
    blobfigax.set_ylim([ylim_min, ylim_max])

    # Set the axis tick mark spacing.
    blobfigax.xaxis.set_major_locator(MultipleLocator(10))
    blobfigax.yaxis.set_major_locator(MultipleLocator(10))


def make_frame_image(pixel_dict):
    """ Create a figure displaying the frame data. """

    ## The minimum x value.
    x_min = 0

    ## The maximum x value.
    x_max = 256

    ## The minimum y value.
    y_min = 0

    ## The maximum y value.
    y_max = 256

    ## The width of the frame.
    w = 256

    ## The height of the frame.
    h = 256

    ## The maximum count value.
    C_max = 1

    # We add this just in case there are no pixels supplied.
    #if len(Cs) > 0:
    if len(pixel_dict) > 0:
        C_max = max(pixel_dict.values())

    # Create the figure.
    plt.close('all')

    ## The default size of the figure [inches].
    fig_size = 5.0

    ## The figure for the frame.
    fig = plt.figure(1, figsize=(fig_size*1.27, fig_size), dpi=150, facecolor='w', edgecolor='w')

    ## The frame axes.
    figax = fig.add_subplot(111, axisbg='#222222')

    # Add the frame background (blue).
    figax.add_patch(plt.Rectangle((0,0),256,256,facecolor='#82bcff'))

    # Add a grid.
    plt.grid(1)

    # Select the "hot" colour map for the pixel counts and add a
    # colour bar to indicate the count value for each pixel.
    #
    cmap = plt.cm.hot
    #
    colax, _ = colorbar.make_axes(plt.gca())
    #
    col_max = 10*(np.floor(C_max/10.)+1)
    #
    colorbar.ColorbarBase(colax,cmap=cmap,norm=colors.Normalize(vmin=0,vmax=col_max))

    # Loop over the pixels and add them to the figure.
    #for i, x in enumerate(xs):
    for X, C in pixel_dict.iteritems():
        x = X%256; y = X/256
        ## The scaled count value (for the colour map).
        scaled_C = float(C)/float(col_max)

        # Rather than use, say, a 2D histogram for the pixels, we add
        # a coloured square to the plot for each pixel.
        figax.add_patch(plt.Rectangle((x,y),1,1,edgecolor=cmap(scaled_C),facecolor=cmap(scaled_C)))

    ## The frame border width [pixels].
    b = 3

    # Set the axis limits based on the cluster radius.
    figax.set_xlim([0 - b, 256 + b])
    figax.set_ylim([0 - b, 256 + b])

    #return fig
