from args import *
from ..base_filters import *
import os.path

from pandacore import setupPandaApp, getScreenshot

def saveScreenshot(p3dapp, filename):
    pilimage = getScreenshot(p3dapp)
    pilimage.save(filename)

def FilterGenerator():
    class SaveScreenshotFilter(SaveFilter):
        def __init__(self):
            super(SaveScreenshotFilter, self).__init__('save_screenshot', 'Saves a screenshot of the rendered collada file')
        def apply(self, mesh, filename):
            if os.path.exists(filename):
                raise FilterException("specified filename already exists")
            p3dApp = setupPandaApp(mesh)
            saveScreenshot(p3dApp, filename)
            return mesh
        
    return SaveScreenshotFilter()