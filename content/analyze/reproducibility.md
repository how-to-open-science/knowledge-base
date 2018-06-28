title: Analysis

# What makes an analysis replicable?

**The goal of replicable data analysis is to communicate your analytic process in a way that other researchers can easily follow and reproduce your analysis and its results.** A great introduction to this topic with a focus on psychology is the [**practical guide for transparency in psychological science**](https://psyarxiv.com/rtygm/) by Klein et al., who also provide extensive [supplemental resources](http://psych-transparency-guide.uni-koeln.de/) with practical tips for reproducable analyses, and propose an exemplary [folder structure](http://psych-transparency-guide.uni-koeln.de/folder-structure.html) for data in [online repositories](../share/open-data/repositories.md).

The list of demands and best practices can seem overwhelming at times, but as Klein et al. note, even small steps are helpful, and often reduce effort on part of the original analyst:
> [the adoption of reproducible workflows] can be piecemeal -- each incremental step towards complete transparency adds positive value.

----

## Open-source tools

**For maximum reproducibility, freely available tools that can be picked up by any colleague are often more helpful than proprietary, commercial tools.** Thankfully, there are several sets of tools to choose from:

### Scientific Programming 

* The [`R`](https://cran.rstudio.com/) programming language and the corresponding [RStudio](https://www.rstudio.com/) interface.
* [Python](https://www.python.org/) and [Jupyter](https://jupyter.org/) provide an alternative approach.
* [Julia](https://julialang.org/) is a programming language focussed on high-performance numerical computation.
* [JASP](https://jasp-stats.org/) and [Jamovi](https://www.jamovi.org/) are easy-to-use, graphical interfaces for statistical analysis.

!!! tip "Resources for learning `R`"
    If you are new to `R`, there are several fantastic resources to help you get started:

    * RStudio maintains a [repository of **`R` Tutorials**](https://www.rstudio.com/online-learning/), and Lorne Campbell has put together another list of [resources for learning to use `R`](https://osf.io/ny5bq/).
    * The Software Carpentry offers an [**introduction to `R`** for non-programmers](http://swcarpentry.github.io/r-novice-gapminder/).
    * RStudio's [`R` **Cheatsheets**](https://www.rstudio.com/resources/cheatsheets/) are a fantastic resource for finding `R` commands for any particular purpose.
    * [`R` for Data Science](http://r4ds.had.co.nz/) by Grolemund & Wickham is a more comprehensive, and also more advanced, tutorial that covers all aspects of data analysis.

### Containers

> Containers help to ensure that your analysis runs today, and in years to come.

* [Singularity](https://singularityware.github.io/) containers offer a secure means to distribute scientific applications on a shared resource.
* [Docker`](https://docs.docker.com/get-started/) is ideal for building a container intended for local use, or for conversion to Singularity, allowing for both use cases easily.
* [The Experiment Factory](https://expfactory.github.io/) to generate reproducible container based behavioral experiments.
* [The Scientific Filesystem](https://sci-f.github.io/) and it's associated [Container Builder](https://sci-f.github.io/) to easily plug your code into a `build` --> `test` --> `deploy` framework.
* [Container Tools](https://singularityhub.github.io/) for a wide range of open source tools for containers optimized for open science.


!!! tip "Container Resources"
    If you are new to using containers, there are several fantastic resources to help you get started:

    * The preprint [Computational Reproducibility via Containers in Social Psychology](https://psyarxiv.com/mf82t/), is a solid introduction and overview to container technology, and its importance for reproducibility.
    * [Singularity: Scientific containers for mobility of compute](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177459) and [Enhancing reproducibility in scientific computing: Metrics and registry for Singularity containers](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0188511) discusses challenges specific to container technologies on shared resources that are common to academic institutions.
    * [The Scientific Filesystem](https://academic.oup.com/gigascience/article/7/5/giy023/4931737) reviews some of the challenges and offers a solution for creating modular, discoverable container software.


----

## Open and documented data formats

**Like the tools used for analysis, data is most useful if it can be reused by anyone.**

* Text-based data formats such as [comma-seperated values](https://en.wikipedia.org/wiki/Comma-separated_values) are probably the most widely understood format for tabular data. If in doubt, the Library of Congress provides some guidelines around [data formats for long-term archival](https://www.loc.gov/preservation/resources/rfs/data.html).
* Wickham (2014) provides guidelines and examples for creating [**tidy datasets**](https://www.jstatsoft.org/article/view/v059i10).
* It's often helpful to create a **codebook** with further information about your data. The [`codebook` package for `R`](https://rubenarslan.github.io/codebook/) can help you create an overview of you data automatically, and is especially helpful for survey data.

----

## Public code

**As with the above steps, publishing code can seem daunting, but Barnes (2010) makes a compelling argument to [publish your computer code: It is good enough](https://dx.doi.org/10.1038/467753a).** The code that produced them is often a vital part of the results you report, as it documents the precise steps in the analysis. For added transparency, syntax files can be shared alongside data in a [public online repository](../share/open-data/repositories.md).

### Further steps

Beyond sharing your code, you can take several additional steps further increase the ease with with fellow researchers (and yourself) can follow and reproduce your analysis:

* Give your files (data, analysis scripts, etc.) [self-explanatory names](http://kbroman.org/dataorg/pages/names.html) or follow a [standardized folder structure](http://psych-transparency-guide.uni-koeln.de/folder-structure.html).
* [**Self-contained projects**](https://www.tidyverse.org/articles/2017/12/workflow-vs-script/) reduce the degree to which a programme is tied to any specific computer, ensuring that analyses can be re-run by others.
* [**Literate programming**](https://en.wikipedia.org/wiki/Literate_programming) is the practice of combining code interwoven with the narrative of the analysis such as explanations and discussions of the intermediate steps. For example, [Notebooks in RStudio](https://rmarkdown.rstudio.com/r_notebooks.html) or [Jupyter](https://jupyter.org) contain not only code, but also the output of every analysis step, and can also contain your commentary. They also produce `HTML` and `PDF` reports that make it possible to inspect all results without re-running the analysis. **Comments** in scripts also facilitate understanding.
* **Consistency** can also help add clarity to code. For added standardization, you might consider adopting [naming conventions in `R`](https://www.r-bloggers.com/consistent-naming-conventions-in-r/), follow a styleguide such as the one proposed in [Advanced `R`](http://adv-r.had.co.nz/Style.html), or the [Google Styleguide](https://google.github.io/styleguide/Rguide.xml), or let a package like [FormatR](https://yihui.name/formatr/) do the work for you.
* **Documenting dependencies** of your code, such as the package versions you relied on, so that others can reproduce the exact state of every part of your program. This helps avoid [works-on-my-machine errors](http://psych-transparency-guide.uni-koeln.de/analytic-reproducibility.html#avoid-works-on-my-machine-errors) that can be extremely difficult to pin down. In `R`, the [packrat package](https://rstudio.github.io/packrat/) provides a snapshot of your package library, as does the `sessionInfo()` command.
* **Version control** systems track changes to code (and other files) over time, documenting the history of a project, and providing backups of earlier versions to fall back on. Bryan (2017) provides a good introduction to the most popular such system, `Git`, in the context of research data and `R`, if you have [a moment to talk about version control](https://dx.doi.org/10.1080/00031305.2017.1399928). Vuorre & Curley (2018) provide a tutorial on [curating research assets](https://doi.org/10.1177%2F2515245918754826) with `Git`, tailored specifically to psychology.
