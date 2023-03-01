import itertools
import pretty_midi
import random
import datetime
import time

#########INSTRUCTIONS
# 1. Set the scale_root to desired scale root
# 2. Set the mod_scale_type to desired scale type
# 3. Set octave_int to desired octave
# 4. Set gen_progressions to desired number of progressions to generate
# 5. (Optional) Set convert_to_midi_io to True and set desired file path on line 780 to generate MIDI file

#########INSTALL PRETTY_MIDI
# pip install pretty_midi


#########START TIME
start_time = time.time()

#########MASTER SETTINGS
master_print_io = False
convert_to_midi_io = False
octave_int = 1
gen_progressions = 100

#########MASTER CHORD LIST
all_chords = []

#########ALL NOTES
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

#########SET SCALE ROOT
scale_root = 'C' #Choose Scale Root

scale_notes_ext = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
if scale_notes_ext[0] != scale_root:
    for i in range(12):
        if scale_notes_ext[i] == scale_root:
            scale_notes_ext = scale_notes_ext[i:] + scale_notes_ext[:i]
            break

scale_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
if scale_notes[0] != scale_root:
    for i in range(12):
        if scale_notes[i] == scale_root:
            scale_notes = scale_notes[i:] + scale_notes[:i]
            break

#########DEFINE SCALE TYPE
major_scale = [scale_notes[0], scale_notes[2], scale_notes[4], scale_notes[5], scale_notes[7], scale_notes[9], scale_notes[11]]
dorian_scale = [scale_notes[0], scale_notes[2], scale_notes[3], scale_notes[5], scale_notes[7], scale_notes[9], scale_notes[10]]
phrygian_scale = [scale_notes[0], scale_notes[1], scale_notes[3], scale_notes[5], scale_notes[7], scale_notes[8], scale_notes[10]]
lydian_scale = [scale_notes[0], scale_notes[2], scale_notes[4], scale_notes[6], scale_notes[7], scale_notes[9], scale_notes[11]]
mixolydian_scale = [scale_notes[0], scale_notes[2], scale_notes[4], scale_notes[5], scale_notes[7], scale_notes[9], scale_notes[10]]
aeolian_scale = [scale_notes[0], scale_notes[2], scale_notes[3], scale_notes[5], scale_notes[7], scale_notes[8], scale_notes[10]]
locrian_scale = [scale_notes[0], scale_notes[1], scale_notes[3], scale_notes[5], scale_notes[6], scale_notes[8], scale_notes[10]]
harmonic_minor_scale = [scale_notes[0], scale_notes[2], scale_notes[3], scale_notes[5], scale_notes[7], scale_notes[8], scale_notes[11]]
melodic_minor_scale = [scale_notes[0], scale_notes[2], scale_notes[3], scale_notes[5], scale_notes[7], scale_notes[9], scale_notes[11]]

#########SET SCALE TYPE
mod_scale_type = major_scale #Choose Scale Type

#########SET SCALE TYPE NAME
if mod_scale_type == major_scale:
    mod_scale_type_name = 'Major'
elif mod_scale_type == dorian_scale:
    mod_scale_type_name = 'Dorian'
elif mod_scale_type == phrygian_scale:
    mod_scale_type_name = 'Phrygian'
elif mod_scale_type == lydian_scale:
    mod_scale_type_name = 'Lydian'
elif mod_scale_type == mixolydian_scale:
    mod_scale_type_name = 'Mixolydian'
elif mod_scale_type == aeolian_scale:
    mod_scale_type_name = 'Aeolian'
elif mod_scale_type == locrian_scale:
    mod_scale_type_name = 'Locrian'
elif mod_scale_type == harmonic_minor_scale:
    mod_scale_type_name = 'Harmonic Minor'
elif mod_scale_type == melodic_minor_scale:
    mod_scale_type_name = 'Melodic Minor'

#########PRINT SCALE
print('-' * 50)
print(f'SCALE: {scale_root}, {mod_scale_type_name}')
print(f'NOTES: {mod_scale_type}')
print('')


#########CREATE CHORD FUNCTION
def create_chord(scale_notes, scale_notes_ext, mod_scale_type, chord_type):
    chords = []
    for i in range(len(scale_notes_ext)):
        if scale_notes_ext[i] in mod_scale_type:
            chord = [scale_notes[i]]
            for j in chord_type:
                chord.append(scale_notes[(i+j)%12])
            chords.append(chord)

    chords_to_remove = []
    for chord in chords:
        for note in chord:
            if note not in mod_scale_type:
                chords_to_remove.append(chord)
                break

    for chord in chords_to_remove:
        chords.remove(chord)

    if not chords:
        pass
    else:
        return chords

