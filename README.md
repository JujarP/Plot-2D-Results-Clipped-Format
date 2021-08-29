# Plot-2D-Results-Cipped-Format
Saves images of 2D results from raw time stamped data. E.g. Opens data.dat, reads column 1 (x) position, column 2 (y) position, column 3 (some data like velocity or temperature)


# Description

Python script to plot variables on a 2D grid where the data is read from time stamped files.
* Suppose you have a series of time stamped results files: 12.0000.xplt, 14.0000.xplt, 16.0000.xplt, etc
* The script loops through all those files in the working directory and plots variables onto a 2D grid
* Suppose those files have the structure as follows:

| x coordinate | y coordinate | variable 1, e.g. Temp | Variable 2, e.g. Velocity |
|---|---|---|---|
| Some data | Some data | Some data | Some data |
| ... | ... | ... | ... |
| Last data point | Last data point | Last data point | Last data point |

* This script loops through all time stamped results files and plots a figure of a variable against the x and y coordinates creating a colour map
* The figures are time stamped and are also saved as timestamps in their file names
* E.g. 12.0000.png, 14.0000.png, etc
* Ultimately this allows users to stitch the images together and create animations in a program of their choice.

## Installation

Use a Python environment of your choice. This was created in Anaconda Spyder.

## Usage

The main user inputs are:

* Change the extension of your files that contains your data. E.g. .plt, .dat, .txt, etc

```python
        if filepath.endswith(".yplt"):
```

* Change your variable names. In you don't need headers, but you must tell the script what each data column is.
* This is done by the command 
```python
 data = pd.read_table(filepath,sep="\s+",header = None,
                                 names = ["x","z","ux","uy","uz"])      #Import data from .plt as a pandas table
``` 
* In this example we are saying the first column of the data is "x", second is "z", third is "ux" etc.
* This can be anything. E.g. "x", "y", "Temperature".
* You need to also label your data within the script.

```python
            x = data["x"].values                                        #Assign variable name
            y = data["z"].values                                        #Assign variable name
            xy_ux = data["ux"].values                                   #Assign variable name
            xy_uy = data["uy"].values                                   #Assign variable name
            xy_uz = data["uz"].values                                   #Assign variable name

``` 

* Change the variable you want to plot

```python
            var=xy_uz                                    #Which variable do you want to plot?

```

* There are also some graphing options you can change and these are under the section 

```python
##################################################
################GRAPHING OPTIONS##################
##################################################
```
## Example Files

Included are example results files ending in .yplt so you can see the original use case and data:
* SOL_.0000.yplt
* ...
* SOL_10.0000.yplt

The file names are time stamped (as is commonly the case when writing transient results files). The Python script reads the time stamp and uses it as the output for the saved image files. Example output files are therefore:
* 0.png
* ...
* 15.png

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Support

Feel free to contact me jujar dot panesar at gmail dot com
