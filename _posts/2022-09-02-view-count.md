---
title: "View count is available"
date: 2022-09-02
permalink: /posts/2022-09-02/view-count
categories:
  - Misc
tags:
  - Front-end
  - Github pages
# last_modified_at: 2022-09-01
---

As you can see in the subtitle of this post, as well as the bottom-right corner of the [homepage](https://koohoko.github.io/#busuanzi_container_site_uv), view counts for this site and for individual posts are now available.

Just like the comment function, to have view counts on a static page require external services. We use [不蒜子](http://busuanzi.ibruce.info), with tutorials [here](http://ibruce.info/2015/04/04/busuanzi/). It is quiet easy to use, with only two steps:
  1. Add a js script to every page, like [this](https://github.com/Koohoko/Koohoko.github.io/blob/ec2f88c3d2248744d67f3d535b8a1cd81455f2c7/_includes/analytics.html#L13).
  2. Add a span element to the html to show page counts, like [this](https://github.com/Koohoko/Koohoko.github.io/blob/ec2f88c3d2248744d67f3d535b8a1cd81455f2c7/_layouts/single.html#L57-L59).


Please note that some browsers will prohibit cross-site tracking (e.g. Safari browser) which will cause inaccurate page view counts. This can't be fixed at the website side, instead you have to configure manually following [this](https://www.arcolatheatre.com/disable-prevent-cross-site-tracking/). Some related discussions are available [here](https://stackoverflow.com/questions/62225068/safari-mobile-and-desktop-are-hiding-full-referrer-url-why) and [here](https://jdhao.github.io/2020/10/31/busuanzi_pv_count_error/).