#########ALL PERMUTATIONS FUNCTION
def all_permutations(chords):
    permutations = []
    if chords:
        for chord in chords:
            permutations.extend(list(itertools.permutations(chord)))
        return remove_duplicate_permutations(permutations)
    else:
        pass

def remove_duplicate_permutations(chords_permutations):
    chords_permutations_processed = []
    for i in chords_permutations:
        if i not in chords_permutations_processed:
            chords_permutations_processed.append(i)
    return chords_permutations_processed

#########ALL CHORDS LIST FUNCTION
def all_chords_list(chords):
    all_chords = []
    if chords:
        for chord in chords:
            all_chords.extend(chord)
        return all_chords
    else:
        pass


#########CHORD VOICINGS
all_permutations_io = True
chord_voices = 6

#########MAJOR CHORDS

#########VOICING LOGIC 6 VOICE CHORDS
# IF CHORD LENGTH IS 3, ADD OCTAVE, 3RD ABOVE AND 5TH ABOVE
# IF CHORD LENGTH IS 4, ADD OCTAVE AND 3RD ABOVE
# IF CHORD LENGTH IS 5, ADD 3RD ABOVE
# IF CHORD LENGTH == 6, NO CHANGE
# IF CHORD LENGTH IS 7, REMOVE 5TH
# IF CHORD LENGTH IS 8, REMOVE 5TH AND 11TH

if chord_voices == 6:
    major_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 12, 16, 19])
    major_7_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 11, 12, 16])
    major_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 11, 14, 16])
    major_11_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 11, 14, 17])
    major_13_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 11, 14, 17, 21])
    major_6_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 9, 12, 16])
    major_6_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 9, 14, 16])
    major_sharp_11_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 11, 16, 18])
    major_7_flat_13_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 11, 16, 20])

else:
    pass

#########MAJOR CHORDS ALL PERMUTATIONS
major_chords_all = all_permutations(major_chords)
major_7_chords_all = all_permutations(major_7_chords)
major_9_chords_all = all_permutations(major_9_chords)
major_11_chords_all = all_permutations(major_11_chords)
major_13_chords_all = all_permutations(major_13_chords)
major_6_chords_all = all_permutations(major_6_chords)
major_6_9_chords_all = all_permutations(major_6_9_chords)
major_sharp_11_chords_all = all_permutations(major_sharp_11_chords)
major_7_flat_13_chords_all = all_permutations(major_7_flat_13_chords)

#########PRINT MAJOR CHORDS
if master_print_io == True:
    if all_permutations_io == True:
        print('MAJOR CHORDS ALL PERMUTATIONS:')
        print('')
        print(f'MAJOR: {major_chords_all}')
        print(f'MAJOR 7: {major_7_chords_all}')
        print(f'MAJOR 9: {major_9_chords_all}')
        print(f'MAJOR 11: {major_11_chords_all}')
        print(f'MAJOR 13: {major_13_chords_all}')
        print(f'MAJOR 6: {major_6_chords_all}')
        print(f'MAJOR 6/9: {major_6_9_chords_all}')
        print(f'MAJOR #11: {major_sharp_11_chords_all}')
        print(f'MAJOR 7 b13: {major_7_flat_13_chords_all}')
        print('')
    else:
        print('-' * 50)
        print('MAJOR CHORDS:')
        print('')
        print(major_chords)
        print(major_7_chords)
        print(major_9_chords)
        print(major_11_chords)
        print(major_13_chords)
        print(major_6_chords)
        print(major_6_9_chords)
        print(major_sharp_11_chords)
        print(major_7_flat_13_chords)
        print('')
else:
    pass

#########MINOR CHORDS

#########VOICING LOGIC 6 VOICE CHORDS
# IF CHORD LENGTH IS 3, ADD OCTAVE, 3RD ABOVE AND 5TH ABOVE
# IF CHORD LENGTH IS 4, ADD OCTAVE AND 3RD ABOVE
# IF CHORD LENGTH IS 5, ADD 3RD ABOVE
# IF CHORD LENGTH == 6, NO CHANGE
# IF CHORD LENGTH IS 7, REMOVE 5TH
# IF CHORD LENGTH IS 8, REMOVE 5TH AND 11TH

