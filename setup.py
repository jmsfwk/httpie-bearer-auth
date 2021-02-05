from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-bearer-auth',
    description='Bearer token Auth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    long_description_content_type='text/x-rst',
    version='0.1.0',
    author='James Fenwick',
    author_email='j.fenwick@me.com',
    license='MIT',
    url='https://github.com/jmsfwk/httpie-bearer-auth',
    download_url='https://github.com/jmsfwk/httpie-bearer-auth',
    py_modules=['httpie_bearer_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_bearer_auth = httpie_bearer_auth:BearerAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
