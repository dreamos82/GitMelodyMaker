# GitSongMaker

Let's your commits play a melody for you.

This project is just an experiment, made more for fun than with serious purposes. 

The idea behind it is try to see how it "sound" a melody created from git commits stats. 

So far i'm using a very naive approeach, converting the stats to notes attributes using the mod operation (probably i will do something more elaborate in the future). 

The output is generated in midi format.

## Usage

```bash
    python3 melodymaker path_togit_repo [filename]
```

* filename is an optional parameter if not provided, it will default to gitMelodyYYYYMMDDhhmmss.mid
* path_to_git_repo is the local path to the git repository you want to play!
