#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                               import sqrt, cos, sin, pi
from RootTools.core.standard            import *
from nanoMET.tools.user                 import plot_directory
from nanoMET.samples.color              import color
from nanoMET.tools.puReweighting        import getReweightingFunction
from Samples.Tools.metFilters           import getFilterCut
#from nanoMET.tools.cutInterpreter  import cutInterpreter

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',            action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--noData',              action='store_true', default=False,           help='also plot data?')
argParser.add_argument('--small',               action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--plot_directory',      action='store',      default='analysisPlots_test')
argParser.add_argument('--year',                action='store',      default=2016)
argParser.add_argument('--selection',           action='store',      default='relIso0.12-looseLeptonVeto-mll20-onZ')
args = argParser.parse_args()


year = int(args.year)
#
# Logger
#
import StopsDilepton.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.noData:                       args.plot_directory += "_noData"
#
# Make samples, will be searched for in the postProcessing directory
#
postProcessing_directory = "2016_v5/dimuon/"
from nanoMET.samples.nanoTuples_Summer16_postProcessed import *
postProcessing_directory = "2016_v4/dimuon/"
from nanoMET.samples.nanoTuples_Run2016_17Jul2018_postProcessed import *

#
# Text on the plots
#
def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    if "mt2ll100" in args.selection and args.noData: lines += [(0.55, 0.5, 'M_{T2}(ll) > 100 GeV')] # Manually put the mt2ll > 100 GeV label
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots, mode, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      if not args.noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data"
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)"

      plotting.draw(plot,
	    plot_directory = plot_directory_,
	    ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = {},
	    legend = (0.50,0.88-0.04*sum(map(len, plot.histos)),0.9,0.88) if not args.noData else (0.50,0.9-0.047*sum(map(len, plot.histos)),0.85,0.9),
	    drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ),
        copyIndexPHP = True,
      )

#
# Read variables and sequences
#
read_variables = ["weight/F", "MET_pt/F", "MET_phi/F", "MET_sumPt/F", "fixedGridRhoFastjetAll/F", "Muon[pt/F,eta/F,phi/F]", "Jet[pt/F,eta/F,phi/F,cleanmask/I,cleanmaskPhoton/I]", "nJet/I"]

sequence = []

from nanoMET.core.JetResolution import *
from nanoMET.core.Event         import Event
JERData = JetResolution('Summer16_25nsV1_DATA')
JERMC   = JetResolution('Summer16_25nsV1_MC')
#JERData = JetResolution('Spring16_25nsV6_DATA')
#JERMC   = JetResolution('Spring16_25nsV6_MC')
paramsData  = [1.38, 1.27, 1.22, 1.16, 1.10, 0.0, 0.58]
paramsMC    = [1.39, 1.26, 1.21, 1.23, 1.28, -0.26, 0.62]
#paramsData  = [1.26, 1.14, 1.13, 1.13, 1.06, -3.3, 0.59]
#paramsMC    = [1.29, 1.19, 1.07, 1.13, 1.12, -0.04, 0.65]

def calcMETSig( event, sample ):
    if sample.isData:
        JER = JERData
        params = paramsData
    else:
        JER = JERMC
        params = paramsMC
    ev = Event(event, JER, isData=sample.isData)
    ev.calcMETSig(params)
    event.MET_significance_rec = ev.MET_sig

sequence += [ calcMETSig ]

def getLeptonSelection( mode ):
  if   mode=="mumu": return "Sum$(Muon_pt>25&&Muon_isGoodMuon)==2 && Sum$(Electron_pt>10&&abs(Electron_eta)<2.5&&Electron_cutBased>0&&abs(Electron_pfRelIso03_all)<0.4)==0"

nTrueInt36fb_puRW        = getReweightingFunction(data="PU_2016_36000_XSecCentral", mc="Summer16")

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumu']

