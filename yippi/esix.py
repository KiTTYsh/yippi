import urllib.request, json, datetime

headers = {
    'User-Agent': 'Yippi/1.0 (by Error- on e621)'
}

def search(tags : list, rating="e", limit=50, page=1, **kwargs):
    extratags = []
    for kw in list(kwargs.items()):
        kw =':'.join(kw)
        extratags.append(kw)
    apiurl = 'https://e621.net/post/index.json?tags=%s+rating:%s+%s&limit=%s&page=%s' \
        % ('+'.join(tags), rating, '+'.join(extratags), limit, page)
    req = urllib.request.Request(apiurl, headers=headers)
    http = urllib.request.urlopen(req)
    results = json.loads(http.read())
    objects = []
    for obj in results:
        esixobject = Submission(obj)
        objects.append(esixobject)
    return objects

def post(id : int):
    apiurl = "https://e621.net/post/show.json?id=%s" % (id)
    req = urllib.request.Request(apiurl, headers=headers)
    http = urllib.request.urlopen(req)
    result = json.loads(http.read())
    return Submission(result)

class Submission(object):
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
            self._tags = self.object['tags']
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
