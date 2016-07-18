from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='gpg-group-chat',
      version='0.1',
      description='Simple encrypted group chats',
      long_description=read('README.md'),
      author='Bah! Hackers',
      author_email='',
      url='https://github.com/bahackers',
      packages=[
          'gpg_group_chat',
          'gpg_group_chat.client',
          'gpg_group_chat.server'
          ],
      install_requires=[],
      entry_points={
          'console_scripts': [
              'gpg-group-chat = app:main'
              ]
          },
      include_package_data=True)
