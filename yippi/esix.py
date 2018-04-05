import urllib.request, json, datetime, yippi.object

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
    
        This command will return list of :class:`yippi.object.Submission` object"""
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
            esixobject = yippi.object.Submission(obj)
            objects.append(esixobject)
        return objects

    def artist(name : str, limit=10, order="name", page=1):
        """
        Searches e621 artist info

        :Parameters:

        name : [:class:`str`]
            Artist name that will be given as query to e621 API
        limit : [:class:`int`]
            Limit total results from e621 API, defaults to 50
        order : [:class:`str`]
            Order the result based on "date" or "name", defaults to "name"
        page : [:class:`int`]
             Scroll through the page given, defaults to page 1

        :Returns:

        :class:`yippi.object.Artist` object of the artist"""
        apiurl = 'https://e621.net/artist/index.json?name=%s&limit=%s&order=%s&page=%s' \
            % (name, limit, order, page)
        req = urllib.request.Request(apiurl, headers=headers)
        http = urllib.request.urlopen(req)
        results = json.loads(http.read().decode("utf-8"))
        objects = []
        for obj in results:
            esixobject = yippi.object.Artist(obj)
            objects.append(esixobject)
        return objects

    def user(*, id="", name="", level=-1, order="name"):
        """
        Searches user at e621

        :Parameters:

        id : [:class:`int`]
            The user ID to search
        name : [:class:`str`]
            Text query matching part or all of a user's name
        level : [:class:`int` or :class:`yippi.object.UserLevel]
            Permission level to search
        order : [:class:`str`]
            Sort of order, defaults to `name`

        :Returns:

        :class:`yippi.object.User` object"""
        if not id and not name:
            print("Please specify either id or name!")
            return
        if isinstance(level, yippi.object.UserLevel):
            level = level.value
        apiurl = "https://e621.net/user/index.json?id=%s&name=%s&level=%s&order=%s" % (id, name, level, order)
        req = urllib.request.Request(apiurl, headers=headers)
        http = urllib.request.urlopen(req)
        result = json.loads(http.read().decode("utf-8"))
        objects = []
        for obj in result:
            esixobject = yippi.object.User(obj)
            objects.append(esixobject)
        return objects

def post(id : int):
    """
    Opens a e621 post

    :Parameters:

    id : :class:`int`
        The post ID of a submission

    :Return:

    :class:`yippi.object.Submission` object of the post"""
    apiurl = "https://e621.net/post/show.json?id=%s" % (id)
    req = urllib.request.Request(apiurl, headers=headers)
    http = urllib.request.urlopen(req)
    result = json.loads(http.read().decode("utf-8"))
    return yippi.object.Submission(result)

def get_level(lvl : str):
    """
    Get the :class:`yippi.object.UserLevel` object of requested UserLevel"""
    Level = {
        'Everyone': -1,
        'Unactivated': 0,
        'Blocked': 10,
        'Member': 20,
        'Privileged': 30,
        'Staff': 34,
        'Janitor': 35,
        'Mod': 40,
        'Admin': 50
    }

    lvl = Level[lvl]
    return yippi.object.UserLevel(lvl)