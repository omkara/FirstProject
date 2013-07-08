# This module give the information about  list,dict,tuples method etc 

def info(object,spacing=10,collapse=1):
    """ Print methods and doc string.
    Takes module,class,list,dictionary,or string."""
    methodlist=[method for method in dir(object) if callable(getattr(object,method))]

    
    function=collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n\n".join(["%s %s " %(method.ljust(spacing),function(str(getattr(object,method).__doc__))) for method in methodlist])