for index, mode in enumerate(allModes):
  yields[mode] = {}
  if   mode=="mumu":
    data_sample = DoubleMuon_Run2016
    data_sample.texName = "data (2 #mu)"
    data_selectionString = '&&'.join([getFilterCut(isData=True, year=year).replace('&&weight>0',''), getLeptonSelection(mode), "( %s )"%" || ".join(['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL', 'HLT_IsoMu24', 'HLT_IsoTkMu24'])])
    # maybe add singleMu backup
    print data_selectionString
    data_sample.setSelectionString([data_selectionString])
  if   mode=="mumu": data_sample.texName = "data (2 #mu)"

  data_sample.name           = "data"
  data_sample.read_variables = ["event/I","run/I"]
  data_sample.style          = styles.errorStyle(ROOT.kBlack)
  lumi_scale                 = data_sample.lumi/1000

  if args.noData: lumi_scale = 35.9
  weight_ = lambda event, sample: event.weight

  mc = [DY_LO_16, Top_16, VVTo2L2Nu_16]

  for sample in mc: sample.style = styles.fillStyle(sample.color)

  for sample in mc:
    sample.scale          = lumi_scale
    sample.read_variables = ['puWeight/F','Pileup_nTrueInt/F']
    sample.weight         = lambda event, sample: event.puWeight*nTrueInt36fb_puRW(event.Pileup_nTrueInt)
    sample.setSelectionString([getFilterCut(isData=False, year=year), getLeptonSelection(mode)])

  if not args.noData:
    stack = Stack(mc, data_sample)
  else:
    stack = Stack(mc)

  if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 3 )

  # Use some defaults
  Plot.setDefaults(stack = stack, weight = staticmethod(weight_), selectionString = "Sum$(Jet_pt>30&&Jet_jetId&&abs(Jet_eta)<2.4)>=0 && abs(dl_mass-91.2)<10", addOverFlowBin='upper')
  
  plots = []

  plots.append(Plot(
    name = 'yield', texX = 'yield', texY = 'Number of Events',
    attribute = lambda event, sample: 0.5 + index,
    binning=[1, 0, 1],
  ))

  plots.append(Plot(
    name = 'nVtxs', texX = 'vertex multiplicity', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "PV_npvsGood/I" ),
    binning=[50,0,50],
  ))

  plots.append(Plot(
      texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
      attribute = TreeVariable.fromString( "MET_pt/F" ),
      binning=[400/20,0,400],
  ))

  plots.append(Plot(
      texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
      attribute = TreeVariable.fromString( "MET_phi/F" ),
      binning=[10,-pi,pi],
  ))

  # removed from nanoAOD
  #plots.append(Plot(
  #  texX = 'E_{T}^{miss} Significance', texY = 'Number of Events',
  #  attribute = TreeVariable.fromString('MET_significance/F'),
  #  binning= [50,0,100],
  #))

  plots.append(Plot(
    texX = 'E_{T}^{miss} Significance rec.', texY = 'Number of Events',
    name = "MET_significance_rec",
    attribute = lambda event, sample: event.MET_significance_rec,
    binning= [50,0,100],
  ))

  plots.append(Plot(
    texX = '#Sigma p_{T} (GeV)', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "MET_sumPt/F" ),
    binning=[50, 0,2500],
  ))

  plots.append(Plot(
    texX = '#Sigma E_{T} (GeV)', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "MET_sumEt/F" ),
    binning=[50, 0,2500],
  ))

  plots.append(Plot(
    texX = 'm(ll) of leading dilepton (GeV)', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "dl_mass/F" ),
    binning=[40,81.2,101.2],
  ))

  plots.append(Plot(
    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events / 15 GeV',
    name = 'l1_pt',
    attribute = lambda event, sample: event.Muon_pt[0],
    binning=[20,0,300],
  ))

  plots.append(Plot(
    texX = '#phi(l_{1}) (GeV)', texY = 'Number of Events / 15 GeV',
    name = 'l1_phi',
    attribute = lambda event, sample: event.Muon_phi[0],
    binning=[16,-3.2,3.2],
  ))


  plots.append(Plot(
    texX = '#eta(l_{1}) (GeV)', texY = 'Number of Events / 15 GeV',
    name = 'l1_eta',
    attribute = lambda event, sample: event.Muon_eta[0],
    binning=[15,-3.0,3.0],
  ))

  plots.append(Plot(
    texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events / 15 GeV',
    name = 'l1_pt',
    attribute = lambda event, sample: event.Muon_pt[0],
    binning=[20,0,300],
  ))

  plots.append(Plot(
    texX = '#phi(l_{2}) (GeV)', texY = 'Number of Events / 15 GeV',
    name = 'l2_phi',
    attribute = lambda event, sample: event.Muon_phi[1],
    binning=[16,-3.2,3.2],
  ))

  plots.append(Plot(
    texX = '#eta(l_{2}) (GeV)', texY = 'Number of Events / 15 GeV',
    name = 'l2_eta',
    attribute = lambda event, sample: event.Muon_eta[1],
    binning=[15,-3.0,3.0],
  ))

  plots.append(Plot(
    texX = 'p_{T}(l_{2}) (GeV)', texY = 'Number of Events / 15 GeV',
    name = 'l2_pt',
    attribute = lambda event, sample: event.Muon_pt[1],
    binning=[20,0,300],
  ))
  plotting.fill(plots, read_variables = read_variables, sequence = sequence)

  # Get normalization yields from yield histogram
  for plot in plots:
    if plot.name == "yield":
      for i, l in enumerate(plot.histos):
        for j, h in enumerate(l):
          yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
          h.GetXaxis().SetBinLabel(1, "#mu#mu")
          #h.GetXaxis().SetBinLabel(2, "e#mu")
          #h.GetXaxis().SetBinLabel(3, "ee")
  if args.noData: yields[mode]["data"] = 0

  yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
  dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

  drawPlots(plots, mode, dataMCScale)
  allPlots[mode] = plots

# Add the different channels into SF and all
if len(allModes) == 3: #just added for slimmedPlots since we only use doubleMu channel
    for mode in ["SF","all"]:
      yields[mode] = {}
      for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in (['ee','mumu'] if mode=="SF" else ['ee','mumu','mue']))
        except: yields[mode][y] = 0
      dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
    
      for plot in allPlots['mumu']:
        for plot2 in (p for p in (allPlots['ee'] if mode=="SF" else allPlots["mue"]) if p.name == plot.name):  #For SF add EE, second round add EMu for all
          for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
    	    for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
    	        if i==k:
    	            j.Add(l)
    
    drawPlots(allPlots['mumu'], mode, dataMCScale)

logger.info( "Done." )
