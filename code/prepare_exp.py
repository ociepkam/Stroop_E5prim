#!/usr/bin/env python
# -*- coding: utf8 -*

import random
import math
from psychopy import visual

stim_text = {'CZERWONY': 'red', 'NIEBIESKI': '#5e75d9', 'BRAZOWY': '#574400', 'ZIELONY': 'green'}  # text: color
half_word_pos = {'CZERWONY': {"small_big": [-32, 32], "big_small": [-31, 31]},
                 'NIEBIESKI': {"small_big": [-27, 27], "big_small": [-28, 28]},
                 'BRAZOWY': {"small_big": [-27, 27], "big_small": [-27, 27]},
                 'ZIELONY': {"small_big": [-27, 27], "big_small": [-27, 27]}}
stim_neutral = "HHHHHHHH"

colors_text = list(stim_text.keys())
random.shuffle(colors_text)
colors_names = [stim_text[color] for color in colors_text]
left_hand = colors_text[:2]
right_hand = colors_text[2:]

last_color = None


def prepare_trial(trial_type, win, text_height, words_dist, small_letters_font, big_letters_font, small_letters_size, big_letters_size):
    global last_color

    if trial_type == 'trial_con_con':
        possible_text = list(stim_text.keys())
        if last_color is not None:
            possible_text.remove([k for k, v in stim_text.items() if v == last_color][0])
        text = random.choice(possible_text)
        color = stim_text[text]
        words = [text, text]
        stim1 = visual.TextStim(win, color=color, text=words[0], height=text_height, pos=(0, words_dist / 2))
        stim2 = visual.TextStim(win, color=color, text=words[1], height=text_height, pos=(0, -words_dist / 2))
        stim_list = [stim1, stim2]

    elif trial_type.startswith("trial_inc_inc_"):
        text = random.choice(list(stim_text.keys()))
        if text in left_hand:
            possible_colors = [stim_text[key] for key in right_hand]
        else:
            possible_colors = [stim_text[key] for key in left_hand]
        if last_color in possible_colors:
            possible_colors.remove(last_color)
        color = random.choice(possible_colors)
        if trial_type == "trial_inc_inc_different1":
            words = [text.upper(), text.lower()]
            stim1 = visual.TextStim(win, color=color, text=words[0], height=big_letters_size, pos=(0, words_dist / 2), font=big_letters_font)
            stim2 = visual.TextStim(win, color=color, text=words[1], height=small_letters_size, pos=(0, -words_dist / 2), font=small_letters_font)
            stim_list = [stim1, stim2]
        elif trial_type == "trial_inc_inc_different2":
            words = [text.lower(), text.upper()]
            stim1 = visual.TextStim(win, color=color, text=words[0], height=small_letters_size, pos=(0, words_dist / 2), font=small_letters_font)
            stim2 = visual.TextStim(win, color=color, text=words[1], height=big_letters_size, pos=(0, -words_dist / 2), font=big_letters_font)
            stim_list = [stim1, stim2]
        elif trial_type == "trial_inc_inc_reversed1":
            half = math.ceil(len(text)/2)
            words = [text[:half].upper() + text[half:].lower(), text[:half].lower() + text[half:].upper()]

            stim1_pos = (half_word_pos[text]["big_small"][0], words_dist / 2)
            stim1 = visual.TextStim(win, color=color, text=text[:half].upper(), height=big_letters_size, pos=stim1_pos, font=big_letters_font)

            stim2_pos = (half_word_pos[text]["big_small"][1], words_dist / 2)
            stim2 = visual.TextStim(win, color=color, text=text[half:].lower(), height=small_letters_size, pos=stim2_pos, font=small_letters_font)

            stim3_pos = (half_word_pos[text]["small_big"][0], -words_dist / 2)
            stim3 = visual.TextStim(win, color=color, text=text[:half].lower(), height=small_letters_size, pos=stim3_pos, font=small_letters_font)

            stim4_pos = (half_word_pos[text]["small_big"][1], -words_dist / 2)
            stim4 = visual.TextStim(win, color=color, text=text[half:].upper(), height=big_letters_size, pos=stim4_pos, font=big_letters_font)

            stim_list = [stim1, stim2, stim3, stim4]

        elif trial_type == "trial_inc_inc_reversed2":
            half = math.ceil(len(text) / 2)
            words = [text[:half].lower() + text[half:].upper(), text[:half].upper() + text[half:].lower()]

            stim1_pos = (half_word_pos[text]["small_big"][0], words_dist / 2)
            stim1 = visual.TextStim(win, color=color, text=text[:half].lower(), height=small_letters_size, pos=stim1_pos, font=small_letters_font)

            stim2_pos = (half_word_pos[text]["small_big"][1], words_dist / 2)
            stim2 = visual.TextStim(win, color=color, text=text[half:].upper(), height=big_letters_size, pos=stim2_pos, font=big_letters_font)

            stim3_pos = (half_word_pos[text]["big_small"][0], -words_dist / 2)
            stim3 = visual.TextStim(win, color=color, text=text[:half].upper(), height=big_letters_size, pos=stim3_pos, font=big_letters_font)

            stim4_pos = (half_word_pos[text]["big_small"][1], -words_dist / 2)
            stim4 = visual.TextStim(win, color=color, text=text[half:].lower(), height=small_letters_size, pos=stim4_pos, font=small_letters_font)

            stim_list = [stim1, stim2, stim3, stim4]

        elif trial_type == "trial_inc_inc_merged1":
            half = math.ceil(len(text) / 2)
            words = [text[:half].lower() + text[half:].upper(), text[:half].lower() + text[half:].upper()]

            stim1_pos = (half_word_pos[text]["small_big"][0], words_dist / 2)
            stim1 = visual.TextStim(win, color=color, text=text[:half].lower(), height=small_letters_size, pos=stim1_pos, font=small_letters_font)

            stim2_pos = (half_word_pos[text]["small_big"][1], words_dist / 2)
            stim2 = visual.TextStim(win, color=color, text=text[half:].upper(), height=big_letters_size, pos=stim2_pos, font=big_letters_font)

            stim3_pos = (half_word_pos[text]["small_big"][0], -words_dist / 2)
            stim3 = visual.TextStim(win, color=color, text=text[:half].lower(), height=small_letters_size, pos=stim3_pos, font=small_letters_font)

            stim4_pos = (half_word_pos[text]["small_big"][1], -words_dist / 2)
            stim4 = visual.TextStim(win, color=color, text=text[half:].upper(), height=big_letters_size, pos=stim4_pos, font=big_letters_font)

            stim_list = [stim1, stim2, stim3, stim4]

        elif trial_type == "trial_inc_inc_merged2":
            half = math.ceil(len(text) / 2)
            words = [text[:half].upper() + text[half:].lower(), text[:half].upper() + text[half:].lower()]

            stim1_pos = (half_word_pos[text]["big_small"][0], words_dist / 2)
            stim1 = visual.TextStim(win, color=color, text=text[:half].upper(), height=big_letters_size, pos=stim1_pos, font=big_letters_font)

            stim2_pos = (half_word_pos[text]["big_small"][1], words_dist / 2)
            stim2 = visual.TextStim(win, color=color, text=text[half:].lower(), height=small_letters_size, pos=stim2_pos, font=small_letters_font)

            stim3_pos = (half_word_pos[text]["big_small"][0], -words_dist / 2)
            stim3 = visual.TextStim(win, color=color, text=text[:half].upper(), height=big_letters_size, pos=stim3_pos, font=big_letters_font)

            stim4_pos = (half_word_pos[text]["big_small"][1], -words_dist / 2)
            stim4 = visual.TextStim(win, color=color, text=text[half:].lower(), height=small_letters_size, pos=stim4_pos, font=small_letters_font)

            stim_list = [stim1, stim2, stim3, stim4]

        elif trial_type == "trial_inc_inc_same1":
            words = [text.upper(), text.upper()]
            stim1 = visual.TextStim(win, color=color, text=words[0], height=big_letters_size, pos=(0, words_dist / 2), font=big_letters_font)
            stim2 = visual.TextStim(win, color=color, text=words[1], height=big_letters_size, pos=(0, -words_dist / 2), font=big_letters_font)
            stim_list = [stim1, stim2]
        elif trial_type == "trial_inc_inc_same2":
            words = [text.lower(), text.lower()]
            stim1 = visual.TextStim(win, color=color, text=words[0], height=small_letters_size, pos=(0, words_dist / 2), font=small_letters_font)
            stim2 = visual.TextStim(win, color=color, text=words[1], height=small_letters_size, pos=(0, -words_dist / 2), font=small_letters_font)
            stim_list = [stim1, stim2]
        else:
            raise Exception(f'{trial_type} - wrong trigger type')

    elif trial_type == 'trial_neu_neu':
        possible_colors = list(stim_text.values())
        if last_color is not None:
            possible_colors.remove(last_color)
        color = random.choice(possible_colors)
        words = [stim_neutral, stim_neutral]
        stim1 = visual.TextStim(win, color=color, text=words[0], height=text_height, pos=(0, words_dist / 2))
        stim2 = visual.TextStim(win, color=color, text=words[1], height=text_height, pos=(0, -words_dist / 2))
        stim_list = [stim1, stim2]

    else:
        raise Exception(f'{trial_type} - wrong trigger type')

    last_color = color

    # print({'trial_type': trial_type, 'text': words, 'color': color, 'stim': [stim1, stim2]})
    return {'trial_type': trial_type, 'text': words, 'color': color, 'stim': stim_list}


