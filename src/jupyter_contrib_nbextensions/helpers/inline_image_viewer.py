# Inline image viewer (use h/l in jupyter mode to navigate, 1/2 to markup, 0 to dump markup to console)

from time import time

from IPython.display import HTML, display


def show_inline_viewer(urls, (width, height)):
    imageViewer = '<div class=inline-image-viewer style="width: {}px; height: {}px;" data-index=0>'.format(width, height)
    imageViewer += '<span class=inline-image-viewer-filename></span>'
    imageViewer += '<span class=inline-image-labels></span>'
    for i, s in enumerate(urls):
        imageViewer += ('<img style="{}" src="{}?rnd={}" />'.format('display: block; ' if i == 0 else '', s, int(time())))
    imageViewer += '</div>'

    display(HTML(imageViewer))
