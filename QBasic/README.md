# My QBasic Practice
Nostalgia!
- Play Music (2021.02.20)
- Hello World (2020.02.27)


### Play Music (2021.02.20)
- Practice of functions : `BEEP` `SOUND` `PLAY`
- Run by `MS QuickBASIC v4.5`

#### Xerxes.bas
Using `SHELL` function to borrow the `CLS` command from DOS
```QBasic
 SHELL "CLS"
 PRINT "I am generous"
```
> I am generous

#### Sound.bas
Refer to ☞ https://en.wikibooks.org/wiki/QBasic/Sound
```QBasic
SHELL "CLS"


'BEEP

PRINT "BEEP"
BEEP
PRINT CHR$(7)
SLEEP


'SOUND

PRINT "SOUND" + CHR$(13) 'CHR$(13) : Line break

FOR i% = 1 TO 30
        SOUND i% * 100, 1  'Freqency, Duration
NEXT
SLEEP


'PLAY

PRINT "PLAY" + CHR$(13)
PLAY "L16 CDEFGAB>C" '> : Move up one octave
SLEEP
```
**Results** : [BEEP](./Sounds/QB_SOUND_BEEP.wav) [SOUND](./Sounds/QB_SOUND_SOUND.wav) [PLAY](./Sounds/QB_SOUND_PLAY.wav)  
(* These can't be played directly, but played after downloading.)

#### SchoolBell.bas
Play the same song with the keys of both C major and C minor
```QBasic
SHELL "CLS"

PRINT "School Bell"

PRINT "C major"

PLAY "MS G8G8A8A8 G8G8E4 G8G8E8E8 D6 P8"
PLAY "MS G8G8A8A8 G8G8E4 G8E8D8E8 C6 P8"

PRINT "C minor"

PLAY "MS G8G8A-8A-8 G8G8E-4 G8G8E-8E-8 D6 P8"
PLAY "MS G8G8A-8A-8 G8G8E-4 G8E-8D8E-8 C6 P8"
```
**Results** :
[C major](./Sounds/QB_PLAY_C major.wav) [C minor](./Sounds/QB_PLAY_C minor.wav)  
(* These can't be played directly, but played after downloading.)


### Hello World (2020.02.27)

#### HelloWorld.bas

```QBasic
print "Hello World!"
```
> Call to undefined sub 'print'

```QBasic
print("Hello World!")
```
> Call to undefined sub 'print'

```QBasic
print 'Hello World!'
```
> Call to undefined sub 'print'

How can I make `print` work?

```QBasic
PRINT "Hello World!"
```
> Hello World!

The secret was UPPER CASE!

```QBasic
PRINT 'Hello World!'
```
>
`''` seems to be used for single-line comments.

```QBasic
'You can't see what I'm saying.'
```
ㅋ