if chord_voices == 6:
    minor_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 12, 15, 19])
    minor_7_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 10, 12, 15])
    minor_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 10, 14, 15])
    minor_11_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 10, 14, 17])
    minor_13_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 10, 14, 17, 21])
    minor_6_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 9, 12, 15])
    minor_major_7_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 11, 12, 15])
    minor_major_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 11, 14, 15])
    minor_major_13_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 11, 14, 17, 21])
    minor_major_flat_13_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 7, 11, 15, 20])

#########MINOR CHORDS ALL PERMUTATIONS
minor_chords_all = all_permutations(minor_chords)
minor_7_chords_all = all_permutations(minor_7_chords)
minor_9_chords_all = all_permutations(minor_9_chords)
minor_11_chords_all = all_permutations(minor_11_chords)
minor_13_chords_all = all_permutations(minor_13_chords)
minor_6_chords_all = all_permutations(minor_6_chords)
minor_major_7_chords_all = all_permutations(minor_major_7_chords)
minor_major_9_chords_all = all_permutations(minor_major_9_chords)
minor_major_13_chords_all = all_permutations(minor_major_13_chords)
minor_major_flat_13_chords_all = all_permutations(minor_major_flat_13_chords)

#########PRINT MINOR CHORDS
if master_print_io == True:
    if all_permutations_io == True:
        print('-' * 50)
        print('MINOR CHORDS ALL PERMUTATIONS:')
        print('')
        print(f'MINOR: {minor_chords_all}')
        print(f'MINOR 7: {minor_7_chords_all}')
        print(f'MINOR 9: {minor_9_chords_all}')
        print(f'MINOR 11: {minor_11_chords_all}')
        print(f'MINOR 13: {minor_13_chords_all}')
        print(f'MINOR 6: {minor_6_chords_all}')
        print(f'MINOR MAJOR 7: {minor_major_7_chords_all}')
        print(f'MINOR MAJOR 9: {minor_major_9_chords_all}')
        print(f'MINOR MAJOR 13: {minor_major_13_chords_all}')
        print(f'MINOR MAJOR b13: {minor_major_flat_13_chords_all}')
        print('')
    else:
        print('-' * 50)
        print('MINOR CHORDS:')
        print('')
        print(minor_chords)
        print(minor_7_chords)
        print(minor_9_chords)
        print(minor_11_chords)
        print(minor_13_chords)
        print(minor_6_chords)
        print(minor_major_7_chords)
        print(minor_major_9_chords)
        print(minor_major_13_chords)
        print(minor_major_flat_13_chords)
        print('')
else:
    pass

#########DOMINANT CHORDS

#########VOICING LOGIC 6 VOICE CHORDS
# IF CHORD LENGTH IS 3, ADD OCTAVE, 3RD ABOVE AND 5TH ABOVE
# IF CHORD LENGTH IS 4, ADD OCTAVE AND 3RD ABOVE
# IF CHORD LENGTH IS 5, ADD 3RD ABOVE
# IF CHORD LENGTH == 6, NO CHANGE
# IF CHORD LENGTH IS 7, REMOVE 5TH
# IF CHORD LENGTH IS 8, REMOVE 5TH AND 11TH

if chord_voices == 6:
    dominant_7_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 10, 12, 16])
    dominant_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 10, 14, 16])
    dominant_13_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 10, 14, 17, 21])
    dominant_7_flat_5_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 6, 10, 12, 16])
    dominant_7_flat_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 10, 13, 16])
    dominant_7_sharp_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 10, 15, 16])
    dominant_7_sharp_11_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 7, 10, 16, 18])
    dominant_9_flat_5_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 6, 10, 14, 16])
    dominant_9_sharp_5_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [4, 8, 10, 14, 16])

#########DOMINANT CHORDS ALL PERMUTATIONS
dominant_7_chords_all = all_permutations(dominant_7_chords)
dominant_9_chords_all = all_permutations(dominant_9_chords)
dominant_13_chords_all = all_permutations(dominant_13_chords)
dominant_7_flat_5_chords_all = all_permutations(dominant_7_flat_5_chords)
dominant_7_flat_9_chords_all = all_permutations(dominant_7_flat_9_chords)
dominant_7_sharp_9_chords_all = all_permutations(dominant_7_sharp_9_chords)
dominant_7_sharp_11_chords_all = all_permutations(dominant_7_sharp_11_chords)
dominant_9_flat_5_chords_all = all_permutations(dominant_9_flat_5_chords)
dominant_9_sharp_5_chords_all = all_permutations(dominant_9_sharp_5_chords)

