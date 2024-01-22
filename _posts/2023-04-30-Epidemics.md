---
title: "Book notes: Epidemics, Models and Data using R (Ottar N. Bjørnstad, 2018)"
date: 2023-04-30
permalink: /posts/2023-04-30/epidemics
categories:
  - Book notes
tags:
  - Infectious Disease Modelling
toc: true
last_modified_at: 2023-10-21
---

This post records the notes when I read [*Epidemics, Models and Data using R*](https://link.springer.com/book/10.1007/978-3-319-97487-3) byOttar N. Bjørnstad.

The text in this book is designed to be more of a “practicum in infectious disease dynamics.”

## Introduction

### In-Host Persistence

- “in-host persistence” refers to the ability of a pathogen to persist in a host for a long time, e.g., retroviruses as HIV, latent viruses as herpes viruses, symbionts that are beneficial to the host (viz. commmensals and mutualists) etc.
- Acute infections are those that are cleared by the immune system, e.g., influenza, measles, and chickenpox.
- From an epidemiological point of view, it is important to make the functional—as opposed to taxonomical—classification of pathogens because it allows us to under- stand the differences in age-specific attack rates and contrasting disease dynamics.

### Patterns of Endemicity

- Local persistence fails when a local chain-of-transmission breaks. This can happen for two very different reasons: 
  1. The *transmission bottleneck* is when a pathogen is insufficiently transmissible to sustain a chain of transmission (Note that this is different from the *transmission bottleneck* describing virions passed between individuals); 
  2. at the opposite end of the spectrum is the *susceptible bottleneck* for acute pathogens that are so transmissible that they burn through susceptibles much faster than they are replenished.

- The locally persistent infections can be classified as: 
  1. Stable endemics that show little variation in incidence through time. (e.g. HIV)
  2. Seasonal endemics that show low’ish-level predictable seasonal variation around some mean. (e.g. Cholera)
  3. recurrent epi- demics that may be regular or irregular are characterized by violent epidemic fluc- tuations over time. (e.g. measles)

## SIR




