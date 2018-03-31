import urllib.request, json, datetime, yippi.object

Submission = yippi.object.Submission
Artist = yippi.object.Artist
User = yippi.object.User

headers = {
    'User-Agent': 'Yippi/1.0 (by Error- on e621)'
}

class search:
    """
    Main search feature, this doesn't have any parameter to process."""
    def post(tags : list, rating="e", limit=50, page=1, **kwargs):
        """
        Searches e621 submission
    
        :Parameters:
    
        tags : [:class:`list`]
            The tags that will be given to and processed by e621
        rating : [Optional :class:`str`]
            Rating that will be used to search, refer to `e621 cheatseet`_ for more information, defaults to "e"
        limit : [Optional :class:`int`]
            Limit total results from e621 API, defaults to 50
        page : [Optional :class:`int`]
            Scroll through the page given, defaults to page 1
    
        Every kwargs will be processed like what `e621 cheatseet` said
    
        .. _e621 cheatseet: https://e621.net/help/show/cheatsheet
    
        :Return:
    
        This command will return list of :class:Submission object"""
        extratags = []
        for kw in list(kwargs.items()):
            kw =':'.join(kw)
            extratags.append(kw)
        apiurl = 'https://e621.net/post/index.json?tags=%s+rating:%s+%s&limit=%s&page=%s' \
            % ('+'.join(tags), rating, '+'.join(extratags), limit, page)
        req = urllib.request.Request(apiurl, headers=headers)
        http = urllib.request.urlopen(req)
        results = json.loads(http.read().decode("utf-8"))
        objects = []
        for obj in results:
            esixobject = Submission(obj)
            objects.append(esixobject)
        return objects

    def artist(name : str, limit=10, order="name", page=1):
        """
        Searches e621 artist info

        :Parameters:

        name : [:class:`str`]
            Artist name that will be given as query to e621 API
        limit : [:class:`int`]
            Uhm, same as the :function:`post` one, defaults to 10
        order : [:class:`str`]
            Order the result based on "date" or "name", defaults to "name"
        page : [:class:`int`]
             Same as the :function: `search` one too

        :Returns:

        :class:`Artist` object of the artist"""
        apiurl = 'https://e621.net/artist/index.json?name=%s&limit=%s&order=%s&page=%s' \
            % (name, limit, order, page)
        req = urllib.request.Request(apiurl, headers=headers)
        http = urllib.request.urlopen(req)
        results = json.loads(http.read().decode("utf-8"))
        objects = []
        for obj in results:
            esixobject = Artist(obj)
            objects.append(esixobject)
        return objects

    def user(*, id="", name="", level=-1, order="name"):
        if not id and not name:
            print("Please specify either id or name!")
            return
        apiurl = "https://e621.net/user/index.json?id=%s&name=%s&level=%s&order=%s" % (id, name, level, order)
        req = urllib.request.Request(apiurl, headers=headers)
        http = urllib.request.urlopen(req)
        result = json.loads(http.read().decode("utf-8"))
        return User(result)

def post(id : int):
    """
    Opens a e621 post

    :Parameters:

    id : :class:`int`
        The post ID of a submission

    :Return:

    :class:`Submission` object of the post"""
    apiurl = "https://e621.net/post/show.json?id=%s" % (id)
    req = urllib.request.Request(apiurl, headers=headers)
    http = urllib.request.urlopen(req)
    result = json.loads(http.read().decode("utf-8"))
    return Submission(result)
