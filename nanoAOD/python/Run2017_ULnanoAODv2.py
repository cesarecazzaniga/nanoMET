import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
    return argParser
    
# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
from nanoMET.tools.user import redirector_global as redirector

# DB
from nanoMET.tools.user import dbDir
dbFile = dbDir+'/DB_Run2017_ULnanoAODv2.sql'
logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2017B_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017B_UL",        "/DoubleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017C_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017C_UL",        "/DoubleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017D_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017D_UL",        "/DoubleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017E_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017E_UL",        "/DoubleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017F_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017F_UL",        "/DoubleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
#DoubleMuon_Run2017G_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2017G_UL",        "/DoubleMuon/Run2017G-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2017B_UL,
    DoubleMuon_Run2017C_UL,
    DoubleMuon_Run2017D_UL,
    DoubleMuon_Run2017E_UL,
    DoubleMuon_Run2017F_UL,
    #DoubleMuon_Run2017G_UL,
]


allSamples = DoubleMuon

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt")
    s.isData    = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )

