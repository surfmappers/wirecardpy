import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

requires = [i.strip() for i in open('requirements.txt').readlines()]

setuptools.setup(
    name='wirecardpy',
    version='0.6.0',
    description='Python Library to Wirecard (old MOIP in Brazil) API routes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/surfmappers/wirecardpy',
    author='Lucas Alves Limeira',
    author_email='lucas@surfmappers.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)
