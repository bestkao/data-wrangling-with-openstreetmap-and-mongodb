# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "Jamie xx")
    pretty_print(results)

    artist_id = results["artists"][0]["id"]
    print "\nARTIST:"
    pretty_print(results["artists"][0])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]

    print "\nALL TITLES:"
    for t in release_titles:
        print t

    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    print "\nNUMBER OF BANDS NAMED 'FIRST AID KIT':"
    pretty_print(len([result for result in results["artists"] if result["name"] == "First Aid Kit"]))

    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    print "\nBEGIN_AREA NAME FOR QUEEN:"
    pretty_print(results["artists"][0]["begin-area"]["name"])

    results = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    print "\nSPANISH ALIAS FOR BEATLES:"
    aliases = results["artists"][0]["aliases"]
    pretty_print((alias for alias in aliases if alias["locale"] == "es").next()["name"])

    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    print "\nNIRVANA DISAMBIGUATION:"
    pretty_print(results["artists"][0]["disambiguation"])

    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    print "\nONE DIRECTION FORMED ON:"
    pretty_print(results["artists"][0]["life-span"]["begin"])


if __name__ == '__main__':
    main()
