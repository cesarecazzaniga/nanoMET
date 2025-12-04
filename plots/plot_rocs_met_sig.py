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
   'top' : "#3f90da",
   'diboson' : "#f15a24",
   'triboson' : "#ffa90e",
}

top_vs_dy_rocs_bkg_eff_METsig = rocs_data["Top"]["eff_s"]["MET_significance"]
top_vs_dy_rocs_signal_eff_METsig = rocs_data["Top"]["eff_b"]["MET_significance"]

diboson_vs_dy_rocs_bkg_eff_METsig = rocs_data["diboson"]["eff_s"]["MET_significance"]
diboson_vs_dy_rocs_signal_eff_METsig = rocs_data["diboson"]["eff_b"]["MET_significance"]

trobon_vs_dy_rocs_bkg_eff_METsig = rocs_data["rare"]["eff_s"]["MET_significance"]
trobon_vs_dy_rocs_signal_eff_METsig = rocs_data["rare"]["eff_b"]["MET_significance"]

#check if top_vs_dy_rocs_bkg_eff_METsig has 0 values, if so remove them and the corresponding signal efficiency values
top_vs_dy_rocs_bkg_eff_METsig = np.array(top_vs_dy_rocs_bkg_eff_METsig)
top_vs_dy_rocs_signal_eff_METsig = np.array(top_vs_dy_rocs_signal_eff_METsig)
mask = top_vs_dy_rocs_bkg_eff_METsig > 0
top_vs_dy_rocs_bkg_eff_METsig = top_vs_dy_rocs_bkg_eff_METsig[mask]
top_vs_dy_rocs_signal_eff_METsig = top_vs_dy_rocs_signal_eff_METsig[mask]

#do the same for diboson
diboson_vs_dy_rocs_bkg_eff_METsig = np.array(diboson_vs_dy_rocs_bkg_eff_METsig)
diboson_vs_dy_rocs_signal_eff_METsig = np.array(diboson_vs_dy_rocs_signal_eff_METsig)
mask = diboson_vs_dy_rocs_bkg_eff_METsig > 0
diboson_vs_dy_rocs_bkg_eff_METsig = diboson_vs_dy_rocs_bkg_eff_METsig[mask]
diboson_vs_dy_rocs_signal_eff_METsig = diboson_vs_dy_rocs_signal_eff_METsig[mask]


#do the same for rare
trobon_vs_dy_rocs_bkg_eff_METsig = np.array(trobon_vs_dy_rocs_bkg_eff_METsig)
trobon_vs_dy_rocs_signal_eff_METsig = np.array(trobon_vs_dy_rocs_signal_eff_METsig)
mask = trobon_vs_dy_rocs_bkg_eff_METsig > 0
trobon_vs_dy_rocs_bkg_eff_METsig = trobon_vs_dy_rocs_bkg_eff_METsig[mask]
trobon_vs_dy_rocs_signal_eff_METsig = trobon_vs_dy_rocs_signal_eff_METsig[mask] 


#here maybe put some smoothing?



fig, ax = plt.subplots(figsize=(8, 8))

#Setting axis
ax.set_xlim(0.001, 1.0)
#set y-limits
ax.set_ylim(0, 1)


# Set labels
ax.set_xlabel(r"Background efficiency ($\epsilon_{bkg}$)",fontsize=20)
ax.set_ylabel(r"Signal efficiency ($\epsilon_{sig}$)",fontsize=20)


#plot for svjl multi-lepton category
ax.plot(
    top_vs_dy_rocs_bkg_eff_METsig,
    top_vs_dy_rocs_signal_eff_METsig,
    label="Top",
    color=colors['top'],
    linewidth=3,
    linestyle='-',
)


ax.plot(    diboson_vs_dy_rocs_bkg_eff_METsig,
    diboson_vs_dy_rocs_signal_eff_METsig,
    label="Diboson",
    color=colors['diboson'],
    linewidth=3,
    linestyle='-.',
)

ax.plot(    trobon_vs_dy_rocs_bkg_eff_METsig,
    trobon_vs_dy_rocs_signal_eff_METsig,
    label="Rare (triboson)",
    color=colors['triboson'],
    linewidth=3,
    linestyle=':',
)


#set log scale for y axis
ax.set_xscale('log')


ax.yaxis.set_label_coords(-0.1, 1.0)

# Create legends
leg0 = ax.legend(loc='upper left', fontsize=14, title = "", ncols = 1, alignment='left')
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



plt.savefig('Figure_met_sig_performance_double_muon.pdf', bbox_inches='tight')




