{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "# Measuring Matter Antimatter Asymmetries at the Large Hadron Collider"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "![](http://lhcb-public.web.cern.ch/lhcb-public/en/LHCb-outreach/multimedia/LHCbDetectorpnglight1.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "# Introduction\n",
    "### Press the grey arrow to expand each section\n",
    "____"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "<b> Welcome to the first guided LHCb Open Data Portal project! </b>\n",
    "\n",
    "<div align=\"justify\">Here you will be able to analyse data taken by the Large Hadron Collider (LHC) at CERN. The aim of this study is for you to be able to search for differences in the behaviour of matter and [antimatter](https://en.wikipedia.org/wiki/Antimatter). This project will enable you to carry out your own data analysis at a level similar to that of CERN research. This project does not require a detailed knowledge of particle physics. It is most suitable for people with a scientific and mathematical background equivalent to that required for applying for university entrance in a science, technology engineering or mathematics discipline. Some previous familiarity with computer programming would also be advantageous. Additional theoretical information or programming knowledge you might need is provided as the project progresses.</div>\n",
    "\n",
    "Before you start, you might find it helpful to find out more about matter antimatter asymmetries, what we hope to learn by studying them, and how we can detect them with experiments such as the LHCb experiment at CERN.\n",
    "\n",
    "Here are some details that relate directly to this project:\n",
    " - What is the [particle physics focus](Background-Information-Notebooks/ProjectIntro.ipynb) of this experiment? and what will I study in this project?\n",
    " - How does the LHCb [detector](Background-Information-Notebooks/DetectorSoftwareDataSample.ipynb) record the data?\n",
    "\n",
    "Once you have tried the analysis please provide feedback to help us improve this project using [this brief survey](https://docs.google.com/forms/d/1dEh4A4agmk5zpmR0zrhF79k-lJKV4vX1ETIGJjDscnc/viewform?c=0&w=1).\n",
    "\n",
    "Feel free to post questions, feedback and discuss results with other users using the [GitHub issue tracker](https://github.com/lhcb/opendata-project/issues)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "# Getting Started\n",
    "\n",
    "## Aims:\n",
    "* Become familiar with the help available for programming\n",
    "* Read the simulation data into the program\n",
    "____"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "<div align=\"justify\">Just like researchers at CERN, you will be coding your own analysis. This will use the computer programming language Python. There is no prerequisite of Python language programming experience for following this project. There will be hints available to you helping you along the way. You might find these tutorials on Python helpful:</div>\n",
    "\n",
    "[Python Tutorials](http://www.tutorialspoint.com/python/)\n",
    "\n",
    "The most important coding guidance we are providing you is in the form of an unrelated analysis. We have performed an [analysis of Nobel prizes winners](Example-Analysis.ipynb). That link provides you with the full code for this. The coding skills required for this Nobel analysis is very similar to that needed for the particle physics analysis. Hence by reading and understandign that analysis you can copy and adapt the lines of code to perform your particle physics analysis."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "## Reading simulation data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "In order to get started and check the first code that you will be writing works correctly it is best to start by analysing simulated data rather than real data from the LHC. The real data contains not only the type of events that you wish to analyse, known as the 'signal', but also events that can fake these, known as 'background'. The real data measurements are also limited by the resolution of the detector. The simplified simulation data provided here contains only the signal events and provides the results that would be obtained for a perfect detector.\n",
    "\n",
    "IMPORTANT: For every code box with code already in it, like the one below you must click in and press shift+enter to run the code.\n",
    "\n",
    "If the `In [x]:` to the left of a codebox changes to `In [*]:` that means the code in that box is currently running"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "from __future__ import print_function\n",
    "from __future__ import division\n",
    "\n",
    "%pylab inline\n",
    "execfile('Data/setup_main_analysis.py')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "If you want help with coding there is in addition to the [example code](Example-Analysis.ipynb), some hints within each section and a [function reference list](Background-Information-Notebooks/FunctionReferences.pdf)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# Let us now load the simulated data\n",
    "sim_data = read_root('Data/PhaseSpaceSimulation.root')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "<div align=\"justify\">Now that you can access the data, you can use a number of functions which can help you analyse it. You can find these functions in the libraries at the top of the page. Try to make a table of some of the information within your data file so that you can get a feel of the typical values for data in the set. Understanding the range of values for different variables will help with plotting graphs.</div>\n",
    "\n",
    "The data contains information about 'events' that were observed in the detector. An event refers to the particles produced when an interaction took place when two proton are collided at the LHC. The data you have includes information about particles observed in the detector after each collision. If you think of the data as a table, each row of the table is the results from a different collision. The columns of the table are different quantities measured about the particles produced in the collision. \n",
    "\n",
    "We are interested in analysing the decays of particles called B<sup>+</sup> or B<sup>-</sup> mesons decaying into three other mesons called kaons (K<sup>+</sup> or K<sup>-</sup>). The events you have been given are those in which this process may have occurred. The detector has been used to reconstruct tracks that may have come from the kaons. You are given the measured momenta, charge, and likelihood of the tracks being kaons. You are given information for three tracks in each event, the ones that could be the three kaons that a B<sup>+</sup> or B<sup>-</sup> meson has decayed into. The following information is available about each event: [information list](Background-Information-Notebooks/EventData.ipynb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make a table of the data variables here "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "### Hints"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Creating a table** - Use your `head()` - remember to look at the [example analysis](Example-Analysis.ipynb) to see how this was done there."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Invariant mass reconstruction\n",
    "\n",
    "## Aims:\n",
    "* Plot a histogram of the momentum of one of the kaon candidates\n",
    "* Calculate the energy of each of the kaon candidates\n",
    "* Plot the invariant masses of the B<sup>+</sup> or B<sup>-</sup> mesons___"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Plotting a feature:\n",
    "\n",
    "You can plot any features of the data in a histogram. Choose any suitable binning that allows you to observed the distribution of the variable clearly. Try making a histogram for the first kaon candidate's momentum x-component (H1_PX):\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make a histogram of the H1_PX variable here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Momentum is a **vector** quantity, it has x,y, and z components. Try calculating the **magnitude** of the momentum of the first kaon candidate and plotting a histogram of this, you'll need the `H1_PX`, `H1_PY` and `H1_PZ` variables."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# calculate a variable for the magnitude of the momentum of the first kaon \n",
    "# plot a histogram of this variable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "### Hints"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Histogram plotting** - You can use the hist() function. The parameters bins(n) and range(x,y) allow youto plot n bins over the range x to y.\n",
    "\n",
    "**Vector Magnitude** The square magnitude of a magnitude of a vector is given by the sum of the square of its of its components in the x,y and z directions: $p^2 = p_x^2+p_y^2+p_z^2$, where $p$ is the magnitude of the momentum, and $p_x,p_y,p_z$ are the components of the momentum in the X,Y, and Z directions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Energy and mass\n",
    "\n",
    "Einstein's theory of special relativity relates Energy, mass and momentum. We have measured the momentum of the kaon candidates in the detector, and have just plotted one of the components of the momentum of the kaon, and the magnitude of the momentum. The invariant mass of the kaon is well known and you can look this up. We wish to determine the energy of the kaons.    \n",
    "\n",
    "Here is a brief guide to the energy-momentum relation of [special relativity](Background-Information-Notebooks/SpecialRelativity.ipynb). Further information can be found on wikipedia pages on [Invariant Mass](https://en.wikipedia.org/wiki/Invariant_mass)  and the [Energy-momentum relation](https://en.wikipedia.org/wiki/Energy%E2%80%93momentum_relation).\n",
    "\n",
    "Now, calculate the energy of the first kaon candidate using:\n",
    "\n",
    "<center> $E^2 = p^2 + m^2$ </center>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate the energy of the first kaon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# plot a histogram of this variable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "### Hints"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Energy calculation** - Use the magnitude of momentum variable you calculated above and the known invariant mass of the kaon to work out the energy of the first hadron. Calculate the energy squared, and then the energy and plot this.\n",
    "\n",
    "**Kaon mass** - you can find the kaon mass on wikipedia or in physics textbooks. There is also a reference used by particle physicists: all our knowledge of the properties of the particles are collected together by the particle data group  [here](http://pdg.lbl.gov/2014/reviews/rpp2014-rev-charged-kaon-mass.pdf)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "Calculate the momenta and energies of the second and third kaon candidates also.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate variables for the energy of the other two kaons"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Adding features of the $B$ meson\n",
    "\n",
    "In this analysis we are looking for B<sup>+</sup> or B<sup>-</sup> mesons (see [B meson](https://en.wikipedia.org/wiki/B_meson)) that have decayed into the three charged [kaons](https://en.wikipedia.org/wiki/Kaon).\n",
    "\n",
    "Energy is a conserved quantities. This means that you can use the energy of the three 'daughter' kaons, which you have calculated above, to calculate the energy that the B meson that decayed into them must have.\n",
    "\n",
    "Momentum is also a conserved quantity. Hence you can also use the momenta of the 'daughter' kaons to calculate the momentum of the B meson. But be careful - momentum is a *vector* quantity. \n",
    "\n",
    "Using the Energy of the B meson and the magnitude of the momentum of the B meson you can use the energy-momentum relationship again. This time you are applying it to the B meson. This will allow you to calculate the invariant mass of the B meson.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate the energy of the B meson"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate the momentum components of the B meson \n",
    "# and the magnitude of the momentum of the B meson"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "run_control": {
     "frozen": false,
     "read_only": false
    },
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# calculate the B meson invariant mass\n",
    "# plot the B meson invariant mass in a histogram"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You should have a graph that sharply peaks at the mass of the B<sup>+</sup> meson. The mass of the B<sup>+</sup> and B<sup>-</sup> meson are the same. Check that the peak of your graph is at the [known mass](http://pdg.lbl.gov/2014/listings/rpp2014-list-B-plus-minus.pdf) of the B meson. **Congratulations!**\n",
    "\n",
    "Recall that you have made this plot for simulated data. How might you expect the plots for real data to look different ? In the next section you will start to work with the real LHC data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "### Hint"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**B Meson Energy** - From energy conservation, the energy of the B meson will be the sum of the energies of the three kaons: $E_B=E_{K1}+E_{K2}+E_{K3}$, where $E_B$ is the energy of the B meson, $E_{K1}, E_{K2}, E_{K3}$ are the energies of each of the kaons. \n",
    "\n",
    "**B meson momentum** - From momentum conservation, the X component of the momentum of the B meson will be the sum of the X momentum components of the three Kaons : $px_B=px_{K1}+px_{K2}+px_{K3}$, where $px$ is the X direction component of the momentum of the B meson, $px_{K1},px_{K2},px_{K3}$ are the X direction components of the momenta of the three kaons. You can then do the same with the Y and Z components. Having obtained the X,Y, and z components of the B momentum you can find the magnitude of the momentum of the B meson.\n",
    "\n",
    "** B meson invariant mass*** - Rearrange the equation $E^2=p^2+m^2$ to find $m^2$. Using the values of the magnitude of the momentum of the B meson and the B meson Energy, find the mass of the B meson.\n",
    "\n",
    "**Histogram plotting** - Take care that the range of your mass plot is set suitably that you can see the mass peak. Once you have found the peak you can set the range appropriately. You do not have to start your graph at a mass of 0.\n",
    "\n",
    "**Units** - The data you are provided has energies in 'MeV' (10<sup>6</sup> electron volts). The mass of the B meson is often quoted in 'GeV/c<sup>2</sup>' (10<sup>9</sup> electron volts)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Working with real data and applying cuts\n",
    "## Aims:\n",
    "* Filter out data that is not from the B<sup>+</sup> → K<sup>+</sup>K<sup>+</sup>K<sup>−</sup> channel, or the antiparticle equivalent B<sup>-</sup> → K<sup>+</sup>K<sup>-</sup>K<sup>−</sup>\n",
    "\n",
    "* Plot a histogram of B-meson mass for the real data and observe how different cuts affect the data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the section above you have analysed the simulation data to determine the invariant mass of the B meson. Now, you can start applying the methods you have used to the real LHCb data. This data was collected by the LHCb detector at CERN during 2011, the first major year of LHC operations.\n",
    "\n",
    "The data you are given has been filtered to select only events that are likely to have come from B<sup>+</sup> or B<sup>-</sup> mesons decaying into three final state charged particles. You are interested in the case where these three final state paticles are charged kaons K<sup>+</sup> or K<sup>-</sup>.\n",
    "\n",
    "An introduction has been provided on the [detector and data sample](Background-Information-Notebooks/DetectorSoftwareDataSample.ipynb). As background information we also provide further information on the [selection](Background-Information-Notebooks/DataSelection.ipynb) that has been applied to select this data sample.\n",
    "\n",
    "## Preselection\n",
    "You want to apply a preselection to the three final state tracks that\n",
    "* Ensures that they are not muons (i.e. `!H1_isMuon` where `!` means `not`, and similarly for `H2` and `H3`)\n",
    "* Requires that they each have a low probability of being pions (e.g. `H1_ProbPi < 0.5`)\n",
    "* Requires that they each have a high probability of being a kaon (e.g. `H1_ProbK > 0.5`)\n",
    "\n",
    "You need to find a balance between making cuts that are too loose and include too many background events and too tight and reject many of your signal events.\n",
    "\n",
    "In order to now find the most suitable further selection cuts, make yourself familiar with [how cuts can affect the significance of the final result](Background-Information-Notebooks/CutsInformation.ipynb). Feel free to come back to this stage later and adjust your cuts to see the impact. \n",
    "\n",
    "The pre selection you create will be applied for you if give it the name 'preselection'.\n",
    "\n",
    "We have provided an example preselection in the hints, so feel free to use that to get started if you wish. start with a loose preselection and then refine it after you have studied the plots.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# Make your preselection here, this line applies no preselection\n",
    "preselection = \"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This next line of code just loads the real data into a new DataFrame, this may take a few minutes.\n",
    "It also applies the preselection that you have created if you called it preselection."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "real_data = read_root(['Data/B2HHH_MagnetDown.root', 'Data/B2HHH_MagnetUp.root'], where=preselection)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Make histograms of the probability of a final state particle being a kaon or a pion.\n",
    "These will help guide you on suitable probability values at which to cut.\n",
    "\n",
    "You can also consider more sophisticated options like 2-D plots of kaon and pion probabilities or different values of the cuts for the different final state particles."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# plot the probability that a final state particle is a kaon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# plot the probability that a final state particle is a pion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now calculate the invariant mass of the B meson for the real data and plot a histogram of this. \n",
    "Compare it with the one you drew for the simulation data. \n",
    "\n",
    "Can you explain the differences you observe?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# draw a histogram for the B meson mass in the real data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Experiment with the cuts and see the impact of harsher or more lenient cuts on the invariant mass plot.\n",
    "You should select a set of cuts which makes the signal most prominent with respect to the background.\n",
    "Once you have finalised the selection on particle identification also make cuts on the reconstructed particle mass to select the events in the B meson mass peak, removing the background events which lie at lower and higher invariant masses. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "### Preselection example hint"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "This is an example string, showing the syntax, that you could use as a preselection starting point:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "preselection = \"H1_ProbPi < 0.5 & H2_ProbPi < 0.5 & H3_ProbPi < 0.5 & H1_ProbK > 0.5 & H2_ProbK > 0.5 & H3_ProbK > 0.5 & !H1_isMuon & !H2_isMuon & !H3_isMuon\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "# Searching for global matter anti-matter differences\n",
    "\n",
    "In this section you will start to study matter antimatter differences (CP Violation). Here 'global' means that you are looking for differences across all ranges of energy and momentum (the kinematics) of the kaons into which the charge B mesons have decayed. Later we look at 'local' differences in different regions of the kinematics. \n",
    "\n",
    "## Aims:\n",
    "* Calculate the global CP asymmetry \n",
    "* Work out the statistical uncertainty\n",
    "* Determine if there is evidence for CP violation in this decay"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "source": [
    "In order to quantify the matter antimatter asymmetry in this process we wish to compare the B<sup>+</sup> and the B<sup>-</sup> particles. The B<sup>-</sup> is the anti-particle of the B<sup>+</sup>.\n",
    "\n",
    "How can you distinguish between events that contain B<sup>+</sup> and B<sup>-</sup> particles using `H1_Charge`, `H2_Charge` and `H3_Charge`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make a variable for the charge of the B mesons"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "Now count the numbers of events of each of the two types (N<sup>+</sup> and N<sup>-</sup>). Also calculate the difference between these two numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make variables for the numbers of positive and negative B mesons"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "In order to calculate the Asymmetry, you can make use of the formula:\n",
    "(note you may need to run this box in order to see the image)\n",
    "<img src=\"Images/AsymmetryEq.png\" width=\"200\" />"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate the value of the asymmetry, by using the formula above, and then print it"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "### Hint"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Differentiating between N+ and N-**\n",
    "\n",
    " - Charge is a conserved quantity. The charge of the $B$ meson is equal to the sum of the charges of the particles into which it decays.\n",
    " - You can use ` len(real_data.query('B_Charge == charge'))` to count the number of mesons, where `B_Charge` is the variable you created and `charge` is `1` or `-1`.\n",
    " - You can find an example of this at the end of the example notebook."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "### Estimating the significance of the deviation\n",
    "\n",
    "You will now need to calculate the statistical uncertainty of the asymmetry. You can do so using the formula: <img src=\"Images/AsymmetryErrorEq.png\" width=\"200\" />\n",
    "\n",
    "The significance of the result, sigma, is found by dividing the value for asymmetry by its uncertainty. A value exceeding three sigma is considered \"evidence\" by particle physicists while a value of five sigma or more can be called an \"observation\" or \"discovery\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate the statistical significance of your result and print it"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Congratulations!** You have performed your first search for a matter anti-matter difference.\n",
    "\n",
    "Here you have only considered the statistical uncertainty. Your measurement will also have other sources of uncertainty known as systematic uncertainties which you have not considered at this stage.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "# Dalitz plots and two body resonances\n",
    "## Aims:\n",
    "* Produce Dalitz plots of the simulation and real data sample\n",
    "* Create ordered and binned dalitz plots.\n",
    "* Identify two body resonances in the Dalitz plots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "In this stage we introduce you to an important technique for analysing decays of one particle (your charged B meson) into three bodies (the three kaons). This is known as a Dalitz plot. \n",
    "\n",
    "The decay of the B meson can proceed either directly to the three-body final state or via an intermediate particle. For example, B<sup>+</sup> → K<sup>+</sup>K<sup>+</sup>K<sup>−</sup>, could proceed through the decay  B<sup>+</sup> → K<sup>+</sup>R<sup>0</sup>, where R<sup>0</sup> is a neutral particle resonance which can decay R<sup>0</sup> → K<sup>+</sup>K<sup>-</sup>. Dalitz plots can be used to identify these resonances which are visible as bands on the Dalitz plot.\n",
    "\n",
    "More information about these plots and why these are used in particle physics research can be found in [Dalitz Plot Introduction](Background-Information-Notebooks/DalitzPlots.ipynb).\n",
    "\n",
    "The kinematics of a three-body decay can be fully described using only two variables. The energies and momenta of the three kaons are not independent of each other as they all come from the decay of a B meson and energy and momentum are conserved. The axes of the plots conventionally are the squared invariant masses of two pairs of the decay products. It is a 2D plot, the x and y axes are both squared masses and the density of points in the plot shows the structure.\n",
    "\n",
    "Consider our decay B<sup>+</sup> → K<sup>+</sup><sub>1</sub>K<sup>+</sup><sub>2</sub>K<sup>−</sup><sub>3</sub>, where we have numbered the kaons 1,2,3 to distinguish them. We can calculate the invariant mass of three possible combinations that could correspond to intermediate resonances R<sup>++</sup><sub>1</sub> → K<sup>+</sup><sub>1</sub>K<sup>+</sup><sub>2</sub>, R<sup>0</sup><sub>2</sub> → K<sup>+</sup><sub>1</sub>K<sup>-</sup><sub>3</sub>, and R<sup>0</sup><sub>3</sub> → K<sup>+</sup><sub>3</sub>K<sup>-</sup><sub>3</sub>. \n",
    "\n",
    "The potential R<sup>++</sup><sub>1</sub> would be a doubly charged resonance. We would not expect to see any resonances corresponding to this as mesons are composed of one quark and one anti-quark and their charges cannot add up to two units.\n",
    "\n",
    "The potential R<sup>0</sup><sub>2</sub> and R<sup>0</sup><sub>3</sub> correspond to configurations in which we could see resonances. Hence you should compute the invariant mass combinations for these. The square of these masses should be used as the Dalitz variables. \n",
    "\n",
    "We suggest you make these plots first for the simulation data. In the simulation there are no intermediate resonances and your plot should be of uniform density inside the range physically allowed by energy and momentum conservation.\n",
    "\t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate the invariant masses for each possible hadron pair combination"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# plot the invariant mass for one of these combinations "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make a Dalitz plot with labelled axes for the simulation data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "### Hints"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Calculating invariant mass** - Use the same technique as you did above for the B meson, but now applying it to two-body invariant masses rather than three.\n",
    "\n",
    "**Plotting the Dalitz plot** - You can use a `scatter` plot from `matplotlib` to plot a Dalitz plotm, see the [example analysis](Example-Analysis.ipynb). Remember to use the square of each two-body mass."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "## Adding Dalitz plot for real data\n",
    "Now draw a Dalitz plot for the real data. Check that the signs of the charge of the hadrons are correct to correspond to your potential neutral resonances R<sup>0</sup><sub>2</sub> and R<sup>0</sup><sub>3</sub>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# calculate the invariant masses for each possible hadron pair combination in the real data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# make a Dalitz plot for the real data (with your preselection cuts applied)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "<div align=\"justify\">While drawing the Dalitz plot for the real data, label the axes accordingly. Compare the Dalitz plots of the real data with the one for the simulation. \n",
    "What are the most striking differences? \n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "### Ordering Dalitz variables\n",
    "You can make a further improvement to allow you to observe the resonances easier. Your resonances R<sup>0</sup><sub>2</sub> and R<sup>0</sup><sub>3</sub> are both composed of the same particle types, K<sup>+</sup>K<sup>-</sup>, and hence have the same distributions. It is useful to impose an ordering which distinguishes the resonances. We can call the resonances R<sup>0</sup><sub>Low</sub> and R<sup>0</sup><sub>High</sub>. In each event R<sup>0</sup><sub>Low</sub> is the resonance with the lower mass and the other corresponds to the higher mass combination of kaons. You can now use the mass of these ordered resonances as your Dalitz plot variables, thus effectively \"folding\" your Dalitz plot so that one axis always has a higher value than the other.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make a new Dalitz plot with a mass ordering of the axes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "### Hint"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Ordered Dalitz plot** - You can find the maximum of the mass of R<sup>0</sup><sub>Low</sub> vs R<sup>0</sup><sub>High</sub> elementwise on one axis, and the minimum of on the other. You can use `numpy.min(a,b)` and `numpy.max(a,b)` to perform elementwise comparisons between two arrays `a` and `b` and return one array filled by either the individual min/max element from the elementwise comparisons."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "### Binned Dalitz plot\n",
    "You can improve the representation of your Dalitz plot by binning the data. The hist2d function can be used to make a 2D histogram. The number of bins specification in the hist2d function is the number of bins in one axis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# plot a binned Dalitz Plot\n",
    "# use colorbar() to make a legend for your plot at the side"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "## Two body resonances"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "You can now use your Dalitz plot to identify the intermediate resonances that you see in your plots. The resonances will have shown up as bands of higher density of points on the plots. You can use the [particle data group](http://pdg.lbl.gov/2015/tables/contents_tables.html) tables of mesons to identify which particles these correspond to. The tables give the masses and widths of the particles and their decay modes. You are looking for mesons with the masses corresponding to where you see the bands and that decay into K<sup>+</sup>K<sup>-</sup>.\n",
    "\n",
    "**Congratulations!** You have succesfully made a Dalitz plot and used it to observe the presence of intermediate particles in the decay of your charged B meson into three charged kaons. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "# Searching for local matter anti-matter differences\n",
    "## Aims:\n",
    "* Observe matter antimatter differences (CP violation) in regions of the Dalitz plots of the B<sup>+</sup> and B<sup>-</sup> mesons.\n",
    "* For the data in these regions produce plots to best display the CP violation."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "In a section above you searched for global CP violation. You probably did not find a result with very high significance. \n",
    "\n",
    "CP violation may arise from interference between decays through different resonances, and hence the magnitude and sign of the CP violation may vary across the Dalitz plot. We can apply the same equation as in the global CP violation study \n",
    "<img src=\"Images/AsymmetryEq.png\" width=\"200\" />\n",
    "but apply this only to events in particular regions of the Dalitz plot.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "## Removing charm resonances"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "The analysis performed here is to study the CP violation in the charmless B meson decays to kaons. \"charmless\" means that the decay does not proceed through a charm quark. However, the most frequent decay of the B mesons occur through the *b* quark decaying into a *c* quark. The majority of these events can be removed by rejecting the events that are proceeding through a D<sup>0</sup> meson (which contains the charm quark).\n",
    "\n",
    "In the section above you plotted a histogram of the invariant mass of the intermediate resonances and will have observed the D<sup>0</sup> meson in this and in the Dalitz plot. You should now reject events that are around the mass range of the D<sup>0</sup> meson to suppress this contribution. You can do this in your pre-selection on the data that you set-up earlier in the project.\n",
    "\n",
    "This was also a simplification that we did not consider when we were calculating the global asymmetry. After you have applied this pre-selection your code will now recompute the global asymmetry with the D<sup>0</sup> meson contribution rejected. We have not yet observed CP violation in charm mesons and searching for this is another active area of current research."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "## Comparing Dalitz plots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "Make separate Dalitz plots for the B<sup>+</sup> and the B<sup>-</sup> decays.\n",
    "Local CP Violation will show up as an asymmetry between the B<sup>+</sup> and the B<sup>-</sup> plots.  \n",
    "\n",
    "In order that the statistical error on the asymmetry in each bin is not over large the bins need to contain a reasonable number of entries. Hence you will probably need larger bins than when you were looking for resonances in the section above. A suitable initial bin size might be $2.5~\\text{GeV}^2/\\text{c}^4 \\times 2.5~\\text{GeV}^2/\\text{c}^4$.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make a Dalitz plot for the B+ events"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "hidden": true,
    "run_control": {
     "frozen": false,
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "# make a Dalitz plot for the B- events"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# Make a plot showing the asymmetry between these two Daltz plots\n",
    "# i.e. calculate the asymmetry between each bin of the B+ and B- Dalitz plots and show the result in another 2D plot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "Observing a large asymmetry in some regions of the plot does not necessarily mean you have observed CP violation. If there are very few events in that region of the plot the uncertainty on that large asymmetry may be large. Hence, the value may still be compatible with zero.\n",
    "\n",
    "You can calculate the statistical uncertainty on the asymmetry, for each bin of the plot, using the same formulas as you used in the global asymmetry section. You can then make a plot showing the uncertainty on the asymmetry.\n",
    "\n",
    "Dividing the plot showing the asymmetry by the plot showing the statistical uncertainty you can then obtain the significance of the asymmetry in each bin. You can then plot the significance of the asymmetry to see if there is any evidence for CP violation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# Make a plot showing the uncertainty on the asymmetry "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# Make a plot showing the statistical significance of the asymmetry"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true,
    "hidden": true
   },
   "source": [
    "## Observing CP violation\n",
    "\n",
    "From your studies of the asymmetry plot, and the plot of its significance, you will be able to identify regions in the Dalitz plots that show indications of sizeable and significant CP Violation. You may find you have several consecutive bins with significant positive, or negative, asymmetries. You may wish to try alternative binnings of the Dalitz plots to best isolate the regions in which the significant asymmetries occur.\n",
    "\n",
    "You can select events that are in these regions of the Dalitz plots where you observe signs of CP Violation. You can then plot a simple 1D histogram of the invariant mass distribution of the B<sup>+</sup> and the B<sup>-</sup> events, just as you did at the start of the project, but only for events that lie in the region of the Dalitz plot that you are interested in. Make the plots of the B<sup>+</sup> and the B<sup>-</sup> events with the same scale, or superimpose the two plots, so that you can observe if the particle and anti-particle decay processes are occurring at the same rate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# Make a plot showing the invariant mass of the B+ meson particles\n",
    "# using events from a region of the Dalitz plot showing sizeable CP asymmetries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "hidden": true
   },
   "outputs": [],
   "source": [
    "# Make a plot showing the invariant mass of the B- meson particles using events from the same region"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "**Congratulations!** You should now have succesfully observed significant evidence for CP Violation. You should have plots that clearly show that particle and anti-particle decay processes occur at different rates in local regions of the Dalitz plot. You may wish to comapre your results with those published by the LHCb collaboration in this [paper](http://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/LHCb-PAPER-2013-027.html).\n",
    "\n",
    "**Well Done** you have succesfully completed your first particle physics analysis project. There are many more analyses that can be conducted witht the data set that you have been provided and the skills that you have gained. Ideas for some of these are explored in the section below. Maybe you can discover something new!\n",
    "\n",
    "Now you've finished the analysis please provide feedback to help us improve this project using [this brief survey](https://docs.google.com/forms/d/1dEh4A4agmk5zpmR0zrhF79k-lJKV4vX1ETIGJjDscnc/viewform?c=0&w=1)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "heading_collapsed": true
   },
   "source": [
    "# Further analyses"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "The data set you have been provided is the full set of data recorded by LHCb preselected for decays of charged B mesons into three final state tracks. This data set has been used for two important publications, [here](http://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/LHCb-PAPER-2013-027.html) and [here](http://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/LHCb-PAPER-2013-051.html).\n",
    "\n",
    "We discuss here: \n",
    "<ul>\n",
    "<li>Additional elements that you could add to your analysis of B<sup>+</sup> → K<sup>+</sup>K<sup>+</sup>K<sup>−</sup> </li>\n",
    "<li>Further analyses that you could perform with this data set</li>\n",
    "</ul>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "## Adding extra sophistication\n",
    "\n",
    "### Systematic Uncertainties\n",
    "In this analysis you considered the statistical uncertainty on the result. This occurs as a result of having only a limited number of events. In addition there are [systematic uncertainties](https://en.wikipedia.org/wiki/Observational_error#Systematic_versus_random_error), these arise from biases in your measurement. Here we discuss three sources of these for this analysis.\n",
    "<ul>\n",
    "<li> Production asymmetry. The LHC is a proton-proton collider and hence the initial state of the collision is not matter antimatter symmetric. Consequently B<sup>+</sup> and B<sup>-</sup> mesons may not be produced at exactly the same rates. This small production asymmetry it is estimated could be approximately 1%. It can also be measured from the data, as discussed in the LHCb paper.</li>\n",
    "<li> Detection asymmetry. The LHCb detector could be more efficient for detecting either the B<sup>+</sup> or the B<sup>-</sup> final states. This is because the positive and negative kaons will be bent by the magnet indifferent directions in the detector. If the efficiency of the detector is higher in one region than another this will lead to higher efficiencies for K<sup>+</sup> or K<sup>-</sup> and hence for B<sup>+</sup> or B<sup>-</sup>. For this reason the magnetic field of the LHCb detector is regularly reversed. You used data in this analysis in which the magnetic field was both up and down and hence the effect will (partially) cancel. By comparing results for the two magnet polarities separately you can check the size of this effect. When loading the data above both polarities were combined, you can instead load them independently to measure the difference between the two datasets.</li>\n",
    "<li> Analysis technique. The analysis technique you have used may bias the result. A major simplification we made in the analysis above was to neglect 'background' events. We imposed a selection to select a sample of predominantly signal events but have not accounted for the effect of the residual background events.</li>\n",
    "</ul>\n",
    "\n",
    "### Using mass sidebands\n",
    "\n",
    "One source of 'background' events arises from random combinations of tracks in events that happen to fake the 'signal' characteristics. These events will not peak in the mass distribution at the mass of the B meson but rtaher will have a smoothly varying distribution. Looking at the number and distribution of of events away from the mass peak can allow you to estimate the number of background events under the mass peak.\n",
    "\n",
    "### Fitting distributions\n",
    "\n",
    "The next level of sophistication in the analysis requires fitting the distributions of events that are observed in the B mass distribution in order to estimate the yield of signal events and background events. You can see how this is done in the LHCb paper on the analysis. Fitting can be performed using the [CERN root framework](https://root.cern.ch/)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "hidden": true
   },
   "source": [
    "## Further analyses\n",
    "\n",
    "The LHCb papers using this data set that you are using analysed four decay channels of the charged B mesons. You can perform any of these analyses.\n",
    "<ul>\n",
    "<li>B<sup>+</sup> → K<sup>+</sup>K<sup>+</sup>K<sup>−</sup> (and anti-particle equivalent). This is the analysis you have performed here. It has the lowest background of the four channels and hence the approximation we made of neglecting the background events will give the least bias to this channel.</li>\n",
    "<li>B<sup>+</sup> → &pi;<sup>+</sup>&pi;<sup>+</sup>&pi;<sup>−</sup> (and anti-particle equivalent). In this analysis the final state is three charged pions. The level of background events compared to the signal is significantly higher as pions are the most commonly produced particle at the LHC. Hence, a method of estimating the background level should be added to complete this analysis.</li>\n",
    "<li>B<sup>+</sup> → K<sup>+</sup>&pi;<sup>+</sup>&pi;<sup>−</sup> (and anti-particle equivalent). In this analysis the final state is a mixture of one kaon and two pions. This means that the analysis needs to determine in each event which track is the best candidate kaon and apply selection cuts appropriately to select out the events.</li>\n",
    "<li>B<sup>+</sup> → &pi;<sup>+</sup>K<sup>+</sup>K<sup>−</sup> (and anti-particle equivalent). This channel has a higher level of background compared to the signal.</li>\n",
    "</ul>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  },
  "toc": {
   "toc_cell": false,
   "toc_number_sections": true,
   "toc_threshold": 6,
   "toc_window_display": false
  },
  "widgets": {
   "state": {},
   "version": "1.1.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
