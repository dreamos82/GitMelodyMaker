import mingus.core.notes as notes
from converters.convertertonote import ConverterToNote
from mingus.containers import Note
from mingus.containers import Bar
from mingus.containers import NoteContainer
import mingus.core.chords as chords
import random

class ModConverter(ConverterToNote):

    timeSignature = None
    
    def getTimeSignature(self, commits):
        result = (commits[0].stats.total['lines']+commits[len(commits)-1].stats.total['lines'])%3
        self.timeSignature = self.timeSignatures[result]
        print(self.timeSignature)
        return self.timeSignature
    
    def getNoteFromCommit(self, commitItem):
        noteLabel = self.getNoteLabel(commitItem['lines'])
        noteDuration = self.getDuration(commitItem['deletions'])
        noteOctave = self.getOctave(commitItem['insertions'])
        finalNote = self.getAlteration(noteLabel, commitItem['files'])
        print("N: " + str(finalNote) + str(noteOctave) + " T: " + str(noteDuration))
        note = Note(finalNote, noteOctave)
        return [note, noteDuration]

    def getOctave(self, value):
        return value%8

    def getNoteLabel(self, value):
        return self.notesLabels[value % 7]

    def getDuration(self, value):
        current_duration = 1/self.allowedDurations[value%8]
        if self.timeSignature != None:
            tsRealValue = self.timeSignature[0] / self.timeSignature[1]
            while current_duration > tsRealValue:
                value = value + 1
                current_duration = 1/self.allowedDurations[value%8]
        return self.allowedDurations[value%8]

    def getAlteration(self, noteLabel, value):
        result = value%3
        if(result == 0):
            return noteLabel
        elif (result == 1):
            return noteLabel + "b"
        else:
            return noteLabel + "#"

    def getChordOrArpeggio(self, input_bar):
        notes = input_bar.get_note_names()
        random.seed()
        chord = chords.major_triad(notes[random.randint(0,len(notes) - 1)])
        new_bar = Bar()
        #nc = NoteContainer(chord)
        #new_bar.place_notes(nc, 1)
        #return new_bar
        if(len(notes) % 2 != 0):
            #this will be a chord
            nc = NoteContainer(chord)
            new_bar.place_notes(nc, 1)
            return new_bar
        else:
            #this will be an arpeggio
            duration = 0
            print(str(len(chord)))
            for note in chord:
                if(duration == 0):
                    duration = 2
                else:
                    duration = 4
                new_bar.place_notes(note, duration)
            return new_bar

