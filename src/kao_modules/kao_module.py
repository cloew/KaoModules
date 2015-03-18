from kao_decorators import lazy_property

from importlib import import_module

class KaoModule:
    """ Represents a Python module """
    
    def __init__(self, name):
        """ Initialize the module with the name of the module it represents """
        self.name = name
        
    @lazy_property
    def module(self):
        """ Represents the actual module underlying this module """
        return self._import(self.name)
        
    def importModule(self, *names):
        """ Import the names given from this module and return
            If none, then import and return this module """
        modules = [self._import(self.join(name)) for name in names]
        
        if len(modules) == 0:
            return self.module
        elif len(modules) == 1:
            return modules[0]
        else:
            return modules
        
    def _import(self, name):
        """ Import the given name """
        return import_module(name)
        
    def join(self, childName):
        """ REturn the module name of a child with the given name """
        return "{0}.{1}".format(self.name, childName)