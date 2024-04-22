"""
Tuning of MetSig
"""

# Standard imports
import ROOT
ROOT.gROOT.SetBatch(True)
import os
import sys
import math
import copy
import itertools
import json
import random

from RootTools.core.standard      import *

from nanoMET.core.JetResolution   import JetResolution
from nanoMET.tools.cutInterpreter import cutInterpreter
from nanoMET.tools.metFilters     import getFilterCut

from run import run

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',                      action='store',      default='INFO', nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
argParser.add_argument('--pTdependent',                   action='store_true', help='run pT dependent METSig tuning', )
argParser.add_argument('--maxSig',                        action='store',      type=int, default=25 )
argParser.add_argument('--jetThreshold',                  action='store',      type=int, default=15 )
argParser.add_argument('--ttbarModifier',                 action='store',      type=int, default=1 )
argParser.add_argument('--selection',                     action='store',      type=str, default="diMuon-looseLeptonVeto-onZ" )
argParser.add_argument('--year',                          action='store',      type=int, default=2016, choices=[2016,2017,2018] )
argParser.add_argument('--addon',                         action='store',      type=str, default=None, help='additional label in output file')
argParser.add_argument('--runData',                       action='store_true', help='run data tuning' )
argParser.add_argument('--prevfp',                       action='store_true', help='run on prevfp samples' )

args = argParser.parse_args()

# Logger
import nanoMET.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

# define setting
preVFP_string = ""
if args.prevfp:
    preVFP_string = "_preVFP"

if args.year == 2016:
    postProcessing_directory = "2016_UL%s_%s/dimuon/"%(preVFP_string, args.addon)
    trigger                  = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL", "HLT_IsoMu24", "HLT_IsoTkMu24"]
    METPtVar                 = "MET_pt"
    METPhiVar                = "MET_phi"
    JetCollection            = "Jet_pt"
    vetoEtaRegion            = (10.,10.)


    if args.prevfp:
        if args.runData:
            #from nanoMET.samples.nanoTuples_Run2016_ULnanoAODv2_postProcessed import *
            from nanoMET.samples.nanoTuples_Run2016_ULnanoAODv9_preVFP_postProcessed_mumu import *
            samples              = [DoubleMuon_Run2016_preVFP]
            jer                  = "Summer20UL16APV_JRV3_DATA"
        else:
            #from nanoMET.samples.nanoTuples_UL16_nanoAODv2_postProcessed import *
            #from nanoMET.samples.nanoTuples_Run2016_17Jul2018_postProcessed  import *
            from nanoMET.samples.nanoTuples_UL16_nanoAODv9_preVFP_postProcessed_mumu  import *
            samples              = [DY_LO_16, Top_16, diboson_16, rare_16]
            jer                  = "Summer20UL16APV_JRV3_MC"

    else:
        if args.runData:
            from nanoMET.samples.nanoTuples_Run2016_ULnanoAODv9_postProcessed_mumu import *
            samples              = [DoubleMuon_Run2016]
            jer                  = "Summer20UL16_JRV3_DATA"
        else:
            from nanoMET.samples.nanoTuples_UL16_nanoAODv9_postProcessed_mumu import *
            samples              = [DY_LO_16, Top_16, diboson_16, rare_16]
            jer                  = "Summer20UL16_JRV3_MC"


