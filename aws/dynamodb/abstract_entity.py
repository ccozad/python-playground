from abc import ABC, abstractstaticmethod, abstractmethod
class AbstractEntity:
    #@abstractmethod
    #def key(self):
    #    pass

    #@abstractmethod
    #def body():
    #    pass

    @abstractstaticmethod
    def table_name():
        pass

    @abstractstaticmethod
    def key_schema():
        pass

    @abstractstaticmethod
    def key_attributes():
        pass