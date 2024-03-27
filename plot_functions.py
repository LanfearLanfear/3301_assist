import numpy as np
import matplotlib.font_manager
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def plot_bigrams(input_array, axis_option=None, fullscreen=None):
    matplotlib.rcParams['font.family'] = "Segoe UI Historic"

    bigram_table = np.zeros((29, 29), dtype=np.int32)
    for index in range(len(input_array) - 1):
        bigram_table[input_array[index], input_array[index + 1]] += 1

    fig, ax = plt.subplots()
    ax.matshow(bigram_table, cmap=plt.cm.jet)

    sx = ax.secondary_xaxis('bottom')
    sy = ax.secondary_yaxis('right')

    ax.set_xticks(np.arange(29))
    ax.set_yticks(np.arange(29))
    sx.set_xticks(np.arange(29))
    sy.set_yticks(np.arange(29))

    ax.set_xticklabels(latin_ticks())
    ax.set_yticklabels(latin_ticks())

    if axis_option == 'runes':
        sx.set_xticklabels(rune_ticks())
        sy.set_yticklabels(rune_ticks())

    for i in range(29):
        for j in range(29):
            c = bigram_table[j, i]
            ax.text(i, j, str(c), va='center', ha='center')

    if fullscreen:
        plot_fullscreen()

    plt.show()


def plot_letter_frequency(input_array, axis_option=None, fullscreen=None):
    matplotlib.rcParams['font.family'] = "Segoe UI Historic"

    _, counts = np.unique(input_array, return_counts=True)
    if len(counts) != 29:
        counts = np.zeros(29)
        for number in range(29):
            counts[number] = np.sum(input_array == number)
    fig, ax = plt.subplots()
    plt.bar(np.arange(29), counts)
    ax.set_xticks(np.arange(29))
    ax.set_xlim(left=-1, right=29)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    if axis_option == 'runes':
        ax.set_xticklabels(rune_ticks())
    if axis_option == 'latin':
        ax.set_xticklabels(latin_ticks())

    if fullscreen:
        plot_fullscreen()

    plt.tight_layout()
    plt.show()


def latin_ticks():
    return ['F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 'T', 'B', 'E',
            'M', 'L', 'ING', 'OE', 'D', 'A', 'AE', 'Y', 'IA', 'EA']


def rune_ticks():
    return ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ',
            'ᛝ', 'ᛟ', 'ᛞ', 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']


def plot_fullscreen():
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
