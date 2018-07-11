import yippi

def test_yippi():
    res = yippi.search().post(['girly', 'male'], limit=1, rating="q", order="score")[0]
    res.id
    res.tags
    res.locked_tags
    res.description
    res.creator_id
    res.author
    res.change
    res.source
    res.sources
    res.score
    res.fav_count
    res.md5
    res.file_size
    res.file_url
    res.file_ext
    res.rating
    res.status
    res.width
    res.height
    res.has_comments
    res.has_notes
    res.has_children
    res.children
    res.parent
    res.artist
    post = yippi.post(16352)
    post.id
    post.tags
    post.locked_tags
    post.description
    post.creator_id
    post.author
    post.change
    post.source
    post.sources
    post.score
    post.fav_count
    post.md5
    post.file_size
    post.file_url
    post.file_ext
    post.rating
    post.status
    post.width
    post.height
    post.has_comments
    post.has_notes
    post.has_children
    post.children
    post.parent
    post.artist
    user = yippi.search.user(name="Error-")[0]
    user.artist_tags
    user.avatar
    user.created_at
    user.id
    level = user.level
    user.name
    stat = user.stats
    stat.blip_count
    stat.comment_count
    stat.del_post_count
    stat.edit_count
    stat.favorite_count
    stat.forum_post_count
    stat.neg_user_records
    stat.neutral_user_records
    stat.note_count
    stat.pool_update_count
    stat.pos_user_records
    stat.post_count
    stat.set_count
    stat.wiki_count
    level.string
    level.value
    artist = yippi.search().artist("slyus")[0]
    artist.group_name
    artist.id
    artist.is_active
    artist.name
    artist.other_names
    artist.updater_id
    artist.urls
    artist.version