from django.conf import settings

def global_settings(request):
    # return any necessary values
    return {
        'ARTICLE_IMAGE_THUMB_PATH': settings.ARTICLE_IMAGE_THUMB_PATH,
        'ARTICLE_IMAGE_MEDIUM_PATH': settings.ARTICLE_IMAGE_MEDIUM_PATH,
        'ARTICLE_IMAGE_LARGE_PATH': settings.ARTICLE_IMAGE_LARGE_PATH,
        'ARTICLE_IMAGE_EXTRA_LARGE_PATH': settings.ARTICLE_IMAGE_EXTRA_LARGE_PATH,
        'PHOTOSHOOT_IMAGE_PATH': settings.PHOTOSHOOT_IMAGE_PATH,
        'AUTHOR_IMAGE_PATH': settings.AUTHOR_IMAGE_PATH,
	'EVENT_IMAGE_PATH': settings.EVENT_IMAGE_PATH,
        'QUICKBYTES_IMAGE_THUMB_PATH': settings.QUICKBYTES_IMAGE_THUMB_PATH,
        'QUICKBYTES_IMAGE_MEDIUM_PATH': settings.QUICKBYTES_IMAGE_MEDIUM_PATH,
        #'QUICKBYTES_IMAGE_LARGE_PATH': settings.QUICKBYTES_IMAGE_LARGE_PATH,
        'QUICKBYTES_IMAGE_EXTRA_LARGE_PATH': settings.QUICKBYTES_IMAGE_EXTRA_LARGE_PATH,
        'FEATURED_BOX_IMAGE_PATH': settings.FEATURED_BOX_IMAGE_PATH,
        'FEATURED_BOX2_IMAGE_PATH': settings.FEATURED_BOX2_IMAGE_PATH,
        'FEATURED_BOX3_IMAGE_PATH': settings.FEATURED_BOX3_IMAGE_PATH,
        'BUCKET_PATH': settings.BUCKET_PATH,
        'AWS_S3_BASE_URL': settings.AWS_S3_BASE_URL,
        'MAGAZINE_IMAGE_PATH':settings.MAGAZINE_IMAGE_PATH_URL,
        'EXPERT_IMAGE_PATH':settings.EXPERT_IMAGE_PATHS,
        'DEBATE_IMAGE_PATH':settings.DEBATE_IMAGE_PATHS,
        'MASTER_VIDEO_IMAGE_PATH':settings.VIDEO_THUMB,
        'MASTER_VIDEO_PATH':settings.VIDEO_MASTER,
        'QUOTES_IMAGE_PATH':settings.QUOTES_IMAGE
    }
