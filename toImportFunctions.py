from toImportLibraries import *

# prints first and last x rows of df 
def printHnT(df, x, asHTML=False):
    boolConcat = False if (len(df) < 2*x) else True
    if asHTML:
        if boolConcat:
            display(HTML(pd.concat([df.head(x), df.tail(x)]).to_html()))
        else:
            display(HTML(df.to_html()))
    else:
        if boolConcat:
            print(pd.concat([df.head(x), df.tail(x)]).to_string())
        else:
            print(df.to_string())

#Use it after "start_time = time.time()"
def printRuntime(start_time):
    print("> Runtime: %s" % (str(dt.timedelta(seconds=time.time() - start_time))))
    
def mkdirIfnotExist(path):
    if not os.path.exists(path): 
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of directory "+path+" failed")
        else:
            print("Successfully created directory: "+path)
    else:
        print("Directory "+path+" exists")
		
def checkSciLibVersions():
	print("pd: "+pd.__version__)
	print("np: "+np.__version__)
	print("sp: "+sp.__version__)
	print("mpl: "+mpl.__version__)
	
