---
permalink: /
title: ""
excerpt: ""
layout: home
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}
{% assign url_hindex = gsDataBaseUrl | append: "google-scholar-stats/gs_data_hindex.json" %}

<span class="anchor" id="about-me"></span>
My name is Haogao Gu (顾豪高), now an Associate Research Scientist at [Mailman School of Public Health, Columbia University](https://www.publichealth.columbia.edu/). I received my PhD from the [School of Public Health, The University of Hong Kong](https://sph.hku.hk/). 

I study virus evolution, the epidemiology of viral infections, viral sequence features, and virus-host interactions. I specialize in bioinformatic and statistical analysis of viral sequencing data, and my research has provided novel insights into both basic virology and applied approaches to controlling virus transmission. My contribution to this field is reflected in my publication record of <a href='https://scholar.google.com/citations?user=sie-ZJkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=1a3a34&logoColor=1a3a34&style=flat&label=citations"></a> and <a href='https://scholar.google.com/citations?user=sie-ZJkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url_hindex | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=1a3a34&logoColor=1a3a34&style=flat&label=h-index"></a>. 

I enjoy solving biological problems with computational methods; I have also been developing some tools (check my [Github](https://github.com/Koohoko)) for studying virus evolution. I like playing basketball and hiking during my leisure time. 

## News
- **2026-05-16** I am joining the Mailman School of Public Health, Columbia University as an Associate Research Scientist, my mentor is [Sen Pei](https://senpei-cu.github.io/).
- **2024-12-02** I got the The HKU-Pasteur Fellowship for visiting *Institut Pasteur, Paris* for three months, my mentor is [Sebastian Duchene](https://scholar.google.com.au/citations?user=K7q8WywAAAAJ&hl=en).
- **2023-04-21** I am awarded the [RGC postdoctoral fellowship](https://www.ugc.edu.hk/eng/rgc/funding_opport/pdfs/) (totalling stipend >1.2 million HKD for 36 months) from the University Grant Committee (Hong Kong)!
- **2021-11-23** As a team member, I got [Outstanding Project Team on COVID-19 Research Awards](https://www.info.gov.hk/gia/general/202111/23/P2021112300465.htm) from the Hong Kong government!
- **2020-10-28** I completed my PhD in Infectious Disease at the [School of Public Health, The University of Hong Kong](https://sph.hku.hk/), under the supervision of my PhD advisor, Professor [Leo Poon](https://hub.hku.hk/rp/rp00484).

## [CV](/files/CV/CV_haogao.pdf)
<iframe src="/web/viewer.html?file=/files/CV/CV_haogao.pdf#pagemode=none" width="100%" height="860" title="Curriculum Vitae (PDF viewer)"></iframe>

<hr />

## Recent Posts

{% for post in site.posts limit:5 %}{% include archive-single.html type="list" %}{% endfor %}

[See all posts →](/year-archive/)
