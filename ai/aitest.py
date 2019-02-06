# Import dependencies
import pandas as pd
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.mlab as mlab


import matplotlib.pyplot as plt


def learnTest():  

    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot([1, 2, 3], 'ro--', markersize=12, markerfacecolor='g')
  
    
    incomes = np.random.normal(100.0, 20.0 ,10000)
    
    n, bins2, patches = ax.hist(incomes, 100)

    canvas = FigureCanvasAgg(fig)
    canvas.print_png( os.getcwd()+ '/static/media/'+'webapp.png', dpi=150)

    

def aiTest1():  

    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot([1, 2, 3], 'ro--', markersize=12, markerfacecolor='g')    
    


    np.random.seed(19680801)

    dt = 0.01
    t = np.arange(0, 10, dt)
    nse = np.random.randn(len(t))
    r = np.exp(-t / 0.05)

    cnse = np.convolve(nse, r) * dt
    cnse = cnse[:len(t)]
    s = 0.1 * np.sin(2 * np.pi * t) + cnse

    
    ax.plot(t, s)
   
    ax.psd(s, 512, 1 / dt)


    canvas = FigureCanvasAgg(fig)
    canvas.print_png( os.getcwd()+ '/static/media/'+'webapp.png', dpi=150)




def aiTest2():
    dt = np.pi / 100.
    fs = 1. / dt
    t = np.arange(0, 8, dt)
    y = 10. * np.sin(2 * np.pi * 4 * t) + 5. * np.sin(2 * np.pi * 4.25 * t)
    y = y + np.random.randn(*t.shape)

    # Plot the raw time series
    fig = Figure(constrained_layout=True)
    gs = gridspec.GridSpec(2, 3, figure=fig)
    ax = fig.add_subplot(gs[0, :])
    ax.plot(t, y)
    ax.set_xlabel('time [s]')
    ax.set_ylabel('signal')

    # Plot the PSD with different amounts of zero padding. This uses the entire
    # time series at once
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.psd(y, NFFT=len(t), pad_to=len(t), Fs=fs)
    ax2.psd(y, NFFT=len(t), pad_to=len(t) * 2, Fs=fs)
    ax2.psd(y, NFFT=len(t), pad_to=len(t) * 4, Fs=fs)
    plt.title('zero padding')

    # Plot the PSD with different block sizes, Zero pad to the length of the
    # original data sequence.
    ax3 = fig.add_subplot(gs[1, 1], sharex=ax2, sharey=ax2)
    ax3.psd(y, NFFT=len(t), pad_to=len(t), Fs=fs)
    ax3.psd(y, NFFT=len(t) // 2, pad_to=len(t), Fs=fs)
    ax3.psd(y, NFFT=len(t) // 4, pad_to=len(t), Fs=fs)
    ax3.set_ylabel('')
    plt.title('block size')

    # Plot the PSD with different amounts of overlap between blocks
    ax4 = fig.add_subplot(gs[1, 2], sharex=ax2, sharey=ax2)
    ax4.psd(y, NFFT=len(t) // 2, pad_to=len(t), noverlap=0, Fs=fs)
    ax4.psd(y, NFFT=len(t) // 2, pad_to=len(t),
            noverlap=int(0.05 * len(t) / 2.), Fs=fs)
    ax4.psd(y, NFFT=len(t) // 2, pad_to=len(t),
            noverlap=int(0.2 * len(t) / 2.), Fs=fs)
    ax4.set_ylabel('')

    canvas = FigureCanvasAgg(fig)
    canvas.print_png( os.getcwd()+ '/static/media/'+'webapp.png', dpi=150)


def aiTest3():
    prng = np.random.RandomState(19680801)  # to ensure reproducibility

    fs = 1000
    t = np.linspace(0, 0.3, 301)
    A = np.array([2, 8]).reshape(-1, 1)
    f = np.array([150, 140]).reshape(-1, 1)
    xn = (A * np.exp(2j * np.pi * f * t)).sum(axis=0) + 5 * prng.randn(*t.shape)

    fig, (ax0, ax1) = plt.subplots(ncols=2, constrained_layout=True)

    yticks = np.arange(-50, 30, 10)
    yrange = (yticks[0], yticks[-1])
    xticks = np.arange(-500, 550, 200)

    ax0.psd(xn, NFFT=301, Fs=fs, window=mlab.window_none, pad_to=1024,
            scale_by_freq=True)
    ax0.set_title('Periodogram')
    ax0.set_yticks(yticks)
    ax0.set_xticks(xticks)
    ax0.grid(True)
    ax0.set_ylim(yrange)

    ax1.psd(xn, NFFT=150, Fs=fs, window=mlab.window_none, pad_to=512, noverlap=75,
            scale_by_freq=True)
    ax1.set_title('Welch')
    ax1.set_xticks(xticks)
    ax1.set_yticks(yticks)
    ax1.set_ylabel('')  # overwrite the y-label added by `psd`
    ax1.grid(True)
    ax1.set_ylim(yrange)


    canvas = FigureCanvasAgg(fig)
    canvas.print_png( os.getcwd()+ '/static/media/'+'webapp.png', dpi=150)
