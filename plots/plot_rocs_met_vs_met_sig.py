import matplotlib.pyplot as plt
import mplhep as hep
import json
import numpy as np

hep.style.use("CMS")

#load json file
# Read in data svjl - multi-lepton category
file_rocs = "/Users/cesarecazzaniga/MET_significance_plots/rocs_DoubleMuon.json"
with open(file_rocs, 'r') as f:
    rocs_data = json.load(f)



colors = {
   'MET_significance' : "#3f90da",
   'MET_T1_pt' : "#ffa90e",
}

top_vs_dy_rocs_bkg_eff_METsig = rocs_data["diboson"]["eff_s"]["MET_significance"]
top_vs_dy_rocs_signal_eff_METsig = rocs_data["diboson"]["eff_b"]["MET_significance"]
top_vs_dy_rocs_bkg_eff_MET = rocs_data["diboson"]["eff_s"]["MET_T1_pt"]
top_vs_dy_rocs_signal_eff_MET = rocs_data["diboson"]["eff_b"]["MET_T1_pt"]


#apply a smoothinng using gaussian filter from scipy
from scipy.ndimage import gaussian_filter1d
top_vs_dy_rocs_bkg_eff_METsig = gaussian_filter1d(top_vs_dy_rocs_bkg_eff_METsig, sigma=1)
top_vs_dy_rocs_signal_eff_METsig = gaussian_filter1d(top_vs_dy_rocs_signal_eff_METsig, sigma=1)
top_vs_dy_rocs_bkg_eff_MET = gaussian_filter1d(top_vs_dy_rocs_bkg_eff_MET, sigma=1)
top_vs_dy_rocs_signal_eff_MET = gaussian_filter1d(top_vs_dy_rocs_signal_eff_MET, sigma=1)


fig, ax = plt.subplots(figsize=(8, 8))

#Setting axis
ax.set_xlim(0.00001, 1.0)
#set y-limits
ax.set_ylim(0, 1)


# Set labels
ax.set_xlabel(r"Background efficiency ($\epsilon_{bkg}$)",fontsize=20)
ax.set_ylabel(r"Signal efficiency ($\epsilon_{sig}$)",fontsize=20)


#plot for svjl multi-lepton category
ax.plot(
    top_vs_dy_rocs_bkg_eff_METsig,
    top_vs_dy_rocs_signal_eff_METsig,
    label="MET significance",
    color=colors['MET_significance'],
    linewidth=3,
    linestyle='-',
)

ax.plot(
    top_vs_dy_rocs_bkg_eff_MET,
    top_vs_dy_rocs_signal_eff_MET,
    label="PF MET",
    color=colors['MET_T1_pt'],
    linewidth=3,
    linestyle='--',
)




#set log scale for y axis
ax.set_xscale('log')


ax.yaxis.set_label_coords(-0.1, 1.0)

# Create legends
leg0 = ax.legend(loc='upper left', fontsize=14, title = "diboson (signal) vs DY+jets (background)", ncols = 1, alignment='left')
leg0.get_title().set_fontsize(16)


#move leg0, leg1, leg2 slightly down 
#leg0.set_bbox_to_anchor((0.95, 0.6))


hep.cms.label("Preliminary", ax=ax, data=False, rlabel="", fontsize=20)



ax.text(
    1.0, 1.0,  # (x, y) in axis coordinates
    r"138 fb$^{-1}$ (13 TeV)",
    ha="right", va="bottom",
    transform=ax.transAxes,
    fontsize=20
)



plt.savefig('Figure_met_sig_performance_single_muon.pdf', bbox_inches='tight')