#########PRINT DOMINANT CHORDS
if master_print_io == True:
    if all_permutations_io == True:
        print('-' * 50)
        print('DOMINANT CHORDS ALL PERMUTATIONS:')
        print('')
        print(f'DOMINANT 7: {dominant_7_chords_all}')
        print(f'DOMINANT 9: {dominant_9_chords_all}')
        print(f'DOMINANT 13: {dominant_13_chords_all}')
        print(f'DOMINANT 7 b5: {dominant_7_flat_5_chords_all}')
        print(f'DOMINANT 7 b9: {dominant_7_flat_9_chords_all}')
        print(f'DOMINANT 7 #9: {dominant_7_sharp_9_chords_all}')
        print(f'DOMINANT 7 #11: {dominant_7_sharp_11_chords_all}')
        print(f'DOMINANT 9 b5: {dominant_9_flat_5_chords_all}')
        print(f'DOMINANT 9 #5: {dominant_9_sharp_5_chords_all}')
        print('')
    else:
        print('-' * 50)
        print('DOMINANT CHORDS:')
        print('')
        print(dominant_7_chords)
        print(dominant_9_chords)
        print(dominant_13_chords)
        print(dominant_7_flat_5_chords)
        print(dominant_7_flat_9_chords)
        print(dominant_7_sharp_9_chords)
        print(dominant_7_sharp_11_chords)
        print(dominant_9_flat_5_chords)
        print(dominant_9_sharp_5_chords)
        print('')
else:
    pass

#########SUSPENDED CHORDS

#########VOICING LOGIC 6 VOICE CHORDS
# IF CHORD LENGTH IS 3, ADD 2ND (SUS2) OR 4TH (SUS4), OCTAVE AND 5TH
# IF CHORD LENGTH IS 4, ADD 2ND (SUS2) OR 4TH (SUS4) AND OCTAVE
# IF CHORD LENGTH IS 5, ADD 2ND (SUS2) OR 4TH (SUS4)
# IF CHORD LENGTH == 6, NO CHANGE
# IF CHORD LENGTH IS 7, REMOVE 2ND (SUS2) OR 4TH (SUS4)
# IF CHORD LENGTH IS 8, REMOVE 2ND (SUS2) OR 4TH (SUS4) AND OCTAVE

if chord_voices == 6:
    suspended_2_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [2, 7, 12, 14, 19])
    suspended_4_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [5, 7, 12, 17, 19])
    suspended_4_7_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [5, 7, 10, 12, 17])
    suspended_4_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [5, 7, 10, 14, 17])
    suspended_11_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [2, 7, 10, 14, 17])
    suspended_4_flat_9_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [5, 7, 10, 13, 17])

#########SUSPENDED CHORDS ALL PERMUTATIONS
suspended_2_chords_all = all_permutations(suspended_2_chords)
suspended_4_chords_all = all_permutations(suspended_4_chords)
suspended_4_7_chords_all = all_permutations(suspended_4_7_chords)
suspended_4_9_chords_all = all_permutations(suspended_4_9_chords)
suspended_11_chords_all = all_permutations(suspended_11_chords)
suspended_4_flat_9_chords_all = all_permutations(suspended_4_flat_9_chords)

#########PRINT SUSPENDED CHORDS
if master_print_io == True:
    if all_permutations_io == True:
        print('-' * 50)
        print('SUSPENDED CHORDS ALL PERMUTATIONS:')
        print('')
        print(f'SUSPENDED 2: {suspended_2_chords_all}')
        print(f'SUSPENDED 4: {suspended_4_chords_all}')
        print(f'SUSPENDED 4 7: {suspended_4_7_chords_all}')
        print(f'SUSPENDED 4 9: {suspended_4_9_chords_all}')
        print(f'SUSPENDED 11: {suspended_11_chords_all}')
        print(f'SUSPENDED 4 b9: {suspended_4_flat_9_chords_all}')
        print('')
    else:
        print('-' * 50)
        print('SUSPENDED CHORDS:')
        print('')
        print(suspended_2_chords)
        print(suspended_4_chords)
        print(suspended_4_7_chords)
        print(suspended_4_9_chords)
        print(suspended_11_chords)
        print(suspended_4_flat_9_chords)
        print('')
else:
    pass

#########DIMINISHED CHORDS

#########VOICING LOGIC 6 VOICE CHORDS
# IF CHORD LENGTH IS 3, ADD OCTAVE, 3RD ABOVE AND 5TH ABOVE
# IF CHORD LENGTH IS 4, ADD OCTAVE AND 3RD ABOVE
# IF CHORD LENGTH IS 5, ADD 3RD ABOVE
# IF CHORD LENGTH == 6, NO CHANGE
# IF CHORD LENGTH IS 7, REMOVE 5TH
# IF CHORD LENGTH IS 8, REMOVE 5TH AND 11TH

