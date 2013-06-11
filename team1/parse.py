from data import data_set

searched = set()


def films_staring(actor):

    films = set()

    for film, actors in data_set.iteritems():
        if actor in actors:
            films.add(film)

    return films


def check_actor_films(actor_1, actor_2):

    for film in films_staring(actor_1):
        if actor_2 in data_set[film]:
            return film


def main(actor_1, actor_2):

    common = films_staring(actor_1).intersection(films_staring(actor_2))

    if len(common) > 0:
        return common.pop()

    films = films_staring(actor_1)
    go_deep(films, actor_2)


def go_deep(films, target, branch=None):

    for film in films:

        if film in searched:
            continue

        searched.add(film)

        if not branch:
            branch = []

        branch.append(film)

        for actor in data_set[film]:

            common = check_actor_films(actor, target)
            if common:
                branch.append(common)
                print branch
                print data_set[branch[0]]
                print data_set[branch[-1]]
                return True
            else:
                r = go_deep(films_staring(actor), target, branch[:])
                if r:
                    return True

if __name__ == "__main__":

    actor_1 = 'YH'
    actor_2 = 'ZQ'

    print actor_1, actor_2

    main(actor_1, actor_2)
