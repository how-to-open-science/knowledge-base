# How can I avoid mistakes during analysis?

[**Everyone makes mistakes during data analysis.**](https://twitter.com/mcxfrank/status/1010254884938047488) Careful checks of the literature consistently that [exact results are difficult to reproduce](https://osf.io/preprints/bitss/39cfb/), and [reporting errors are fairly common](https://doi.org/10.3758/s13428-011-0089-5) (see also [Nuijten et al., 2016](https://dx.doi.org/10.3758/s13428-015-0664-2), below). All of us have very likely made mistakes, and are likely to make more in the future. Open practices help others spot these and correct them; we can work to reduce the incidence of errors.

## Tools

* **Statcheck** automatically checks the consistency of APA-formatted test statistics and _p_ values in manuscripts. It can process `HTML`, `PDF` and `DOC` files directly, but can also check individual test statistics. The [online version](http://statcheck.io/) works without installation; an [`R` package](http://cran.r-project.org/package=statcheck) is also available for local use. <br> Using statcheck, [Nuijten et al. (2016)](https://dx.doi.org/10.3758/s13428-015-0664-2) re-checked over a quarter-million _p_ values spanning almost 30 years of psychological research, and found inconsistent reported results in one in two articles, and qualitative divergences from the reported conclusions in one in eight articles.

!!! info "See also"
    In general, **any practice that increases the transparency of your results is also likely to help you spot room for improvement**. Many more ideas are listed on the [reproducible analysis](./reproducibility.md) page.
