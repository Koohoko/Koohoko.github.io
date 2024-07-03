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
My name is Haogao Gu (顾豪高), now a Research Assistant Professor at [School of Public Health, the University of Hong Kong](https://sph.hku.hk/). I graduated from [Sun Yat-sen University](https://www.sysu.edu.cn/sysuen/) with a bachelor degree of preventive medicine. I obtained my PhD in infectious diseases in 2020 from [The University of Hong Kong](https://www.hku.hk/) under the supervision of [Prof. Leo Poon](https://sph.hku.hk/en/Biography/Poon-Lit-Man-Leo). 

I study the evolution and epidemiology of virus infections, viral sequence features and virus-host interactions. I am good at bioinformatic and statistical analysis of viral sequencing data, and my research has provided novel insights on both basic virology and applied science on controlling virus transmission. My contribution to this field is reflected in my publication record of <a href='https://scholar.google.com/citations?user=sie-ZJkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> and <a href='https://scholar.google.com/citations?user=sie-ZJkAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url_hindex | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>. 

I enjoy solving biological problems with computational methods, I have developed some tools (e.g. [SynMut](https://github.com/Koohoko/SynMut), [GEII](https://leo-poon-lab-geii-scriptsweb-app-pk8r5m.streamlitapp.com/), [epitope_diversity](https://github.com/Koohoko/epitope_diversity), [fasta_filter](https://github.com/Koohoko/fasta_filter)) for studying virus evolution. I like playing basketball and fishing during my leisure times. 

# Selected Publications
- _**Haogao Gu**_, Ahmed Abdul Quadeer, Pavithra Krishnan, Lydia Chang, Gigi Liu, Daisy Ng, Samuel Cheng, Tommy Lam, Malik Peiris, Matthew McKay, Leo Poon. [Within-host genetic diversity of SARS-CoV-2 lineages in unvaccinated and vaccinated individuals.](https://www.nature.com/articles/s41467-023-37468-y) **Nature Communications**, 14, 1793 (2023) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:maZDTaKrznsC'></span></i>
- _**Haogao Gu**_<sup>*</sup>, Ruopeng Xie<sup>*</sup>, Dillon Adam<sup>*</sup>, Joseph Tsui<sup>*</sup>, Daniel Chu<sup>*</sup>, Lydia Chang, Sammi Cheuk, Shreya Gurung, Pavithra Krishnan, Daisy Ng, Gigi Liu, Carrie Wan, Samuel Cheng, Kimberly Edwards, Kathy Leung, Joseph Wu, Dominic Tsang, Gabriel Leung, Benjamin Cowling, Malik Peiris, Tommy Lam, Vijaykrishna Dhanasekaran, Leo Poon. [Genomic epidemiology of SARS-CoV-2 under an elimination strategy in Hong Kong.](https://pubmed.ncbi.nlm.nih.gov/35136039/) **Nature Communications**, 13, 736 (2022) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:aqlVkmm33-oC'></span></i>
- _**Haogao Gu**_, Pavithra Krishnan, Daisy Ng, Lydia Chang, Gigi Liu, Samuel Cheng, Mani Hui, Mathew Fan, Jacob Wan, Leo Lau, Benjamin Cowling, Malik Peiris, Leo Poon. [Probable Transmission of SARS-CoV-2 Omicron Variant in Quarantine Hotel, Hong Kong, China, November 2021.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8798678/) **Emerging Infection Diseases**, 28 (2): 460. (2022) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:ULOm3_A8WrAC'></span></i>
- _**Haogao Gu**_, Daniel KW Chu, Lydia DJ Chang, Sammi SY Cheuk, Shreya Gurung, Pavithra Krishnan, Daisy YM Ng, Gigi YZ Liu, Carrie KC Wan, Ruopeng Xie, Samuel SM Cheng, Benjamin J Cowling, Dominic NC Tsang, Malik Peiris, Vijaykrishna Dhanasekaran, Leo LM Poon. [Genetic diversity of SARS-CoV-2 among travelers arriving in Hong Kong.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8462320/) **Emerging Infection Diseases**, 27 (10), 2666. (2021) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:Zph67rFs4hoC'></span></i>
- _**Haogao Gu**_, Daniel KW Chu, Malik Peiris, Leo LM Poon. [Multivariate analyses of codon usage of SARS-CoV-2 and other betacoronaviruses.](https://pubmed.ncbi.nlm.nih.gov/32431949/) **Virus Evolution**, 6, no. 1: veaa032. (2020) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:Tyk-4Ss8FVUC'></span></i>
- _**Haogao Gu**_, Rebecca Fan, Di Wang, Leo Poon. [Dinucleotide evolutionary dynamics in influenza A virus.](https://pubmed.ncbi.nlm.nih.gov/31737288/) **Virus Evolution**, 5, no. 2: vez038. (2019) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:u-x6o8ySG0sC'></span></i>
- Kenrie PY Hui, John CW Ho, Man-chun Cheung, Ka-chun Ng, Rachel HH Ching, Ka-ling Lai, Tonia Tong Kam, _**Haogao Gu**_, Ko-Yung Sit, Michael KY Hsin, Timmy WK Au, Leo LM Poon, Malik Peiris, John M Nicholls, Michael CW Chan. [SARS-CoV-2 Omicron variant replication in human bronchus and lung ex vivo.](https://pubmed.ncbi.nlm.nih.gov/35104836/) **Nature**, 603 (7902), 715-720. (2022) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:qxL8FJ1GzNcC'></span></i>
- Hui-Ling Yen, Thomas HC Sit, Christopher J Brackman, Shirley SY Chuk, _**Haogao Gu**_, Karina WS Tam, Pierra YT Law, Gabriel M Leung, Malik Peiris, Leo LM Poon, Samuel MS Cheng, Lydia DJ Chang, Pavithra Krishnan, Daisy YM Ng, Gigi YZ Liu, Mani MY Hui, Sin Ying Ho, Wen Su, Sin Fun Sia, Ka-Tim Choy, Sammi SY Cheuk, Sylvia PN Lau, Amy WY Tang, Joe CT Koo, Louise Yung. [Transmission of SARS-CoV-2 delta variant (AY. 127) from pet hamsters to humans, leading to onward human-to-human transmission: a case study.](https://pubmed.ncbi.nlm.nih.gov/35279259/) **Lancet**, 399 (10329), 1070-1078. (2022) <i><span class='show_paper_citations' data='sie-ZJkAAAAJ:4DMP91E08xMC'></span></i>

# News
- **2023-04-21** I am awarded the [RGC postdoctoral fellowship](https://www.ugc.edu.hk/eng/rgc/funding_opport/pdfs/) (totalling stipend >1.2 million HKD for 36 months) from the University Grant Committee (Hong Kong)!
- **2021-11-23** As a team member, I got [Outstanding Project Team on COVID-19 Research Awards](https://www.info.gov.hk/gia/general/202111/23/P2021112300465.htm) from the Hong Kong government!

# [CV](/files/CV/CV_haogao.pdf)
<iframe src="/web/viewer.html?file=/files/CV/CV_haogao.pdf#pagemode=none" width="100%" height="860"></iframe>

<hr />
