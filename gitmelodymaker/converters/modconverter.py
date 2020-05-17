import mingus.core.notes as notes
from converters.convertertonote import ConverterToNote
from mingus.containers import Note

class ModConverter(ConverterToNote):
    
    def getNoteFromCommit(self, commitItem):
        noteLabel = self.getNoteLabel(commitItem['lines'])
        noteDuration = self.getDuration(commitItem['deletions'])
        noteOctave = self.getOctave(commitItem['insertions'])
        finalNote = self.getAlteration(noteLabel, commitItem['files'])
        print(": " + str(finalNote) + str(noteOctave) + " T: " + str(noteDuration))
        note = Note(finalNote, noteOctave)
        return [note, noteDuration]

    def getOctave(self, value):
        return value%8

    def getNoteLabel(self, value):
        return self.notesLabels[value % 7]

    def getDuration(self, value):
        return (value%4)+1

    def getAlteration(self, noteLabel, value):
        result = value%3
        if(result == 0):
            return noteLabel
        elif (result == 1):
            return noteLabel + "b"
        else:
            return noteLabel + "#"
