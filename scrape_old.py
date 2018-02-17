import requests
from HTMLParser import HTMLParser
import json
import re
import BeautifulSoup
import os


h = HTMLParser()


if __name__ == '__main__':
    base_url = 'http://bmoregeo.com/wp-json/wp/v2'

    post_url = base_url + '/posts?page='
    category_url = base_url + '/categories'

    categories = dict([(c['id'], '' + c['name'].replace(' ', '-') + '') for c in requests.get(category_url).json()])

    for i in xrange(1,6):
        result = requests.get(post_url + str(i))
        for post in result.json():

            file_name = post['date_gmt'].split('T')[0] + '-' + post['slug'] + '.md'
            metadata = {
                'layout': 'post',
                'title': h.unescape(post['title']['rendered']),
                'date': post['date_gmt'],
                'excerpt': re.sub("<p><a class=\"button\" href=\".*\" title=\"More\">.*Read More.*</a></p>", "", h.unescape(post['excerpt']['rendered'])),
                'categories': json.dumps([categories[c] for c in post['categories']])
            }
            content = h.unescape(post['content']['rendered'])

            soup = BeautifulSoup.BeautifulSoup(content)
            images = soup.findAll("img", src=True)

            for image in images:
                image_source = re.sub('-[0-9]..x[0-9]..', '', image['src'])
                path = os.path.join('/Users/christopherfricke/Documents/Source/website/bmoregeo_jekyll/assets/image', image_source.replace('http://bmoregeo.com/wp-content/uploads/', ''))
                try:
                    os.makedirs(os.path.dirname(path))
                except:
                    pass

                """
                result = requests.get(image_source, stream=True)
                with open(path, 'wb') as playFile:
                    for chunk in result.iter_content(1024):
                        playFile.write(chunk)

                res = requests.get(image['src'], stream=True)
                mpath = os.path.join('/Users/christopherfricke/Documents/Source/website/bmoregeo_jekyll/assets/image', image['src'].replace('http://bmoregeo.com/wp-content/uploads/', ''))

                with open(mpath, 'wb') as playFile:
                    for chunk in res.iter_content(1024):
                        playFile.write(chunk)
                
                """


                image_html = '/Users/christopherfricke/Documents/Source/website/bmoregeo_jekyll/images/{}.html'.format(
                    image_source.replace('http://bmoregeo.com/wp-content/uploads/', '').replace('.png', '').replace('.jpg', '').replace('/','-'))

                try:
                    os.makedirs(os.path.dirname(image_html))
                except:
                    pass

                with open(image_html, 'w') as cursor:
                    lines = [
                        '---',
                        'layout: page',
                        'date: ' + metadata['date'],
                        'categories: ' + metadata['categories'],
                        '---',
                        '<img src="{}" />'.format(image_source.replace('http://bmoregeo.com/wp-content/uploads', '/assets/image'))
                    ]

                    for row in lines:
                        cursor.write(row.encode('utf8') + '\r\n')

                content = content.replace(image['src'], image['src'].replace('http://bmoregeo.com/wp-content/uploads',
                                                                             '/assets/image'))
                content = content.replace(image_source, '/images/{}.html'.format(image_source.replace('http://bmoregeo.com/wp-content/uploads/', '').replace('.png', '').replace('.jpg', '').replace('/','-')))


                if metadata['title'] == "State of the Map":
                    content = content.replace('<br style="clear: both" />', '')

            with open('/Users/christopherfricke/Documents/Source/website/bmoregeo_jekyll/_posts/' + file_name, 'w') as cursor:
                lines = [
                    '---',
                    'layout: post',
                    'title: "' + metadata['title'] + '"',
                    'date: ' + metadata['date'],
                    'categories: ' + metadata['categories'],
                    'excerpt: >\r\n ' + metadata['excerpt'].replace('\r\n', '').replace('\r','').replace('\n','') + '',
                    '---',
                    content
                ]

                for row in lines:
                    cursor.write(row.encode('utf8') + '\r\n')