import urllib.request, json, datetime

headers = {
    'User-Agent': 'Yippi/1.0 (by Error- on e621)'
}

class search():
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
            Uhm, same as the :function:`search` one, defaults to 10
        order : [:class:`str`]
            Order the result based on "date" or "name", defaults to "name"
        page : [:class:`int`M
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

class Submission(object):
    """
    A representation of e621 submission post object

    :Parameters:

    object : [:class:`dict`]
        A JSON or dict of the submission given from e621 API, this should be a valid JSON or everything will broke

    :Attributes:
    
    id : :class:`int`
        The post ID of the submission
    tags : :class:`list`
        Tags of the submission, splitted with every space
    locked_tags : :class:`bool`
        Check if the tags are locked for edit
    description : :class:`str`
        Description of the submission, if no description is given, this will be a `None` object
    created_at : :class:`str`
        Date of the submission is posted
    creator_id : :class:`int`
        The creator's user ID
    author : :class:`str`
        Author of the submission
    change : :class:`int`
        This thing is still unknown, e621 doesn't give any info about this
    source : :class:`str`
        Source of the submission, taken from :function:sources and took the very first value of it
    sources : :class:`list`
        List of the source of the submission
    score : :class:`int`
        The score of the submission
    fav_count : :class:`int`
        Total favorites of the submission
    md5 : :class:`str`
        MD5 checksum of the submission file
    file_size : :class:`int`
        Size of the submission file in bytes
    file_url : :class:`str`
        Submission file URL
    file_ext : :class:`str`
        Submission file extension
    rating : :class:`str`
        Rating of the submission, refer to `e621 cheatseet`_ for more information
    status : :class:`str`
        Submission status, one of: active, flagged, pending, deleted
    width : :class:`int`
        The width of the file in pixel
    height : :class:`int`
        Same as :function:width but with height
    has_comments : :class:`bool`
        Check if the submission has comments or not
    has_children : :class:`bool`
        Check if the submission has children post or not
    children : :class:`list`
        The child post of the submission, if there's none, it will return `None` object
    parent : :class:`int`
        Parent post of the submission, if there's none, it will return `None` object
    artist : :class:`list`
        The artist who draw the submission, of course.
        
    .. _e621 cheatseet: https://e621.net/help/show/cheatsheet"""
    
    def __init__(self, object):
        self.object = object
        self._id = None
        self._tags = None
        self._locked_tags = None
        self._description = None
        self._created_at = None
        self._creator_id = None
        self._author = None
        self._change = None
        self._source = None
        self._sources = None
        self._score = None
        self._fav_count = None
        self._md5 = None
        self._file_size = None
        self._file_url = None
        self._file_ext = None
        self._rating = None
        self._status = None
        self._width = None
        self._height = None
        self._has_comments = None
        self._has_notes = None
        self._has_children = None
        self._children = None
        self._parent = None
        self._artist = None

    def __repr__(self):
        return str(self.object)

    @property
    def created_at(self):
        created_timestamp = self.object['created_at']['s']
        self._created_at = datetime.datetime.fromtimestamp(int(created_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        return self._created_at

    @property
    def id(self):
        if self.object['id']:
            self._id = self.object['id']
        return self._id

    @property
    def tags(self):
        if self.object['tags']:
            self._tags = self.object['tags'].split(" ")
        return self._tags

    @property
    def locked_tags(self):
        if self.object['locked_tags']:
            self._locked_tags = self.object['locked_tags']
        return self._locked_tags

    @property
    def description(self):
        if self.object['description']:
            self._description = self.object['description']
        return self._description

    @property
    def creator_id(self):
        if self.object['creator_id']:
            self._creator_id = self.object['creator_id']
        return self._creator_id

    @property
    def author(self):
        if self.object['author']:
            self._author = self.object['author']
        return self._author

    @property
    def change(self):
        if self.object['change']:
            self._change = self.object['change']
        return self._change

    @property
    def source(self):
        if self.object['source']:
            self._source = self.object['source']
        return self._source

    @property
    def sources(self):
        if self.object['sources']:
            self._sources = self.object['sources']
        return self._sources

    @property
    def score(self):
        if self.object['score']:
            self._score = self.object['score']
        return self._score

    @property
    def fav_count(self):
        if self.object['fav_count']:
            self._fav_count = self.object['fav_count']
        return self._fav_count

    @property
    def md5(self):
        if self.object['md5']:
            self._md5 = self.object['md5']
        return self._md5

    @property
    def file_size(self):
        if self.object['file_size']:
            self._file_size = self.object['file_size']
        return self._file_size

    @property
    def file_url(self):
        if self.object['file_url']:
            self._file_url = self.object['file_url']
        return self._file_url

    @property
    def file_ext(self):
        if self.object['file_ext']:
            self._file_ext = self.object['file_ext']
        return self._file_ext

    @property
    def rating(self):
        if self.object['rating']:
            self._rating = self.object['rating']
        return self._rating

    @property
    def status(self):
        if self.object['status']:
            self._status = self.object['status']
        return self._status

    @property
    def width(self):
        if self.object['width']:
            self._width = self.object['width']
        return self._width

    @property
    def height(self):
        if self.object['height']:
            self._height = self.object['height']
        return self._height

    @property
    def has_comments(self):
        if self.object['has_comments']:
            self._has_comments = self.object['has_comments']
        return self._has_comments

    @property
    def has_notes(self):
        if self.object['has_notes']:
            self._has_notes = self.object['has_notes']
        return self._has_notes

    @property
    def has_children(self):
        if self.object['has_children']:
            self._has_children = self.object['has_children']
        return self._has_children

    @property
    def children(self):
        if self.object['children']:
            self._children = self.object['children']
            splitted = self._children.split(',')
            self._children = []
            for child in splitted:
                self._children.append(post(child))
        return self._children

    @property
    def parent(self):
        if self.object['parent_id']:
            self._parent = post(self.object['parent_id'])
        return self._parent

    @property
    def artist(self):
        if self.object['artist']:
            self._artist = self.object['artist']
        return self._artist

class Artist(object):
    """
    A representation of e621 artist info

    :Parameters:

    object : [:class:`dict`]

    :Attributes:

    id : :class:`int`
        e621 artist ID
    name : :class:`int`
        The artist name, of course
    other_names : :class:`str`
        Artist's alias(es), separared by comma
    group_name : :class:`str`
        The group or circle that this artist is a member of
    is_active : :class:`bool`
         Whether the artist is still active or not"""
    def __init__(self, object):
        self.object = object
        self._id = None
        self._name = None
        self._other_names = None
        self._group_name = None
        self._urls = None
        self._is_active = None
        self._version = None
        self._updater_id = None

    def __repr__(self):
        return str(self.object)

    @property
    def id(self):
        if self.object['id']:
            self._id = self.object['id']
        return self._id

    @property
    def name(self):
        if self.object['name']:
            self._id = self.object['name']
        return self._name

    @property
    def other_names(self):
        if self.object['other_names']:
            self._id = self.object['other_names']
        return self._other_names

    @property
    def group_name(self):
        if self.object['group_name']:
            self._id = self.object['group_name']
        return self._group_name

    @property
    def urls(self):
        if self.object['urls']:
            self._id = self.object['urls']
        return self._urls

    @property
    def is_active(self):
        if self.object['is_active']:
            self._id = self.object['is_active']
        return self._is_active

    @property
    def version(self):
        if self.object['version']:
            self._id = self.object['version']
        return self._version

    @property
    def updater_id(self):
        if self.object['updater_id']:
            self._id = self.object['updater_id']
        return self._updater_id
