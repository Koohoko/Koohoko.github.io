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
My name is Haogao Gu, now a postdoctoral fellow at [School of Public Health](https://sph.hku.hk/), the University of Hong Kong. I graduated from [Sun Yat-sen University](https://www.sysu.edu.cn/sysuen/) with a bachelor degree of preventive medicine. I obtained my PhD in infectious diseases in 2020 from [The University of Hong Kong](https://www.hku.hk/) under the supervision of [Prof. Leo Poon](https://sph.hku.hk/en/Biography/Poon-Lit-Man-Leo). 

I study the evolution and epidemiology of virus infections, viral sequence features and virus-host interactions. I am good at bioinformatic and statistical analysis of viral sequencing data, and my research has provided novel insights on both basic virology and applied science on controlling virus transmission. My contribution to this field is reflected in my publication record of <a href='https://scholar.google.com/citations?user=sie-ZJkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> and <a href='https://scholar.google.com/citations?user=sie-ZJkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url_hindex | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>. 

I enjoy solving biological problems with computational methods, I have developed some tools (e.g. [SynMut](https://github.com/Koohoko/SynMut), [GEII](https://leo-poon-lab-geii-scriptsweb-app-pk8r5m.streamlitapp.com/), [fasta_filter](https://github.com/Koohoko/fasta_filter)) for studying virus evolution. I like playing basketball and fishing during my leisure times. 

# Selected Publications
- _Haogao Gu_, Ahmed Abdul Quadeer, Pavithra Krishnan, Lydia Chang, Gigi Liu, Daisy Ng, Samuel Cheng, Tommy Lam, Malik Peiris, Matthew McKay, Leo Poon. [Within-host diversity of SARS-CoV-2 lineages and effect of vaccination.](https://www.researchsquare.com/article/rs-1927944/v1) **Under Review** (2022) 
- _Haogao Gu_<sup>*</sup>, Ruopeng Xie<sup>*</sup>, Dillon Adam<sup>*</sup>, Joseph Tsui<sup>*</sup>, Daniel Chu<sup>*</sup>, Lydia Chang, Sammi Cheuk, Shreya Gurung, Pavithra Krishnan, Daisy Ng, Gigi Liu, Carrie Wan, Samuel Cheng, Kimberly Edwards, Kathy Leung, Joseph Wu, Dominic Tsang, Gabriel Leung, Benjamin Cowling, Malik Peiris, Tommy Lam, Vijaykrishna Dhanasekaran, Leo Poon. [Genomic epidemiology of SARS-CoV-2 under an elimination strategy in Hong Kong.](https://pubmed.ncbi.nlm.nih.gov/35136039/) **NATURE COMMUNICATIONS**, 13, 736 : 1-10. (2022) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:aqlVkmm33-oC'></span></i>
- _Haogao Gu_, Daisy Ng, Gigi Liu, Samuel Cheng, Pavithra Krishnan, Lydia Chang, Sammi Cheuk, Mani Hui, Tommy Lam, Malik Peiris, Leo Poon. [Recombinant BA. 1/BA. 2 SARS-CoV-2 Virus in Arriving Travelers, Hong Kong, February 2022.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9155883/) **EMERGING INFECTIOUS DISEASES**, 28 (6) : 1276. (2022) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:9ZlFYXVOiuMC'></span></i>
- _Haogao Gu_, Pavithra Krishnan, Daisy Ng, Lydia Chang, Gigi Liu, Samuel Cheng, Mani Hui, Mathew Fan, Jacob Wan, Leo Lau, Benjamin Cowling, Malik Peiris, Leo Poon. [Probable Transmission of SARS-CoV-2 Omicron Variant in Quarantine Hotel, Hong Kong, China, November 2021.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8798678/) **EMERGING INFECTIOUS DISEASES**, 28 (2): 460. (2022) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:ULOm3_A8WrAC'></span></i>
- _Haogao Gu_, Daniel KW Chu, Malik Peiris, Leo LM Poon. [Multivariate analyses of codon usage of SARS-CoV-2 and other betacoronaviruses.](https://pubmed.ncbi.nlm.nih.gov/32431949/) **VIRUS EVOLUTION** 6, no. 1: veaa032. (2020) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:Tyk-4Ss8FVUC'></span></i>
- _Haogao Gu_, Rebecca Fan, Di Wang, Leo Poon. [Dinucleotide evolutionary dynamics in influenza A virus.](https://pubmed.ncbi.nlm.nih.gov/31737288/) **VIRUS EVOLUTION** 5, no. 2: vez038. (2019) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:u-x6o8ySG0sC'></span></i>


# CV
[Download full PDF]("../files/CV/CV_haogao.pdf")
<iframe src="/web/viewer.html?file=/files/CV/CV_haogao.pdf#pagemode=none" width="100%" height="800"></iframe>

# News
- **2022-08-17**: Chekc our new preprint on within-host evolution of SARS-CoV-2.
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">We investigated within-host evolution of SARS-CoV-2 using HK deep sequencing data from 2020 to 2022 in this study. Potential lineage-specific and vaccination-specific effects were discussed. <a href="https://t.co/PUamvKKqrR">https://t.co/PUamvKKqrR</a> <a href="https://t.co/DZIHjbz0MT">https://t.co/DZIHjbz0MT</a></p>&mdash; Haogao Gu (@GuHaogao) <a href="https://twitter.com/GuHaogao/status/1559896855705632768?ref_src=twsrc%5Etfw">August 17, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

- **2022-02**: Our paper on molecular epidemiology of the first to the fourth COVID-19 waves in Hong Kong published on NC.
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Glad to learn that our NGS paper for <a href="https://twitter.com/hashtag/COVID19?src=hash&amp;ref_src=twsrc%5Etfw">#COVID19</a> is selected as a featured article for public health. We indeed have learnt a lot from AUGC！<a href="https://t.co/OvCexcMywY">https://t.co/OvCexcMywY</a> <a href="https://t.co/PWyZEjdOQt">pic.twitter.com/PWyZEjdOQt</a></p>&mdash; Leo Poon (@world_epidemic) <a href="https://twitter.com/world_epidemic/status/1497195122127032334?ref_src=twsrc%5Etfw">February 25, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