if chord_voices == 6:
    diminished_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 6, 12, 15, 18])
    diminished_7_chords = create_chord(scale_notes, scale_notes_ext, mod_scale_type, [3, 6, 10, 12, 15])

#########DIMINISHED CHORDS ALL PERMUTATIONS
diminished_chords_all = all_permutations(diminished_chords)
diminished_7_chords_all = all_permutations(diminished_7_chords)

#########PRINT DIMINISHED CHORDS
if master_print_io == True:
    if all_permutations_io == True:
        print('-' * 50)
        print('DIMINISHED CHORDS ALL PERMUTATIONS:')
        print('')
        print(f'DIMINISHED: {diminished_chords_all}')
        print(f'DIMINISHED 7: {diminished_7_chords_all}')
        print('')
    else:
        print('-' * 50)
        print('DIMINISHED CHORDS:')
        print('')
        print(diminished_chords)
        print(diminished_7_chords)
        print('')
else:
    pass

chord_list = []

for name in dir():
    if name.endswith('_chords'):
        chord_list.append(eval(name))

for chord in chord_list:
    if chord == None:
        chord_list.remove(chord)

all_chord_types = [major_chords_all, 
                   major_7_chords_all, 
                   major_9_chords_all, 
                   major_11_chords_all,
                   major_13_chords_all, 
                   major_6_chords_all, 
                   major_6_9_chords_all, 
                   major_sharp_11_chords_all,
                   major_7_flat_13_chords_all, 
                   minor_chords_all, 
                   minor_7_chords_all, 
                   minor_9_chords_all, 
                   minor_11_chords_all, 
                   minor_13_chords_all, 
                   minor_6_chords_all, 
                   minor_major_7_chords_all, 
                   minor_major_9_chords_all, 
                   minor_major_13_chords_all, 
                   minor_major_flat_13_chords_all,
                   dominant_7_chords_all,
                   dominant_9_chords_all,
                   dominant_13_chords_all,
                   dominant_7_flat_5_chords_all,
                   dominant_7_flat_9_chords_all,
                   dominant_7_sharp_9_chords_all,
                   dominant_7_sharp_11_chords_all,
                   dominant_9_flat_5_chords_all,
                   dominant_9_sharp_5_chords_all,
                   suspended_2_chords_all,
                   suspended_4_chords_all,
                   suspended_4_7_chords_all,
                   suspended_4_9_chords_all,
                   suspended_11_chords_all,
                   suspended_4_flat_9_chords_all,
                   diminished_chords_all,
                   diminished_7_chords_all]

chord_labels = ['Major', 'Major 7', 'Major 9', 'Major 11', 'Major 13', 'Major 6', 'Major 6/9', 'Major #11', 'Major 7b13', 
                'Minor', 'Minor 7', 'Minor 9', 'Minor 11', 'Minor 13', 'Minor 6', 'Minor/Major 7', 'Minor/Major 9', 'Minor/Major 13', 'Minor/Major b13', 
                'Dominant 7', 'Dominant 9', 'Dominant 13', 'Dominant 7b5', 'Dominant 7b9', 'Dominant 7#9', 'Dominant 7#11', 'Dominant 9b5', 'Dominant 9#5', 
                'Suspended 2', 'Suspended 4', 'Suspended 4/7', 'Suspended 4/9', 'Suspended 11', 'Suspended 4b9', 
                'Diminished', 'Diminished 7']


all_chord_types_dict = {}

for i, chord_type in enumerate(all_chord_types):
    all_chord_types_dict[chord_labels[i]] = chord_type

#########ALL CHORD TYPES AND PERMUTATIONS IN KEY
for chords in all_chord_types:
    if chords:
        for chord in chords:
            all_chords.append(chord)

def remove_duplicates(all_chords):
    all_chords_processed = []
    for i in all_chords:
        if i not in all_chords_processed:
            all_chords_processed.append(i)
    return all_chords_processed

all_chords_processed = remove_duplicates(all_chords)


#########CHORD PREPROCESSING
octave = octave_int
octave_second_note = octave_int
octave_third_note = octave_int
octave_fourth_note = octave_int
octave_fifth_note = octave_int
octave_sixth_note = octave_int

chords_octave_processed = []

