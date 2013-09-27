# Author: Avishai Ish-Shalom <avishai@fewbytes.com>
# License: MIT


class Hashie(dict):
    """A ruby style Hashie/mash object.
     It recursively sets missing keys to additional hashie objects,
    so you can set nested properties with ease. E.G.
    h = Hashie()
    h['misc']['start'] = True
    h.misc.delay = 2
    """
    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        return self.__setitem__(name, value)

    def __getitem__(self, item):
        if not self.__contains__(item):
            self.__setitem__(item, Hashie())
        return super(Hashie, self).__getitem__(item)

    def __contains__(self, key, *keys):
        if not keys:
            return super(Hashie, self).__contains__(key)
        elif super(Hashie, self).__contains__(key):
            super_key = super(Hashie, self).__getitem__(key)
            super_attr = getattr(super_key, '__contains__', lambda x: False)
            return super_attr(*keys)
        else:
            return False


def main():
    """Show example - should work in both python 2.7 and 3

    TODO: change this to actual tests
    """
    d = Hashie()

    d["a"]["b"] = 42

    print(d["a"]["b"])
    print(d.a.b)
    print(d["c"]["e"])
    print(d.c.e)

    d["a"]["e"]["f"] = 43
    print(d["a"]["e"]["f"])
    print(d.a.e.f)
    print(d.a.e)
    print(d.a)


if __name__ == "__main__":
    main()