def prepare_part(trials_con_con,
                 trials_inc_inc_different1, trials_inc_inc_different2,
                 trials_inc_inc_reversed1, trials_inc_inc_reversed2,
                 trials_inc_inc_merged1, trials_inc_inc_merged2,
                 trials_inc_inc_same1, trials_inc_inc_same2,
                 trials_neu_neu,
                 win, text_height, words_dist,
                 small_letters_font, big_letters_font, small_letters_size, big_letters_size):
    trials = ['trial_con_con'] * trials_con_con + \
             ['trial_inc_inc_different1'] * trials_inc_inc_different1 + \
             ['trial_inc_inc_different2'] * trials_inc_inc_different2 + \
             ['trial_inc_inc_reversed1'] * trials_inc_inc_reversed1 + \
             ['trial_inc_inc_reversed2'] * trials_inc_inc_reversed2 + \
             ['trial_inc_inc_merged1'] * trials_inc_inc_merged1 + \
             ['trial_inc_inc_merged2'] * trials_inc_inc_merged2 + \
             ['trial_inc_inc_same1'] * trials_inc_inc_same1 + \
             ['trial_inc_inc_same2'] * trials_inc_inc_same2 + \
             ['trial_neu_neu'] * trials_neu_neu
    random.shuffle(trials)
    return [prepare_trial(trial_type, win, text_height, words_dist, small_letters_font, big_letters_font, small_letters_size, big_letters_size) for trial_type in trials]


