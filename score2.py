
# pylint: disable=missing-function-docstring, unspecified-encoding

import json

FILEPATH = 'animal_score.json'

def read_vanilla_json():

    fileobj_read = open(FILEPATH, 'r')
    score_obj = json.load(fileobj_read)
    return score_obj

def write_2_json(score):

    score_str = json.dumps(score)

    fileobj_write = open(FILEPATH, 'w')
    fileobj_write.write(score_str)
    fileobj_write.close()

# read - read ram's score
def read_json():

    score_obj = read_vanilla_json()

    toronto_score = score_obj['lion']

    print(f'[READ] lion_score: {toronto_score}')

# create new record (sharmila)
def create_new_record():

    score = read_vanilla_json()

    scaborough_score = 87
    score['zebra'] = scaborough_score

    write_2_json(score)

    print('[CREATE] zebra score added in the file')

# update kevin's score to 87
def update_record():

    score = read_vanilla_json()
    score['tiger'] = 94

    write_2_json(score)

    print('[UPDATE] tiger score updated in the file')

# delete azar
def delete_record():

    score = read_vanilla_json()
    score.pop('giraffe')

    write_2_json(score)

    print('[DELETE] giraffe score deleted from the file')


read_json()
create_new_record()
update_record()
delete_record()