# What makes an analysis reproducible?

**The goal of reproducible data analysis is to document and communicate your analysis so that other researchers can easily follow your procedure and replicate it results.**

The list of demands and best practices can seem overwhelming at times, but as [Klein et al. (2018)](https://psyarxiv.com/rtygm/) note, even small steps are helpful, and often reduce effort on part of the original analyst:
> [the adoption of reproducible workflows] can be piecemeal -- each incremental step towards complete transparency adds positive value.

----

## Introductions

* A great introduction to this topic with a focus on psychology is the [**practical guide for transparency in psychological science**](https://psyarxiv.com/rtygm/) by Klein et al. (2018), who also provide extensive [supplemental resources](http://psych-transparency-guide.uni-koeln.de/) with practical tips for reproducible analyses, and propose an exemplary [folder structure](http://psych-transparency-guide.uni-koeln.de/folder-structure.html) for data in [online repositories](../share/open-data/repositories.md).
* Daniel Lakens has written an excellent and very comprehensive step-by-step [**tutorial on computational reproducibility**](https://docs.google.com/document/d/1WvApy4ayQcZaLRpD6bvAqhWncUaPmmRimT016-PrLBk/edit) using `R` and Markdown.

----

## Open-source tools

**The tools we use for analysis should allow colleagues to see what we have done, and re-run or adapt our steps.** Freely available tools that can be picked up by any colleague are often more helpful than proprietary, commercial tools, but either will do. Thankfully, there are several sets of tools to choose from:

### Analysis frameworks

* [JASP](https://jasp-stats.org/) and [Jamovi](https://www.jamovi.org/) are easy-to-use, graphical interfaces for statistical analysis. Both make possible fully reproducible analyses without needing to write code.
* The [`R`](https://cran.rstudio.com/) programming language and the corresponding [RStudio](https://www.rstudio.com/) interface are probably the most common analysis tools in the social sciences.
* [Python](https://www.python.org/) and [Jupyter](https://jupyter.org/) provide an alternative approach.
* [Julia](https://julialang.org/) is a programming language focussed on high-performance numerical computation.

!!! tip "Resources for learning `R`"
    If you are new to `R`, there are several fantastic resources to help you get started:

    * RStudio maintains a [repository of **`R` Tutorials**](https://www.rstudio.com/online-learning/), and Lorne Campbell has put together another list of [resources for learning to use `R`](https://osf.io/ny5bq/).
    * The Software Carpentry offers an [**introduction to `R`** for non-programmers](http://swcarpentry.github.io/r-novice-gapminder/).
    * RStudio's [**`R` Cheatsheets**](https://www.rstudio.com/resources/cheatsheets/) are a fantastic resource for finding `R` commands for any particular purpose.
    * [`R` for Data Science](http://r4ds.had.co.nz/) by Grolemund & Wickham is a more comprehensive, and more advanced, tutorial that covers all aspects of data analysis.

----

## Open and documented data formats

**Like the tools used for analysis, data is most useful if it can be reused by anyone.**

* Text-based data formats such as [comma-seperated values](https://en.wikipedia.org/wiki/Comma-separated_values) are probably the most widely understood format for tabular data. If in doubt, the Library of Congress provides some guidelines around [data formats for long-term archival](https://www.loc.gov/preservation/resources/rfs/data.html).
* Wickham (2014) provides guidelines and examples for creating [**tidy datasets**](https://www.jstatsoft.org/article/view/v059i10).
* It's often helpful to create a **codebook** with further information about your data. The [`codebook` package for `R`](https://rubenarslan.github.io/codebook/) can help you create an overview of you data automatically, and is especially helpful for survey data.

----

## Public code

**As with the above steps, publishing code can seem daunting, but Barnes (2010) makes a compelling argument to [publish your computer code: It is good enough](https://dx.doi.org/10.1038/467753a).** The code that produced them is often a vital part of the results you report, as it documents the precise steps in the analysis. For added transparency, syntax files can be shared alongside data in a [public online repository](../share/open-data/repositories.md).

----

## Further steps

Beyond sharing your code, you can take several additional steps further increase the ease with with fellow researchers (and yourself) can follow and reproduce your analysis:

* Give your files (data, analysis scripts, etc.) [self-explanatory names](http://kbroman.org/dataorg/pages/names.html) or follow a [standardized folder structure](http://psych-transparency-guide.uni-koeln.de/folder-structure.html).
* [**Self-contained projects**](https://www.tidyverse.org/articles/2017/12/workflow-vs-script/) reduce the degree to which a programme is tied to any specific computer, ensuring that analyses can be re-run by others.
* [**Literate programming**](https://en.wikipedia.org/wiki/Literate_programming) is the practice of combining code interwoven with the narrative of the analysis such as explanations and discussions of the intermediate steps. For example, [Notebooks in RStudio](https://rmarkdown.rstudio.com/r_notebooks.html) or [Jupyter](https://jupyter.org) contain not only code, but also the output of every analysis step, and can also contain your commentary. They also produce `HTML` and `PDF` reports that make it possible to inspect all results without re-running the analysis. **Comments** in scripts also facilitate understanding.
* **Consistency** can also help add clarity to code. For added standardization, you might consider adopting [naming conventions in `R`](https://www.r-bloggers.com/consistent-naming-conventions-in-r/), follow a styleguide such as the one proposed in [Advanced `R`](http://adv-r.had.co.nz/Style.html), or the [Google Styleguide](https://google.github.io/styleguide/Rguide.xml), or let a package like [FormatR](https://yihui.name/formatr/) do the work for you.

### Version control

**Version control** systems track changes to code (and other files) over time, documenting the history of a project, and providing backups of earlier versions to fall back on.

!!! info "Version control resources"
    * Bryan (2017) provides an excellent introduction to the most popular such system, `Git`, in the context of research data and `R`, if you have [a moment to talk about version control](https://dx.doi.org/10.1080/00031305.2017.1399928). The author also shares her extensive step-by-step guide to [Happy Git and GitHub for the useR](http://happygitwithr.com/).
    * Vuorre & Curley (2018) provide a tutorial on [curating research assets](https://doi.org/10.1177%2F2515245918754826) with `Git`, tailored specifically to psychology.

### Dependency management

**Your results may depend on the specific versions of the software you used in your analysis** -- both the analysis framework, and the plugins and packages you installed on your computer. Documenting these dependencies, such as the package versions you relied on, helps others to recreate the exact environment that you conducted the analysis in. This helps avoid [works-on-my-machine errors](http://psych-transparency-guide.uni-koeln.de/analytic-reproducibility.html#avoid-works-on-my-machine-errors) that can be extremely difficult to pin down.

!!! info "Dependency management resources"
    **Approaches**

    * In **`R`**, the [packrat package](https://rstudio.github.io/packrat/) stores a snapshot of your package library and allows others to reproduce the exact same state. The [Checkpoint package](https://github.com/RevolutionAnalytics/checkpoint) will reinstall packages available on a specific date. The built-in `sessionInfo()` command lists the used versions of every active package.
    * In **Python**, the [`virtualenv`](https://virtualenv.pypa.io) helps manage environments on a per-project basis. [Conda](https://conda.io) aims to manage dependencies in any language, but is most common in the Python world.
    * **Containers** are the latest addition to the dependency management toolkit. Instead of just recreating the set of installed packages, _containers capture an entire system_, and often contain instructions for automatically setting up the system from scratch. This ensures that every part of the analysis environment can be reproduced exactly, and safely transferred between computers if desired. Thus, an entire analyis can be packaged and (re-)run on almost any computer, including external online services.<br>Containers are probably most useful where dependencies go beyond a single analysis framework and associated packages, for example in the case of complex toolchains.

    **Containers**

    Containers are frequently used in software engineering, and are a very stable and dependable technology that is slowly finding its way into scientific practice. The most common software for managing containers is [Docker](https://docs.docker.com/get-started/).

    * [Green & Clyburne-Sherin (2018)](https://psyarxiv.com/mf82t/) motivate and review containers in the context of reproducible analyses in the social sciences. Their manuscript introduces the commercial [CodeOcean](https://codeocean.com/) service, which can run analysis containers over the internet.
    * The [Singularity](https://singularityware.github.io/) project is building a container system designed specifically to meet the needs of researchers and academic institutions. The project's motivation is to increase the ["mobility of compute"](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) around high-performance computing systems, and provide a central [hub for sharing containers](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0188511).
    * The [Scientific Filesystem](https://sci-f.github.io/) aims to make containers more accessible and transparent.
