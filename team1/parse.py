import json
import collections

searched = set()
films_data = json.load(file('sample_data.json'))
actor_index = collections.defaultdict(set)

for film, actors in films_data.iteritems():
    for actor in actors:
        actor_index[actor].add(film)


def check_actor_films(actor_1, actor_2):

    for film in actor_index[actor_1]:
        if actor_2 in films_data[film]:
            return film

best_len = None


def main(actor_1, actor_2):

    global best_len

    films = actor_index[actor_1]

    best = None
    worst = None

    for i, result in enumerate(go_deep(films, actor_2)):

        if best is None or len(result) < len(best):
            best = result
            best_len = len(best)

        if worst is None or len(result) > len(worst):
            worst = result

    print "Common films between %s and %s" % (actor_1, actor_2)

    print "Found a total of %s solutions" % i
    print "Worst solution contained %s films" % len(worst)
    print "Best solution contained %s films" % len(best)

    print "\nLinked by the following films:"
    for film in best:
        print "- %s (%s)" % (film, ', '.join(sorted(films_data[film])))


def go_deep(films, target, branch=None):

    for film in films:

        if film in searched:
            continue

        searched.add(film)

        if branch is None:
            branch = []
        else:
            branch = branch[:]

        branch.append(film)

        for actor in films_data[film]:

            common = check_actor_films(actor, target)
            if common:
                branch.append(common)
                yield branch[:]
            elif True or best_len is None or len(branch) < best_len:
                for result in go_deep(actor_index[actor], target, branch[:]):
                    yield result

if __name__ == "__main__":

    actor_1 = 'YH'
    actor_2 = 'ZQ'

    main(actor_1, actor_2)
