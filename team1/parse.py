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

limit = None


def main(actor_1, actor_2):

    global limit

    films = films_staring(actor_1)

    best = None
    worst = None

    for i, result in enumerate(go_deep(films, actor_2)):

        if best is None or len(result) < len(best):
            best = result[:]
            limit = len(best)

        if worst is None or len(result) > len(worst):
            worst = result

    print "Common films between %s and %s" % (actor_1, actor_2)

    print "Found a total of %s solutions" % i
    print "Worst solution contained %s films" % len(worst)
    print "Best solution contained %s films" % len(best)

    print "\nLinked by the following films:"
    for film in best:
        print "- %s (%s)" % (film, ', '.join(sorted(data_set[film])))


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
                yield branch
            elif limit is None or len(branch) < limit:
                for result in go_deep(films_staring(actor), target, branch[:]):
                    yield result

if __name__ == "__main__":

    actor_1 = 'YH'
    actor_2 = 'ZQ'

    main(actor_1, actor_2)
