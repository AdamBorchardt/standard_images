#
#coding: utf-8
# Markdown Conversion
#
# This script demonstrates how you can convert Markdown documents
# to HTML and view the results in the built-in browser.
import PIL
import os, tempfile, codecs
import console, clipboard, webbrowser
from markdown2 import markdown
import Image
import photos
import webbrowser
DEMO = '''
![F.O Logo]('_Image_1')
Format: ![Alt Text](url)
# Foxorion Design
<p>This is <a href="https://ci-9267749214-48822a76.http.atlas.cdn.yimg.com/flickr2/64007559@N04/9267749214/9267749214_360p.mp4?dt=flickr&x=1445867716&b=700&m=video%2Fmp4&a=flickr&fn=9267749214_766.mp4&d=cp_d%3Dwww.flickr.com%26cp_t%3Ds%26cp%3D792600246%26mid%3D9267749214%26ufn%3D9267749214_766.mp4&s=139f27bbd5f2cbe04a57b57407cc48db" title="Title">
#VID_C4D_Dir-Render</a> inline link.</p>
hashtags: #architecture
<p><a href="https://www.flickr.com/gp/64007559@N04/t7WrsT/">This link</a> has no
title attribute.</p>
<p><a href="http://example.net/">This link</a> has no
title attribute.</p>
<p><a href="http://giphy.com/gifs/scarlett-johansson-lucy-box-office-41YIr4dnSd96g/">This link</a> is for a simple
gif to render on galleryMd.</p>

**KEYWORDS**
<p>[#Architect][1]
<p>
<p>[#Artist Quotes][4]
<p>
<p>[#Design][5]
'''
DEMO2 = '''''
<p>[#Albums][12]
<p>[#Presidential_Quotes][16]
<p>[#All_Foxorion_Images][52]
you can see my
<p>[#Why_Im_a_democrat][74]
<p>[#Why_I'm_not_a_republican'][92]
or that I am pro education not indoctrination.
<p>[#Religion_Poisons_Everything][99]

^If this is too simple
and you can Download an apple flash player. @ <p>[Puffin Browser Link][17]
If you want to embed images, this is how you do it:

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
![Image of whatever](https://avatars2.githubusercontent.com/u/14189485?v=3&s=400)

Markdown makes it easy to make text **bold** or *italic*,
and to add [Foxor:on Des:gn Stud:os][2].
to the list of

You can also format block quotes:

> Any intelligent fool can make things bigger, more
> complex, and more violent. It takes a touch of genius
> -- and a lot of courage -- to move in the opposite
> direction.

*-- adamborchardt*

...and code blocks:

    from markdown2 import markdown
    text = "*hello world*"
    html = markdown(text)
    print html

For more detailed information about Markdown,
please read the [Design Range and Resumé][3]
on the project page.
[12]: http://www.digimouth.com/news/media/2011/09/google-logo.jpg
[1]: https://m.flickr.com/#/search/advanced_QM_q_IS_architect_AND_ss_IS_2_AND_prefs_photos_IS_1_AND_mt_IS_all_AND_w_IS_64007559@N04
[2]: http://www.foxorion.com
[3]: http://www.foxorion.org
[4]: https://m.flickr.com/#/search/advanced_QM_q_IS_art_quotes_AND_ss_IS_2_AND_prefs_photos_IS_1_AND_mt_IS_all_AND_w_IS_64007559@N04
[5]: https://m.flickr.com/#/search/advanced_QM_q_IS_design_AND_ss_IS_2_AND_prefs_photos_IS_1_AND_mt_IS_all_AND_w_IS_64007559@N04
[16]: https://m.flickr.com/#/search/advanced_QM_q_IS_presidential_quotes_AND_ss_IS_2_AND_prefs_photos_IS_1_AND_mt_IS_all_AND_w_IS_64007559@N04
[17]: https://appsto.re/us/2shmC.i
mark this down
*My design has no range*
<a href="https://www.flickr.com/photos/64007559@N04/sets/">FoxorionFLICKR</a>
[92]: http://www.foxorion.org
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
'''
TEMPLATE = '''
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<style>
body {
        font-family: helvetica;
        font-size: 18px;
        color: #;

}
blockquote {
        border-left: solid 3px #bbb;
        margin-left: 0px;
        padding-left: 10px;
}
pre {
        border: 1px solid #bbb;
        border-radius: 3px;
        padding: 3px;
        background-color: #f8f8f8;
}
code {
        font-family: DejaVuSansMono, monospace;
}
#wrapper {
        margin: 20px;}
</style>
</head>
<body>
<div id="wrapper">
{{CONTENT}}
</div>
</body>
</html>
'''
def main():
        choice = console.alert('Markdown Conversion', '', 'Demo', 'Convert Clipboard')
        md = DEMO + DEMO2 if choice == 1 else clipboard.get()
        html = markdown(md, extras=['smarty-pants'])
        tempdir = tempfile.gettempdir()
        html_path = os.path.join(tempdir, 'temp.html')
        html = TEMPLATE.replace('{{CONTENT}}', html)
        with codecs.open(html_path, 'w', 'utf-8') as f:
                f.write(html)
        file_url = 'file://' + html_path
        webbrowser.open(file_url)

if __name__ == '__main__':
        main()
