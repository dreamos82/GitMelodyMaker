from abc import ABCMeta, abstractmethod
import abc

class ConverterToNote(abc.ABC):

    notesLabels = [ 'C', 'D', 'E', 'F', 'G', 'A', 'B' ]
    timeSignatures = [ [2,4], [6,8], [4,4] ]
    allowedDurations = [ 1, 2, 4, 8, 16, 32, 64, 128 ]
    
    @abstractmethod
    def getNoteFromCommit(self, commitItem):
        pass

    @abstractmethod
    def getOctave(self, value):
        pass

    @abstractmethod
    def getNoteLabel(self, value):
        pass

    @abstractmethod
    def getAlteration(self, value):
        pass

    @abstractmethod
    def getDuration(self, value):
        pass

    @abstractmethod
    def getChordOrArpeggio(self, input_bar):
        pass

    @abstractmethod
    def getTimeSignature(self, commits):
        pass


