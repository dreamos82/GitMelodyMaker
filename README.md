# GitSongMaker

Let's your commits play a melody for you.

This project is just an experiment, made more for fun than with serious purposes. 

The idea behind it is try to see how a melody created from git commits stats "sound". 

So far i'm using a very naive approeach, converting the stats to notes attributes using the mod operation (probably i will do something more elaborate in the future). 

The output is generated in midi format.

## Usage

```bash
    python3 melodymaker path_togit_repo [filename]
```

* filename is an optional parameter if not provided, it will default to gitMelodyYYYYMMDDhhmmss.mid
* path_to_git_repo is the local path to the git repository you want to play!

## How the conversion work

The idea behind is that the conversion will be made using the stats available in every single commit. These values are: 

* lines added (*a*)
* lines deleted (*d*)
* total lines (added + deleted) (*l*)
* number of files changed (*f*)

Actually only one converter is implemented, based on the mod value of the commit stats. 

### The ModConverter
This is the first converter implemented. It works pretty simply, it takes the statistics as they are and convert them using the mod operation. 

The approach used is pretty naive. Given a tuple that is consisting of commit items values, so composed by the following values: *{a, d, l, f}*, the note is obtained in the following way:

* *Octave :=  a%8*
* *Alteration := f%2*
* *Duration := (d%4)+1*
* *Note := l%7*

This approach is temporary and it can change in any moment. 

In case the duration of the note will be higher than the space left in the bar, the gap will be filled with the selected note or a rest for the duration left in the measure (it is randomly decided). And a new Bar item will be created.


### Adding new Converter

Converters implement the abstract class ConverterToNote. So first think if you want to create a convert is inherit from it:

```python
    from converters.convertertonote import ConverterToNote

    class ModConverter(ConverterToNote):
        #Your implementation here!
```


