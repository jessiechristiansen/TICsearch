# TICsearch
Produce a properly formatted file for upload to the MAST TESS portal

Say you have a list of stars (nearby M dwarfs!) and you want to know the corresponding TESS Input Catalog (TIC) ID, position, TESS_mag, etc for each star. Here is a short python script that uses astroquery.simbad to scrape the list of star names, resolve the positions with SIMBAD, and print a properly formatted file for upload to the MAST TESS portal (https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html). 

First, update the produce_tic_search_file.py script to point to the correct inputFile of star names (example file fulllist.txt is uploaded) and desired outputFile name of the new file. Run the produce_tic_search_file.py file and confirm the output is as expected. Star names that do not resolve in SIMBAD are printed to the output terminal.

Once you have the file, at the MAST TESS portal you can navigate:
  Select a Collection: MAST Catalogs, then 
  Mission: TESS Input (~600 million targets) or TESS CTL (~10 million targets), then
  Upload Target List: and browse to the file created by the python script. 
  
You should get to a screen that looks like the uploaded screenshot. Because of the original file formatting, you can use the nifty MAST tools (like AstroView) to see your targets. There are many columns of information in the TIC, browse through and download the resulting table using the icon with the green arrow. 
