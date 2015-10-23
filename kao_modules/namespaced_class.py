from .kao_module import KaoModule

class NamespacedClass:
    """ Represents a class that is specfied as $module.$class """
    
    def __init__(self, namespaceString):
        """ Initialize the namespaced class with the namespace """
        moduleName, self.classname = namespaceString.rsplit('.', 1)
        self.module = KaoModule(moduleName)
        
    def instantiate(self, *args, **kwargs):
        """ Instantiate this class """
        return self.cls(*args, **kwargs)
        
    @property
    def cls(self):
        """ Return the underlying Python class this wraps """
        return getattr(self.module.module, self.classname)