notes_octave = ['C0', 'C#0', 'D0', 'D#0', 'E0', 'F0', 'F#0', 'G0', 'G#0', 'A0', 'A#0', 'B0', 
                'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 
                'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 
                'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 
                'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 
                'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 
                'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 
                'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7', 
                'C8', 'C#8', 'D8', 'D#8', 'E8', 'F8', 'F#8', 'G8', 'G#8', 'A8', 'A#8', 'B8', 
                'C9', 'C#9', 'D9', 'D#9', 'E9']

#########CONVERT NOTES TO FREQUENCIES
tuning_a4 = 440
pitches = [12 * 2 + c for c in range(len(notes_octave))]
frequencies = [round(tuning_a4 * (2 ** ((pitch - 69) / 12)), 2) for pitch in pitches]
note_frequency_dict = dict(zip(notes_octave, frequencies))


for chord_preprocessed in all_chords_processed:
    first_note_octave_index = notes_octave.index(chord_preprocessed[0] + str(octave))
    second_note_octave_index = notes_octave.index(chord_preprocessed[1] + str(octave_second_note))
    third_note_octave_index = notes_octave.index(chord_preprocessed[2] + str(octave_third_note))
    fourth_note_octave_index = notes_octave.index(chord_preprocessed[3] + str(octave_fourth_note))
    fifth_note_octave_index = notes_octave.index(chord_preprocessed[4] + str(octave_fifth_note))
    sixth_note_octave_index = notes_octave.index(chord_preprocessed[5] + str(octave_sixth_note))

    first_note_octave_letter = notes_octave[first_note_octave_index]
    second_note_octave_letter = notes_octave[second_note_octave_index]
    third_note_octave_letter = notes_octave[third_note_octave_index]
    fourth_note_octave_letter = notes_octave[fourth_note_octave_index]
    fifth_note_octave_letter = notes_octave[fifth_note_octave_index]
    sixth_note_octave_letter = notes_octave[sixth_note_octave_index]

    if second_note_octave_index <= first_note_octave_index:
        second_note_octave_index = second_note_octave_index + 12
        second_note_octave_letter = notes_octave[second_note_octave_index]

    if third_note_octave_index <= second_note_octave_index:
        third_note_octave_index = third_note_octave_index + 12
        third_note_octave_letter = notes_octave[third_note_octave_index]
        if third_note_octave_index <= second_note_octave_index:
            third_note_octave_index = third_note_octave_index + 12
            third_note_octave_letter = notes_octave[third_note_octave_index]

    if fourth_note_octave_index <= third_note_octave_index:
        fourth_note_octave_index = fourth_note_octave_index + 12
        fourth_note_octave_letter = notes_octave[fourth_note_octave_index]
        if fourth_note_octave_index <= third_note_octave_index:
            fourth_note_octave_index = fourth_note_octave_index + 12
            fourth_note_octave_letter = notes_octave[fourth_note_octave_index]
            if fourth_note_octave_index <= third_note_octave_index:
                fourth_note_octave_index = fourth_note_octave_index + 12
                fourth_note_octave_letter = notes_octave[fourth_note_octave_index]

    if fifth_note_octave_index <= fourth_note_octave_index:
        fifth_note_octave_index = fifth_note_octave_index + 12
        fifth_note_octave_letter = notes_octave[fifth_note_octave_index]
        if fifth_note_octave_index <= fourth_note_octave_index:
            fifth_note_octave_index = fifth_note_octave_index + 12
            fifth_note_octave_letter = notes_octave[fifth_note_octave_index]
            if fifth_note_octave_index <= fourth_note_octave_index:
                fifth_note_octave_index = fifth_note_octave_index + 12
                fifth_note_octave_letter = notes_octave[fifth_note_octave_index]
                if fifth_note_octave_index <= fourth_note_octave_index:
                    fifth_note_octave_index = fifth_note_octave_index + 12
                    fifth_note_octave_letter = notes_octave[fifth_note_octave_index]

    if sixth_note_octave_index <= fifth_note_octave_index:
        sixth_note_octave_index = sixth_note_octave_index + 12
        sixth_note_octave_letter = notes_octave[sixth_note_octave_index]
        if sixth_note_octave_index <= fifth_note_octave_index:
            sixth_note_octave_index = sixth_note_octave_index + 12
            sixth_note_octave_letter = notes_octave[sixth_note_octave_index]
            if sixth_note_octave_index <= fifth_note_octave_index:
                sixth_note_octave_index = sixth_note_octave_index + 12
                sixth_note_octave_letter = notes_octave[sixth_note_octave_index]
                if sixth_note_octave_index <= fifth_note_octave_index:
                    sixth_note_octave_index = sixth_note_octave_index + 12
                    sixth_note_octave_letter = notes_octave[sixth_note_octave_index]
                    if sixth_note_octave_index <= fifth_note_octave_index:
                        sixth_note_octave_index = sixth_note_octave_index + 12
                        sixth_note_octave_letter = notes_octave[sixth_note_octave_index]

    chords_octave_processed.append([first_note_octave_letter, second_note_octave_letter, third_note_octave_letter, fourth_note_octave_letter, fifth_note_octave_letter, sixth_note_octave_letter])

