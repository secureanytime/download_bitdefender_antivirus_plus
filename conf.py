project = 'communities-anywhere'
copyright = '2026'
author = 'Admin'

extensions = [ 'sphinx.ext.autodoc',
               'sphinx.ext.napoleon',
               'sphinx_sitemap',
              ]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Screenshot wala classic white theme

html_baseurl = 'https://communities-anytime-download-bitdefender-antivirus-plus.readthedocs-hosted.com/en/latest/'
sitemap_url_scheme = "{link}"

# conf.py

html_title = "Download Bitdefender Antivirus plus"
html_short_title = "Download Bitdefender Antivirus plus"
html_static_path = ['_static']
html_extra_path = ['_static/google5ffeff63dcb91d99.html']

# Meta Tags Configuration
html_context = {
    'metatags': '''
        <meta name="description" content="Step-by-step guide to the Bitdefender Antivirus Plus download, install, activation, and fixes for common errors. Updated for 2026.">
        <meta name="Download Bitdefender Antivirus plus" content="docs, guide, setup, tutorial">
     
    '''
}
