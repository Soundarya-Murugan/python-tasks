
# pylint: disable=missing-function-docstring, unspecified-encoding

import json

FILEPATH = 'product_score.json'

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

    smartphone_score = score_obj['smartphone']

    print(f'[READ] smartphone_score: {smartphone_score}')

# create new record (sharmila)
def create_new_record():

    score = read_vanilla_json()

    scaborough_score = 89
    score['smartwatch'] = scaborough_score

    write_2_json(score)

    print('[CREATE] smartwatch score added in the file')

# update kevin's score to 87
def update_record():

    score = read_vanilla_json()
    score['tablet'] = 86

    write_2_json(score)

    print('[UPDATE] tablet score updated in the file')

# delete azar
def delete_record():

    score = read_vanilla_json()
    score.pop('headphones')

    write_2_json(score)

    print('[DELETE] headphones score deleted from the file')


read_json()
create_new_record()
update_record()
delete_record()