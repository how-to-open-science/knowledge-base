title: Contributing

# How can I contribute to this resource?

Wow, thanks for considering a contribution to this knowledge base! You're awesome, and your help is much appreciated.

----

## Suggest a new page

We're always on the lookout for new topics that are useful for researchers trying to improve the reproducibility of their own research and that of our field in general, and we'd be glad to add content.

If you have an idea for a new entry, please reach out to [Felix Henninger](http://felixhenninger.com), ideally by email, but postcards are also welcome. To save you some effort, please be invited to copy-and-paste the following template:

    Hi Felix, dear team,

    I really enjoyed the Open Science Knowledge Base, and I think you
    could make it even better by adding a page on [ topic ]. This would
    extend the section [ section ], and a good question header would be
    [ question? ]. Would you consider adding a page like this?

    (*Optionally:* I've done some searching, and I think [ ] would make good resources
    that are relatively stable and cater to the practical needs of our
    fellow researchers. [ I'm extra-awesome and have summarized their
    main contributions, which are ... ])

    I understand that we're all super-busy and working hard, so feel
    free to take some time if you need to, but I'd really appreciate to
    be able to make a contribution, and I think my colleagues would
    find this information useful, too.

    Thanks for your help, and kind regards. Yours ever awesome,


    -A friendly and smart contributor


## How can I develop content locally?
These instructions are intended for those users on Linux or Unix flavored systems
with a command line. If you are using Windows, the easier option might be to
[open an issue](https://github.com/FelixHenninger/open-science-knowledge-base/issues) or use the contact above to request a change.


### 1. Fork and Clone the Repository on Github
If you want to dig in and contribute directly, you can clone the repository,
check out a new branch, and then develop locally. FIrst, you should fork the
repository to your Github account. If your username is `waffles` after you
fork, you would clone like this:

```bash
$ git clone https://www.github.com/waffles/open-science-knowledge-base
$ cd open-science-knowledge-base
```

### 2. Create a New Branch

At this point, you are on the `master` branch, which is the main branch of the
repository that should be kept in line with the upstream (the primary repository).
In order to cleanly separate your changes, you should first checkout a new branch:

```bash
$ git checkout -b add/my-addition master
```

### 3. Make Changes
Then, make changes to your heart's content! The project uses [mkdocs](https://www.mkdocs.org)
so you should first install it:

```bash
$ pip install mkdocs
```

The theme that we use is [Material](https://squidfunk.github.io/mkdocs-material/) so
you need to install that too.

```bash
$ pip install mkdocs-material
```

and then start a local server to see your changes in action!

```bash
$ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
[I 180628 10:57:20 server:292] Serving on http://127.0.0.1:8000
[I 180628 10:57:20 handlers:59] Start watching changes
[I 180628 10:57:20 handlers:61] Start detecting changes
```

And open up [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the site. As you
edit the local text files, you will see the server rebuild automatically!
If you need more detail or instruction, please see the link provided above.

### 4. Create a Pull Request

When you are ready you can opena [pull request](https://help.github.com/articles/about-pull-requests/) to the primary repository master branch, and discuss your changes with the maintainers. Please be sure to include details about your contribution.