chords_no_octave = [[note.strip("0123456789") for note in chord] for chord in chords_octave_processed]


#########CHORD FIRST INTERVAL FILTER
i = 0
while i < len(chords_octave_processed):
    chord = chords_octave_processed[i]
    chord_1_index = [notes_octave.index(note) for note in chord]
    chord_1_first_interval = chord_1_index[1] - chord_1_index[0]
    if chord_1_first_interval <= 3:
        chords_octave_processed.pop(i)
        continue
    i += 1


#########CHORD RANGE FILTER
i = 0
while i < len(chords_octave_processed):
    chord_range = chords_octave_processed[i]
    chord_1_index = [notes_octave.index(note_range) for note_range in chord_range]
    chord_1_range = max(chord_1_index) - min(chord_1_index)
    if chord_1_range > 36:
        chords_octave_processed.pop(i)
        continue
    i += 1


#########RANDOMIZE CHORD PROGRESSION
chord_progression = []
first_interval_length = 5
avg_index_length = 5
range_length = 5


i = 0

while i < gen_progressions:
    #########CHORD 1
    while True:
        chord_1 = random.choice(chords_octave_processed)
        chord_1_index = [notes_octave.index(note) for note in chord_1]
        chord_1_first_interval = chord_1_index[1] - chord_1_index[0]
        if chord_1_first_interval >= first_interval_length:
            break

    chord_progression.append(chord_1)

    chord_1_index = [notes_octave.index(note) for note in chord_1]
    chord_1_freq = [note_frequency_dict[note] for note in chord_1]
    chord_1_intervals = [round(chord_1_freq[i] / chord_1_freq[i - 1], 5) for i in range(1, len(chord_1_freq))]
    chord_1_interval_note_1 = [round(chord_1_freq[i] / chord_1_freq[0], 5) for i in range(1, len(chord_1_freq))]
    chord_1_interval_note_2 = [round(chord_1_freq[i] / chord_1_freq[1], 5) for i in range(2, len(chord_1_freq))]
    chord_1_interval_note_3 = [round(chord_1_freq[i] / chord_1_freq[2], 5) for i in range(3, len(chord_1_freq))]
    chord_1_interval_note_4 = [round(chord_1_freq[i] / chord_1_freq[3], 5) for i in range(4, len(chord_1_freq))]
    chord_1_interval_note_5 = [round(chord_1_freq[i] / chord_1_freq[4], 5) for i in range(5, len(chord_1_freq))]

    chord_1_avg_index = int(sum(chord_1_index) / len(chord_1_index))
    chord_1_range = max(chord_1_index) - min(chord_1_index)

    chord_1_no_octave = tuple([note.strip("0123456789") for note in chord_1])

    found = False
    for chord_label, chord_list in all_chord_types_dict.items():
        if chord_list:
            for chord in chord_list:
                if set(chord_1_no_octave) == set(chord) and not found:
                    print('-' * 50)
                    print('CHORD PROGRESSION', i + 1)
                    print('')
                    print(f'CHORD 1: {chord_1}, TYPE: {chord_label}')
                    found = True
        else:
            pass


    #########CHORD 2
    while True:
        chord_2 = random.choice(chords_octave_processed)
        chord_2_index = [notes_octave.index(note) for note in chord_2]
        chord_2_first_interval = chord_2_index[1] - chord_2_index[0]
        chord_2_avg_index = int(sum(chord_2_index) / len(chord_2_index))
        chord_2_range = max(chord_2_index) - min(chord_2_index)
        if ((chord_2_avg_index <= chord_1_avg_index + avg_index_length) and (chord_2_avg_index >= chord_1_avg_index - avg_index_length)) and chord_2_range <= chord_1_range + range_length and chord_2_range >= chord_1_range - range_length and chord_2_first_interval >= first_interval_length:
            chord_progression.append(chord_2)
            break

    chord_2_no_octave = tuple([note.strip("0123456789") for note in chord_2])

    found = False
    for chord_label, chord_list in all_chord_types_dict.items():
        if chord_list:
            for chord in chord_list:
                if set(chord_2_no_octave) == set(chord) and not found:
                    print(f'CHORD 2: {chord_2}, TYPE: {chord_label}')
                    found = True
        else:
            pass


    #########CHORD 3
    while True:
        chord_3 = random.choice(chords_octave_processed)
        chord_3_index = [notes_octave.index(note) for note in chord_3]
        chord_3_first_interval = chord_3_index[1] - chord_3_index[0]
        chord_3_avg_index = int(sum(chord_3_index) / len(chord_3_index))
        chord_3_range = max(chord_3_index) - min(chord_3_index)
        if ((chord_3_avg_index <= chord_2_avg_index + avg_index_length) and (chord_3_avg_index >= chord_2_avg_index - avg_index_length)) and ((chord_3_avg_index <= chord_1_avg_index + avg_index_length) and (chord_3_avg_index >= chord_1_avg_index - avg_index_length)) and chord_3_range <= chord_2_range + range_length and chord_3_range >= chord_2_range - range_length and chord_3_range <= chord_1_range + range_length and chord_3_range >= chord_1_range - range_length and chord_3_first_interval >= first_interval_length:
            chord_progression.append(chord_3)
            break

    chord_3_no_octave = tuple([note.strip("0123456789") for note in chord_3])

    found = False
    for chord_label, chord_list in all_chord_types_dict.items():
        if chord_list:
            for chord in chord_list:
                if set(chord_3_no_octave) == set(chord) and not found:
                    print(f'CHORD 3: {chord_3}, TYPE: {chord_label}')
                    found = True
        else:
            pass


    #########CHORD 4
    while True:
        chord_4 = random.choice(chords_octave_processed)
        chord_4_index = [notes_octave.index(note) for note in chord_4]
        chord_4_first_interval = chord_4_index[1] - chord_4_index[0]
        chord_4_avg_index = int(sum(chord_4_index) / len(chord_4_index))
        chord_4_range = max(chord_4_index) - min(chord_4_index)
        if ((chord_4_avg_index <= chord_3_avg_index + avg_index_length) and (chord_4_avg_index >= chord_3_avg_index - avg_index_length)) and ((chord_4_avg_index <= chord_1_avg_index + avg_index_length) and (chord_4_avg_index >= chord_1_avg_index - avg_index_length)) and chord_4_range <= chord_3_range + range_length and chord_4_range >= chord_3_range - range_length and chord_4_range <= chord_1_range + range_length and chord_4_range >= chord_1_range - range_length and chord_4_first_interval >= first_interval_length:
            chord_progression.append(chord_4)
            break

    chord_4_no_octave = tuple([note.strip("0123456789") for note in chord_4])

    found = False
    for chord_label, chord_list in all_chord_types_dict.items():
        if chord_list:
            for chord in chord_list:
                if set(chord_4_no_octave) == set(chord) and not found:
                    print(f'CHORD 4: {chord_4}, TYPE: {chord_label}')
                    print('')
                    found = True
        else:
            pass


    ######### CONVERT TO MIDI

    #########SET MIDI CONVERSION BOOLEAN
    if convert_to_midi_io == True:
        chord_py_chord = pretty_midi.PrettyMIDI()
        start_time = 0
        end_time = 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    #########CONVERT CHORD PROGRESSION TO MIDI
        name_counter = 0
        for chord_midi in chord_progression:
            chord_py_program = pretty_midi.instrument_name_to_program('Cello')
            chord_instrument = pretty_midi.Instrument(program=chord_py_program)
            for note_name in chord_midi:
                note_number = pretty_midi.note_name_to_number(note_name)
                note = pretty_midi.Note(velocity=100, pitch=note_number-12, start=start_time, end=end_time)
                chord_instrument.notes.append(note)
            chord_py_chord.instruments.append(chord_instrument)
            start_time += 1
            end_time += 1
            
    #########SAVE MIDI FILE
            chord_py_chord.write(f"/Applications/FL Studio 20.app/Contents/Resources/FL/Data/Patches/(INSERT FOLDER NAME)/{mod_scale_type_name}_{scale_root}_ChordPy_{timestamp}.mid")
        print('-' * 50)
        print('MIDI Conversion Enabled')
        print('')

    #########DISABLE MIDI CONVERSION
    else:
        print('-' * 50)
        print('MIDI Conversion Disabled')
        print('')

    i += 1

#########END TIMER
end_time = time.time()
total_time = end_time - start_time
print('-' * 50)
print("Time elapsed: {:.2f}s".format(total_time))
print('')