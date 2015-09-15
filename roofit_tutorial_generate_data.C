/* RooFit tutorial- Dataset generation code
* 
* This is the code I used to make the dataset for the tutorial. 
* The parameters in here should be very similar to the results of your solution
* 
* You can see in here that the exact same PDF specification can _generate_ 
* data as well as fit to it. The generation code is a single line at the end of this macro. 
*
* This tutorial written by Conor Fitzpatrick
* conor.fitzpatrick@cern.ch
* with thanks to Wouter Verkerke and David Kirkby 
* If you spot any bugs or have any problems working through this, let me know... 
*
*/

#include "RooGlobalFunc.h"
#include "RooTreeDataStore.h"
#include "RooRandom.h"
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "RooProdPdf.h"
#include "RooPolynomial.h"
#include "RooExponential.h"
#include "RooAddPdf.h"
#include "TFile.h"
#include "TTree.h"

using namespace RooFit;
void roofit_tutorial_generate_data(){

RooRandom::randomGenerator()->SetSeed(9876); // Use the same random seed so data is always identical

TFile* outputFile = new TFile("dataset.root","RECREATE","dataset.root");
//Define the observables and ranges over which the PDFs will be made:
RooRealVar* obs_mass = new RooRealVar("mass","mass",5300,5400,"MeV/c^{2}");
RooRealVar* obs_time = new RooRealVar("time","time",0.0,12.0,"ps");

/*
 *Make the signal PDFs: 
 */

//First the mass. This is a single gaussian suspiciously like the B_s mass:
RooRealVar* signal_mass_mean = new RooRealVar("signal_mass_mean","signal_mass_mean",5366.3,"MeV/c^{2}");
RooRealVar* signal_mass_sigma = new RooRealVar("signal_mass_sigma","signal_mass_sigma",5.0,"MeV/c^{2}");
RooAbsPdf* signal_mass = new RooGaussian("signal_mass","signal_mass",*obs_mass,*signal_mass_mean,*signal_mass_sigma);

//Now the lifetime. There are built-in PDFs for B-decays in RooFit, but this shows the usefulness of RooFormulaVars:
RooRealVar* signal_lifetime = new RooRealVar("signal_lifetime","signal_lifetime",1.472,"ps");
RooFormulaVar* signal_exponent = new RooFormulaVar("signal_exponent","signal_exponent","-1.0/signal_lifetime",RooArgList(*signal_lifetime));
RooAbsPdf* signal_time = new RooExponential("signal_time","signal_time",*obs_time,*signal_exponent);


//Now we combine the 2 PDFs to make a 2D RooProductPDF in the 2 observables:
RooAbsPdf* signal = new RooProdPdf("signal","signal",*signal_mass,*signal_time);


/*
 *Make the background:
 */ 

//First the mass. This will be a polynomial with a very shallow gradient: 
RooRealVar* bkg_mass_p0 = new RooRealVar("bkg_mass_p0","bkg_mass_p0",5500);
RooRealVar* bkg_mass_p1 = new RooRealVar("bkg_mass_p1","bkg_mass_p1",-1.0);
RooAbsPdf* bkg_mass = new RooPolynomial("bkg_mass","bkg_mass",*obs_mass,RooArgList(*bkg_mass_p0,*bkg_mass_p1));

//Now the time. We'll assume these are prompt short-lived resonances of some sort with an average lifetime much lower than that of our "B_{s}-like" candidates
RooRealVar* bkg_lifetime = new RooRealVar("bkg_lifetime","bkg_lifetime",0.15,"ps");
RooFormulaVar* bkg_exponent = new RooFormulaVar("bkg_exponent","bkg_exponent","-1.0/bkg_lifetime",RooArgList(*bkg_lifetime));
RooAbsPdf* bkg_time = new RooExponential("bkg_time","bkg_time",*obs_time,*bkg_exponent);

//Again we combine the background PDFs to make a 2D Product PDF:
RooAbsPdf* bkg = new RooProdPdf("bkg","bkg",*bkg_mass,*bkg_time);

/*
 * The full Model of signal + background:
 */ 

//This is the sum of the signal and background PDFs, where we use the extended log likelihood to define and extract the relative yields:
RooRealVar* Nsig = new RooRealVar("Nsig","Nsig",1000);
RooRealVar* Nbkg = new RooRealVar("Nbkg","Nbkg",3000);
RooAbsPdf* model = new RooAddPdf("model","model",RooArgList(*signal,*bkg),RooArgList(*Nsig,*Nbkg));

//Now we generate the tutorial dataset from the above PDFs
RooDataSet::setDefaultStorageType(RooAbsData::Tree); 
RooDataSet* data = model->generate(RooArgSet(*obs_mass,*obs_time),-1,true);

cout << "Done generating" << endl;
//And write them out to ntuple
((RooTreeDataStore*)data->store()->tree())->Write();
outputFile->Write();
outputFile->Close();

}
