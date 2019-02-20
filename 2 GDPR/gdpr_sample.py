import sys
from G2Engine import G2Engine

moduleName = "pyG2",
iniFilename = "G2Module.ini"
verboseLogging = False
configID = bytearray([])

# Create the G2Engine object with the G2Module.ini once per process
engine = G2Engine()

# Initialize the G2Engine once per process. This will take a few seconds.
initRet = engine.init(moduleName, iniFilename, verboseLogging, configID)

print(configID)

# Evidently the python library doesn't ship with the Windows installer??

# <rest of sample goes here>
