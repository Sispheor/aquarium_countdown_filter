import re


class IntervalString:

    @classmethod
    def get_second_from_sting(cls, interval_string):

        # the string must contains a number followed by a letter s or m or h or d. E.g: 50m
        full_regex = r'^\d+[smhd]{1}$'

        if re.match(full_regex, interval_string):
            regex_integer = r'\d+'
            group = re.search(regex_integer, interval_string)
            integer = group[0]

            regex_letter = r'[smhd]{1}$'
            group = re.search(regex_letter, interval_string)
            letter = group[0]

            dict_multiplier = {
                "s": 1,
                "m": 60,
                "h": 60 * 60,
                "d": 60 * 60 * 24
            }

            return int(integer) * dict_multiplier[letter]

        return None
