import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    return argParser
    
# Logging
if __name__=="__main__":
    import nanoMET.tools.logger as logger
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
dbFile = dbDir+"/DB_Run2018_17Sep2018_private.sql"

logger.info("Using db file: %s", dbFile)

'''
Single and double lepton PDs are generated with GTs using 2018 V8 JECs.
'''

# DoubleMuon
DoubleMuon_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018A-17Sep2018-v2_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018B-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018C-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018D_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018D-PromptReco-v2_legacy_nano_v4-67e33113cecc3df848e7adac0079af3d/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2018A_17Sep2018,
    DoubleMuon_Run2018B_17Sep2018,
    DoubleMuon_Run2018C_17Sep2018,
    DoubleMuon_Run2018D_17Sep2018,
]

allSamples = DoubleMuon

for s in allSamples:
    s.json = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt")
    s.isData  = True

from nanoMET.tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