elif args.year == 2017:


    trigger                  = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8", "HLT_IsoMu27"]
    METPtVar                 = "MET_pt"                          #"METFixEE2017_pt"
    METPhiVar                = "MET_phi"                         #"METFixEE2017_phi"
    JetCollection            =  "Jet_pt_nom"                     #"Jet_pt_nom"
    vetoEtaRegion            = (2.65,3.14)

    if str(args.addon) == "v2":
        postProcessing_directory = "2017_UL_v2/dimuon/"
        if args.runData:
            from nanoMET.samples.nanoTuples_Run2017_ULnanoAODv2_postProcessed_mumu import *
    #        samples              = [DoubleMuon_Run2017BCDE]
            samples              = [DoubleMuon_Run2017]
            jer                  = "Summer19UL18_JRV2_DATA"
        else:
            from nanoMET.samples.nanoTuples_UL17_nanoAODv2_postProcessed_mumu import *
            samples              = [DY_LO_17, Top_17, diboson_17, rare_17]
            jer                  = "Summer19UL18_JRV2_MC"

    if str(args.addon) == "v9":
        postProcessing_directory = "2017_UL_v9/dimuon/"
        if args.runData:
            from nanoMET.samples.nanoTuples_Run2017_ULnanoAODv9_postProcessed_mumu import *
            samples              = [DoubleMuon_Run2017]
            jer                  = "Summer19UL18_JRV2_DATA"
        else:
            from nanoMET.samples.nanoTuples_UL17_nanoAODv9_postProcessed_mumu import *
            samples              = [DY_LO_17, Top_17, diboson_17, rare_17]
            jer                  = "Summer19UL18_JRV2_MC"


elif args.year == 2018:

    trigger                  = ["HLT_IsoMu24"]
    METPtVar                 = "MET_pt"
    METPhiVar                = "MET_phi"
    JetCollection            = "Jet_pt"
    vetoEtaRegion            = (10.,10.)

    if str(args.addon) == "v2": 

        postProcessing_directory = "2018_UL_v2/singlemu/"

        if args.runData:
            from nanoMET.samples.nanoTuples_Run2018_ULnanoAODv2_postProcessed_mumu import *
            samples              = [DoubleMuon_Run2018]
            jer                  = "Summer19UL18_JRV2_DATA"
        else:
            from nanoMET.samples.nanoTuples_UL18_nanoAODv2_postProcessed_mumu import *
            samples              = [DY_LO_18, Top_18, rare_18]  #diboson_18
            jer                  = "Summer19UL18_JRV2_MC"

    if str(args.addon) == "v9": 

        postProcessing_directory = "2018_UL_v9/singlemu/"

        if args.runData:
            from nanoMET.samples.nanoTuples_Run2018_ULnanoAODv9_postProcessed_mu import *
            samples              = [Run2018]
            jer                  = "Summer19UL18_JRV2_DATA"
        else:
            from nanoMET.samples.nanoTuples_UL18_nanoAODv9_postProcessed_mu import *
            samples              = [DY_LO_18, Top_18, diboson_18, rare_18, QCD_18, WJets_18]
            jer                  = "Summer19UL18_JRV2_MC"

# calculate setting
preselection    = cutInterpreter.cutString(args.selection)
triggerSel      = "(%s)"%"||".join(trigger)
eventfilter     = getFilterCut( args.year, isData=args.runData )
sel             = "&&".join([preselection, triggerSel, eventfilter])
JR              = JetResolution(jer)
version         = postProcessing_directory.split("/")[0]
outfile         = "results/singleMUALLComplete_UL_tune_%s_%i_%s_%s_sumPt%i_max%i"%("DATA" if args.runData else "MC", args.year, jer, args.selection, args.jetThreshold, args.maxSig)
if args.addon:
    outfile    += "_"+str(args.addon)
if args.pTdependent:
    outfile    += "_pTdep"
outfile        += "_"+version
if args.prevfp:
    outfile    += "_prevfp"

# run
r = run(samples, sel, JR, outfile=outfile, maxN=3e5, METPtVar=METPtVar, METPhiVar=METPhiVar, JetCollection=JetCollection, vetoEtaRegion=vetoEtaRegion, jetThreshold=args.jetThreshold, puWeight="puWeight", ttbarModifier=args.ttbarModifier, pTdepMetSig=args.pTdependent)
LL = r.getLL(r.defaultStart)
r.minimize(start=r.defaultStart, maxSig=args.maxSig)
