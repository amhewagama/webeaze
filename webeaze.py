"""
Author: Amila Hewagama
Contact: amhewagama@gmail.com
Description: Introducing "WebEaze: The Ultimate Website Creation Framework"

WebEaze is a cutting-edge website creation framework designed to revolutionize the way websites are built and maintained. With a strong focus on simplicity, memory efficiency, time optimization, and top-notch quality, WebEaze empowers developers and designers to craft stunning websites with ease.

Key Features:

    Simplicity at its Core:
    WebEaze is built with simplicity in mind. Its intuitive interface and streamlined workflow ensure that even beginners can create captivating websites without a steep learning curve.

    Memory Efficiency:
    We understand the importance of optimized memory usage. WebEaze is engineered to utilize system resources efficiently, ensuring smooth performance even on resource-constrained environments.

    Time Efficiency:
    Time is of the essence, and with WebEaze, you can bring your website ideas to life quickly. The framework's pre-designed templates and customizable components accelerate development, saving your valuable time.

    Uncompromising Quality:
    Quality is non-negotiable, and WebEaze upholds the highest standards. Rigorous testing and continuous improvements guarantee that your websites are reliable, secure, and visually impressive.

    Modern Look and Feel:
    Stay ahead of the curve with modern, visually appealing designs. WebEaze offers a vast collection of contemporary themes and styles that ensure your websites always look fresh and up-to-date.

    SEO-Optimized:
    Boost your website's visibility and search engine rankings with WebEaze's adherence to SEO best practices. Your websites will be optimized for improved discoverability and organic traffic.

WebEaze is the go-to solution for web developers, designers, and businesses seeking to create remarkable websites without compromising on efficiency or quality. Whether you're starting a personal blog, launching an online store, or building a corporate website, WebEaze has you covered.

MIT License:
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import json
import re

#run in apachee server=1, static html=0
HTACCESS = 1

#compiled files put in ('dir/' or '')
PUBLIC_DIR = 'www/'

#app dir
APP_DIR = 'app'

#app dir
BLOG_NAME = 'blog'

#source files
SOURCE_FILE = f"{APP_DIR}/source.json"
HEADER_FILE = f"{APP_DIR}/header_li.html"
FOOTER_FILE = f"{APP_DIR}/footer_li.html"
BLOG_TEMPLATE = f"{APP_DIR}/blog_template.html"
GRID_TEMPLATE = f"{APP_DIR}/grid_template.html"
PROFILE_MENUS = f"{APP_DIR}/profile_menus.html"

#file list
FILE_LIST = ["index.html", "about.html", "landscape.html", "travel.html", "monochrome.html", "nature.html", "privacy-policy.html","awards-wbpa.html","awards-hp.html","awards-gc.html","awards-gc.html","awards-pp.html","awards-100asa.html","awards-fs.html"]

#header menus
HEADER_MENUS = ["index.html", "about.html", "landscape.html", "travel.html", "monochrome.html", "nature.html", f"{BLOG_NAME}.html"]

#footer links
FOOTER_MENUS = ["index.html", f"{BLOG_NAME}.html", "about.html", "privacy-policy.html"]

#Categories
CATEGORIES = []

#website title
WEB_TITLE = 'Sri Lanka Landscape Photographer: Capture the Beauty of Sri Lanka\'s Landscapes'

KEY_WORDS = [
    "Sri Lanka landscape photography",
    "landscape photography in Sri Lanka",
    "best places for landscape photography in Sri Lanka",
    "top 10 landscape photography spots in Sri Lanka",
    "Sri Lanka photography tour",
    "Sri Lanka landscape photographer",
    "Sri Lanka landscape photography workshops",
    "Sri Lanka landscape photography tips",
    "Sri Lanka landscape photography inspiration",
    "Sri Lanka landscape photography gear"
]
#website footer
WEB_COPYRIGHT = 'Amila Hewagama'
WEB_COPYSITE = 'https://lankascape.com'

#watsapp enable='', off='hidden'
WATSAPP_STATUS = 'hidden'

#watapp number
PHONE_NUMBER = '+94113876680'


#FILE METHODS

def sanitize_title(title):
    sanitized_title = re.sub(r'[^\w\s]', '', title).strip().replace(' ', '-')
    return sanitized_title.lower()

def read_file_content(filename):
    with open(filename, 'r') as f:
        return f.read()

def delete_existing_html_files(blog_data):
    for blog in blog_data:
        title = blog['title']
        sanitized_title = sanitize_title(title)
        if os.path.exists(f"{PUBLIC_DIR}{sanitized_title}.html"):
            os.remove(f"{PUBLIC_DIR}{sanitized_title}.html")

def extract_filename_and_capitalize(input_filename):
    # Get the file name without the extension
    file_name = os.path.splitext(input_filename)[0]
    capitalized_name = file_name.capitalize()
    return capitalized_name

def write_htaccess(filename):
  with open(f"{PUBLIC_DIR}{filename}", "w") as f:
    f.write("""
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ $1.html [L]
</IfModule>
""")

def truncate_content(original_content, max_chars=100):
    content_without_tags = re.sub(r'<.*?>', '', original_content)
    truncated_content = content_without_tags[:max_chars]
    return truncated_content.join('...')

def extract_subjects(text):
    # subjects followed by ":"
    pattern = r"(?<=^|\n)([^:\n]+):"
    matches = re.findall(pattern, text)
    return matches

def replace_subjects_with_h3(text):
    # match subjects followed by ":"
    pattern = r"(?<=^|\n)([^:\n]+):"
    # Replace subjects with <h3> tags
    modified_text = re.sub(pattern, r'<h3>\1</h3>', text)
    return modified_text
	
def add_classes_and_newlines(input_string):
    # patterns to match <p>, <h1>, <h2>, and <h3> tags
    p_tag_pattern = r"<p>(.*?)<\/p>"
    h1_tag_pattern = r"<h1>(.*?)<\/h1>"
    h2_tag_pattern = r"<h2>(.*?)<\/h2>"
    h3_tag_pattern = r"<h3>(.*?)<\/h3>"
    li_tag_pattern = r"<ul>(.*?)<\/ul>"
    # Replace tags 
    replaced_string = re.sub(p_tag_pattern, r'<p class="font-medium text-body-color text-base sm:text-lg lg:text-base xl:text-lg sm:leading-relaxed lg:leading-relaxed xl:leading-relaxed leading-relaxed mb-8">\1</p>', input_string)
    replaced_string = re.sub(h1_tag_pattern, r'<h1 class="font-bold text-black font-xl sm:text-2xl lg:text-xl xl:text-2xl leading-tight sm:leading-tight lg:leading-tight xl:leading-tight mb-10">\1</h1>', replaced_string)
    replaced_string = re.sub(h2_tag_pattern, r'<h2 class="font-bold text-black font-xl sm:text-2xl lg:text-xl xl:text-2xl leading-tight sm:leading-tight lg:leading-tight xl:leading-tight mb-10">\1</h2>', replaced_string)
    replaced_string = re.sub(h3_tag_pattern, r'<h3 class="font-bold text-black font-xl sm:text-2xl lg:text-xl xl:text-2xl leading-tight sm:leading-tight lg:leading-tight xl:leading-tight mb-10">\1</h3>', replaced_string)
    replaced_string = re.sub(li_tag_pattern, r'<ul class="list-disc list-inside text-body-color mb-10">\1</ul>', replaced_string)
    # Add newlines
    final_string = replaced_string.replace('</p>', '</p>\n').replace('</h1>', '</h1>\n').replace('</h2>', '</h2>\n').replace('</h3>', '</h3>\n')

    return final_string

def generate_tag_code(tags):
    html_code = '<div class="">\n'
    for tag in tags:
        tag_class = tag.lower().replace(" ", "-")
        link = f'<a href="javascript:void(0)" class="inline-flex items-center justify-center py-2 px-4 mr-4 mb-2 rounded-sm bg-primary bg-opacity-10 text-body-color hover:bg-opacity-100 hover:text-white transition">\n{tag}\n</a>'
        html_code += link.replace("ERP", tag).replace("erp", tag_class)
    html_code += '</div>'
    return html_code

#BLOG METHODS	
def generate_blog_list_html(blog_data, header_content, footer_content):
    grid_template_file = GRID_TEMPLATE
    grid_template = read_file_content(grid_template_file)

    blog_html = ""
    for blog in blog_data:
        file_link = sanitize_title(blog['title'])
        file_link = (file_link+".html" if HTACCESS==0 else file_link)
        blog_html += grid_template.format(
            image=blog['image'],
            author=blog['author'],
            date=blog['date_post'],
            title=blog['title'],
			file_link=file_link,
			content=truncate_content(blog['content'])
        )
	
    start = "<section class='relative z-10 pt-[100px] overflow-hidden'><div class='container'><div class='border-b border-[#E9ECF8] pb-20'><div class='flex flex-wrap mx-[-16px] justify-center'>"
    end = "</div></div></section>"
    complete_html = f"{header_content}{start}{blog_html}{end}{footer_content}"
    with open(f"{PUBLIC_DIR}{BLOG_NAME}.html", "w") as f:
        f.write(complete_html)
        print(f"file created: {BLOG_NAME}.html")

def generate_blog_detail_html(blog_data, footer_content,header_menus):
    blog_template_file = BLOG_TEMPLATE
    blog_template = read_file_content(blog_template_file)
    header_content_li = read_file_content(HEADER_FILE)
    keywords = ""

    for blog in blog_data:
        title = blog['title']
        sanitize_t = sanitize_title(title)
        html_content = blog_template.format(
            title=title,
            image=blog['image'],
            author=blog['author'],
            date=blog['date_post'],
            tags=generate_tag_code(blog['tags']),
            content=add_classes_and_newlines(blog['content'])
        )
        keywords = ",".join(blog['tags'])
        header_content = header_content_li.format(keywords=keywords,header_menus=header_menus, web_title=title, contact=('contact.html' if HTACCESS==0 else 'contact'))
        complete_html = f"{header_content}{html_content}{footer_content}"
        with open(f"{PUBLIC_DIR}{sanitize_t}.html", "w") as f:
            f.write(complete_html)
            print("blog created: " +f"{sanitize_t}.html")

#CATEGORY METHODS
def generate_blog_category(data, header_content, footer_content, search_input):
    search_input = search_input.lower()
    results = [blog for blog in data['blogs'] if search_input in blog['title'].lower()]

    grid_template_file = GRID_TEMPLATE
    grid_template = read_file_content(grid_template_file)

    blog_html = ""
    for blog in results:
        file_link = sanitize_title(blog['title'])
        file_link = (file_link+".html" if HTACCESS==0 else file_link)
        blog_html += grid_template.format(
            image=blog['image'],
            author=blog['author'],
            date=blog['date_post'],
            title=blog['title'],
            file_link=file_link,
            content=truncate_content(blog['content'])
        )
    
    start = "<section class='relative z-10 pt-[100px] overflow-hidden'><div class='container'><div class='border-b border-[#E9ECF8] pb-20'><div class='flex flex-wrap mx-[-16px] justify-center'>"
    end = "</div></div></section>"
    complete_html = f"{header_content}{start}{blog_html}{end}{footer_content}"
    search_input = sanitize_title(search_input)

    with open(f"{PUBLIC_DIR}{search_input}.html", "w") as f:
        f.write(complete_html)
        print(f"category created: {search_input}.html")

#PAGES METHODS	
def add_header_footer_to_html(file_list, header_content, footer_content):

    for filename in file_list:
        with open(f"{APP_DIR}/{filename}", 'r') as f:
            original_content = f.read()

        complete_html = f"{header_content}{original_content}{footer_content}"

        with open(f"{PUBLIC_DIR}{filename}", 'w') as f:
            f.write(complete_html)
            print("page created: " +filename)

#MENUS METHODS
def generate_menus(file_list):
    menu_template = '''
    <li class="relative group">
        <a href="{filename}" class="menu-scroll text-base text-black group-hover:text-primary py-2 lg:py-6 lg:inline-flex lg:px-0 flex mx-8 lg:mr-0 lg:ml-8 xl:ml-12">
            {name}
        </a>
    </li>
    '''

    menus = []
    for filename in file_list:
        name = filename.split('.')[0].capitalize()
        if name == 'Index':
            name = 'Home'
        menu_item = menu_template.format(filename=(filename if HTACCESS==0 else filename.split('.')[0]), name=name)
        menus.append(menu_item)

    for name in CATEGORIES:
        filename = sanitize_title(name).lower()
        filename = f"{filename}.html"
        menu_item = menu_template.format(filename=(filename if HTACCESS==0 else filename.split('.')[0]), name=name)
        menus.append(menu_item)

    return "\n".join(menus)

def generate_menus_ft(file_list):
    menu_template = '''
    <a href="{filename}" class="text-base text-black hover:text-primary mx-3">{name}</a>
    '''
    menus = []
    for filename in file_list:
        name = filename.split('.')[0].capitalize()
        if name == 'Index':
            name = 'Home'
        menu_item = menu_template.format(filename=(filename if HTACCESS==0 else filename.split('.')[0]), name=name)
        menus.append(menu_item)

    return "\n".join(menus)


#MAIN()
def main():

    #create public dir
    if PUBLIC_DIR != '':
        if not os.path.exists(PUBLIC_DIR):
            os.makedirs(PUBLIC_DIR)

    with open(SOURCE_FILE, "r") as f:
        data = json.load(f)

    header_menus = generate_menus(HEADER_MENUS)
    footer_menus = generate_menus_ft(FOOTER_MENUS)
    profile_menus = ''#read_file_content(PROFILE_MENUS)

    #header_menus RE
    header_menus = f"{header_menus}\n{profile_menus}"

    header_content_li = read_file_content(HEADER_FILE)
    footer_content_li = read_file_content(FOOTER_FILE)

    keywords = ",".join(KEY_WORDS)

    complete_header = header_content_li.format(keywords=keywords,header_menus=header_menus, web_title=WEB_TITLE, contact=('contact.html' if HTACCESS==0 else 'contact'))
    complete_footer = footer_content_li.format(footer_menus=footer_menus, web_copyright=WEB_COPYRIGHT, web_copysite=WEB_COPYSITE, watsapp_status=WATSAPP_STATUS, phone_number=PHONE_NUMBER)
	
    # Delete existing HTML files
    delete_existing_html_files(data['blogs'])

    #blogs
    generate_blog_list_html(data['blogs'], complete_header, complete_footer)
    generate_blog_detail_html(data['blogs'], complete_footer, header_menus)

    #html files
    add_header_footer_to_html(FILE_LIST, complete_header, complete_footer)

    #Categories
    for name in CATEGORIES:
        filename = f"{name}.html"
        generate_blog_category(data, complete_header, complete_footer, name)

    #htaccess check
    if HTACCESS==1:
      write_htaccess(".htaccess")

if __name__ == "__main__":
    main()
