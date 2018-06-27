#!/usr/bin/env python

import os, yaml

# Collect markdown files included in sitemap -----------------------------------

def leaf_nodes(site_tree):
    output = []

    for subtree in site_tree:
        for k, v in subtree.items():
            if type(v) == str:
                output.append(v)
            elif type(v) == list:
                output += leaf_nodes(v)
            else:
                print('encountered weird data type', type(v))

    return output

included_files = []

with open('../mkdocs.yml', 'r') as stream:
    try:
        site_tree = yaml.safe_load(stream)['pages']
        included_files = leaf_nodes(site_tree)
    except yaml.YAMLError as exc:
        print(exc)

# Collect actually present markdown files --------------------------------------

available_files = []

for root, directory, files in os.walk('../content'):
    filtered_files = filter(lambda f: f.endswith('.md'), files)
    file_paths = map(
      lambda f: os.path.relpath(os.path.join(root, f), '../content'), filtered_files
    )
    available_files += file_paths

included_files = set(included_files)
available_files = set(available_files)

if len(included_files - available_files) is not 0:
    print(
      'In sitemap but not directory',
      included_files - available_files
    )

if len(available_files - included_files) is not 0:
    print(
      'In directory but not sitemap',
      available_files - included_files
    )
