# usr/bin/env python

import datetime


class Day:

    LUNI = '\tLuni\n\n\tGeografie\n\tFranceza\n\tReligie\n\tIstorie\n\tRomana'
    MARTI = '\tMarti\n\n\tMate\n\tEngleza\n\tEconomie\n\tFinantarea ' \
            'afacerii\n\tNegocierea afacerii\n\tRomana'
    MIERCURI = '\tMiercuri\n\n\tMate\n\tMate\n\tFinantarea afaceri\n' \
               '\tMediul concurential\n\tSavin\n\tRomana'
    JOI = '\tJoi\n\n\tMediul conurential\n\tGeografie\n\tNegocierea afacerii' \
        '\n\tEconomie\n\tSport\n\tEngleza'
    VINERI = '\tVineri\n\n\tSavin\n\tFranceza\n\tSavin\n\tSavin\n\tSavin\n' \
             '\tTic'

    __weekDay__ = {
        0: 'Luni',
        1: 'Marti',
        2: 'Miercuri',
        3: 'Joi',
        4: 'Vineri'
    }

    def __init__(self, number: int):
        self.day = self.__weekDay__[number].upper()

    def __repr__(self):
        if self.day == 'LUNI':
            return self.LUNI
        elif self.day == 'MARTI':
            return self.MARTI
        elif self.day == 'MIERCURI':
            return self.MIERCURI
        elif self.day == 'JOI':
            return self.JOI
        else:
            return self.VINERI


def dailySchedule(func: 'functie') -> str:
    def inner():
        now = datetime.datetime.today().weekday()+1
        func(now)
    return inner


@dailySchedule
def main(now: str) -> None:
    print(Day(now))


if __name__ == "__main__":
    main()
