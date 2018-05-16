{
  const el = document.querySelector('[data-md-component="credits"]')
  const repo = 'felixhenninger/open-science-knowledge-base'
  const creditsPrepend = '<small>Curated by</small><div>'
  const creditsAppend = '</div>'

  if (el) {
    // Download contributor data
    fetch(`https://api.github.com/repos/${ repo }/stats/contributors`)
      .then(r => r.json())
      .then(data => data.map(entry => entry.author))
      .then(contributors => {
        // Build footer contents
        el.innerHTML = creditsPrepend + contributors
          .filter(c => c.login !== 'gitbook-bot')
          .map(c => `<a href="${ c.html_url }">
            <img
              src="${ c.avatar_url }"
              class="credits-image"
              alt="${ c.login }"
            >
          </a>`)
          .join('') + creditsAppend
      })
      .then(() => {
        // Show footer
        document.querySelector('.md-footer-credits')
          .style.display = 'block'
      })
  }
}
