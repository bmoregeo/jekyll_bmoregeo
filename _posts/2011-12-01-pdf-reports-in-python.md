---
layout: post
title: "PDF Reports in Python"
date: 2011-12-01T10:00:00
categories: ["Uncategorized"]
excerpt: >
 <p>The past couple weeks at work have been pretty exciting. I’m doing some internal development for one of our GIS Support Teams. Creating Data Development reports is a pretty big part of they job and by pretty big I mean most annoying. These reports showed discrepancies in Primary Key – Foreign Key matches between the GIS data and an external data source.</p>
---
<p>The past couple weeks at work have been pretty exciting. I’m doing some internal development for one of our GIS Support Teams. Creating Data Development reports is a pretty big part of they job and by pretty big I mean most annoying. These reports showed discrepancies in Primary Key – Foreign Key matches between the GIS data and an external data source.</p>
<p>Their current setup is a Microsoft Word Template that they fill in at the end of each data development project. This resulted in some inconsistencies with how each Analyst formatted their report, small grammatical and spelling errors and was time intensive.</p>
<p>I was brought in to help them out by automating some of this process. I decided to utilize the open source version of <a href='http://www.reportlab.com/software/opensource/'>Report Lab </a>to generate a standardized custom report template. This library is AWESOME, but a little difficult to understand. I am probably going to write up a quick tutorial on how I setup my page template.</p>
<p>The end result of the tool is pretty neat. The user opens up a tool in ArcToolbox and throws in a couple tables from before and after their data development and an output pdf location. The tool then runs through, executes a few calculations to determine the quality of the data and outputs it to PDF. Thus taking a couple hours worth of manual work and completing in with a 3 minute script.</p>