def prepare_exp(config, win, text_size):
    text_height = 1.5 * text_size
    training1_trials = prepare_part(config['Training1_trials_con_con'],
                                    config['Training1_trials_inc_inc_different1'],
                                    config['Training1_trials_inc_inc_different2'],
                                    config['Training1_trials_inc_inc_reversed1'],
                                    config['Training1_trials_inc_inc_reversed2'],
                                    config['Training1_trials_inc_inc_merged1'],
                                    config['Training1_trials_inc_inc_merged2'],
                                    config['Training1_trials_inc_inc_same1'],
                                    config['Training1_trials_inc_inc_same2'],
                                    config['Training1_trials_neu_neu'],
                                    win, text_height, config["words_dist"],
                                    config["small_letters_font"], config["big_letters_font"], config["small_letters_size"], config["big_letters_size"])

    training2_trials = prepare_part(config['Training2_trials_con_con'],
                                    config['Training2_trials_inc_inc_different1'],
                                    config['Training2_trials_inc_inc_different2'],
                                    config['Training2_trials_inc_inc_reversed1'],
                                    config['Training2_trials_inc_inc_reversed2'],
                                    config['Training2_trials_inc_inc_merged1'],
                                    config['Training2_trials_inc_inc_merged2'],
                                    config['Training2_trials_inc_inc_same1'],
                                    config['Training2_trials_inc_inc_same2'],
                                    config['Training2_trials_neu_neu'],
                                    win, text_height, config["words_dist"],
                                    config["small_letters_font"], config["big_letters_font"], config["small_letters_size"], config["big_letters_size"])

    experiment_trials = prepare_part(config['Experiment_trials_con_con'],
                                     config['Experiment_trials_inc_inc_different1'],
                                     config['Experiment_trials_inc_inc_different2'],
                                     config['Experiment_trials_inc_inc_reversed1'],
                                     config['Experiment_trials_inc_inc_reversed2'],
                                     config['Experiment_trials_inc_inc_merged1'],
                                     config['Experiment_trials_inc_inc_merged2'],
                                     config['Experiment_trials_inc_inc_same1'],
                                     config['Experiment_trials_inc_inc_same2'],
                                     config['Experiment_trials_neu_neu'],
                                     win, text_height, config["words_dist"],
                                     config["small_letters_font"], config["big_letters_font"], config["small_letters_size"], config["big_letters_size"])

    return [training1_trials, training2_trials], experiment_trials, colors_text, colors_names
