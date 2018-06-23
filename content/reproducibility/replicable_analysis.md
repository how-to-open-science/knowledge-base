title: Replicable analyses

# What makes data analysis replicable?

The goal of replicable data analysis is to communicate your analytic process in a way that other researchers can easily comprehend, interpret and replicate your analysis and its results.

To ensure that your analysis can be replicated, it is recommended to use Open Source Software, such as [R](https://cran.rstudio.com/) and [RStudio](https://www.rstudio.com/) or [JASP](https://jasp-stats.org/).

If you are new to R, there are several fantastic resources to help you get started.
* [R for Data Science](http://r4ds.had.co.nz/) by Garrett Grolemund & Hadley Wickham (which also comes as a physical book, if you want to support the authors)
* [Tidy Data](http://vita.had.co.nz/papers/tidy-data.pdf) by Hadley Wickham
* [R Tutorials](https://www.rstudio.com/online-learning/) provided by RStudio
* [Introduction to R for non-programmers](http://swcarpentry.github.io/r-novice-gapminder/)
* Read [this blog post](https://www.tidyverse.org/articles/2017/12/workflow-vs-script/) by Hadley Wickham for some great advice on setting up your R life to maximize effectiveness and reduce frustration
* Don't be ashamed to refer to [R Cheatsheets](https://www.rstudio.com/resources/cheatsheets/) - seriously, everybody needs to look up stuff ~~sometimes~~ all the time!
* Even more resources for learning how to use R can be found [here](https://osf.io/ny5bq)

The syntax file(s) should be accessible in a [public online repository](open-data/repositories.md) and a link to the repository should be [provided in your paper](Link zu Beitrag über Supplements).
It should contain documentation of the preparation and statistical analysis of your data. Ideally, comments add to its comprehensibility.



To make your syntax files easy to understand, there are a few guidelines you can follow:
* Follow [naming conventions in R](https://www.r-bloggers.com/consistent-naming-conventions-in-r/) (by Robin Lovelace)
* Follow these styleguides to improve readability of your code: [Google Styleguide](https://google.github.io/styleguide/Rguide.xml), [Advanced R by Hadley Wickham](http://adv-r.had.co.nz/Style.html) (or check out the [FormatR Package](https://yihui.name/formatr/) to reformat your R code automatically)
* Create a codebook containing further information about your data (check out the [Codebook Package for R](https://rubenarslan.github.io/codebook/))
* Use comments to explain your analyses
* Give your files (data, analysis scripts, ...) self-explaining [names](http://kbroman.org/dataorg/pages/names.html)
* Use [packrat](https://rstudio.github.io/packrat/) to snapshot the state of your package library, so that your code will work on another computer independently from which package versions they have installed (alternatively you can use sessioninfo() to put information about which package versions you used to the end of your file)
* Use [RMarkdown](https://rmarkdown.rstudio.com/index.html) or [R Notebooks]( https://rmarkdown.rstudio.com/r_notebooks.html), which allow you to combine code, output, and your narrative into a single HTML- or PDF-document. [Read more](https://www.r-bloggers.com/why-i-love-r-notebooks-2/) on why R Notebooks are awesome.

If you finally want to make your code citable, this [Github Guide](https://guides.github.com/activities/citable-code/) will tell you how to do that!
