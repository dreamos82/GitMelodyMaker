from git import Repo
import mingus.core.notes as notes
from mingus.midi import midi_file_out
#from mingus.containers import NoteContainer
from mingus.containers import Note
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers import Composition

import ConverterFactory as cf
import datetime
import sys
import random


#repo = Repo('/home/vetinari/Projects/Extensions/chrome_parameters')
#repo = Repo('/home/vetinari/Projects/tmp/projectt')
#repo = Repo('/home/vetinari/Projects/vos/V-OS')
def main():
    repo = Repo(sys.argv[1])
    factory = cf.ConverterFactory()
    converter = factory.get_converter("mod")
    curtime = datetime.datetime.now()
    if (len(sys.argv) == 3):
        target_file = sys.argv[2]
    else:
        target_file = "gitmelody" + str(curtime.year) + str(curtime.month) + str(curtime.hour) \
            + str(curtime.minute) + str(curtime.second) + ".mid"

    commits = list(repo.iter_commits('master'))
    
    timesignature = converter.getTimeSignature(commits)
    tsValue = timesignature[0]/timesignature[1]
    print(tsValue)
    print(timesignature)
    
    #nc = NoteContainer()
    bar = Bar()
    if timesignature != None:
        bar.set_meter((timesignature[0], timesignature[1]))
    t = Track()
    t2 = Track()
    dursum = 0
    tsValue = 1
    c = Composition()
    #durations are between 1 and 128
    for item in commits:
        #note_item = get_note_from_commit(item.stats.total)
        note_item = converter.getNoteFromCommit(item.stats.total)
        if (dursum + (1/note_item[1]) <= tsValue):
            dursum = dursum + 1/note_item[1]
            bar.place_notes(note_item[0], note_item[1])
        else:
            dursum=0
            if(bar.space_left() > 0):
                booleanValue = bool(random.getrandbits(1))
                if booleanValue == True:
                    bar.place_notes(note_item[0], bar.space_left())
                else:
                    bar.place_rest(bar.space_left())                
            t.add_bar(bar)
            second_line=converter.getChordOrArpeggio(bar)
            t2.add_bar(second_line)
            bar = Bar()
            bar.set_meter((timesignature[0], timesignature[1]))
    c.add_track(t)
    c.add_track(t2)
    print(bar.meter)

        #bar.place_notes(note_item[0], note_item[1])
        #t.add_notes(note_item[0])
    
        #print(item.stats.total['insertions'])
        #print(item.stats.additions)
        #print(item.stats.deletions)
        #print(item.stats.total)a
    
    #nc = NoteContainer(["A", "C", "E"])
    #midi_file_out.write_Track(target_file, t)
    midi_file_out.write_Composition(target_file, c)

if __name__ == "__main__":
    main()

