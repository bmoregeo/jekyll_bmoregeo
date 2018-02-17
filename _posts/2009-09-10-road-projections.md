---
layout: post
title: "Road Projections"
date: 2009-09-10T09:00:00
categories: ["Uncategorized"]
excerpt: >
 <p>I have officially decided to go on a bit of a hiatus on the park map stuff for a while. I wish I had time to work on that project, submit job applications and work 40+ hours, and keep my sanity. Unfortunately, I do not. However, I did do some pretty cool stuff at work last week.</p><p> </p>
---
<p>I have officially decided to go on a bit of a hiatus on the park map stuff for a while. I wish I had time to work on that project, submit job applications and work 40+ hours, and keep my sanity. Unfortunately, I do not. However, I did do some pretty cool stuff at work last week.</p>
<p>For the past 4 months I have been steadfastly working on digitizing the future road projections for the State of Maryland. It is pretty tedious, but worthwhile. If anything the tedium has given me plenty of time to brain storm how I can do my job more effectively.</p>
<p>Lets just say I really like equations. After reading <a href='http://onlinepubs.trb.org/Onlinepubs/tcrp/tcrp_rpt_74-c.pdf'>TCRP Report 74 Part C</a> I realized the analysis I have been performing could just as easily be performed using a modified version of their equation. I knew this at the outset of my analysis, however I could not formulate how the equation should be constructed. This equation computes road density as a dependent variable of population density and a coefficient.</p>
<p>From page 285: In the developed areas of counties:</p>
<p><code>RoadDens = 0.1510 * PopDens ^0.4314 </code></p>
<p>In the undeveloped areas of counties:</p>
<p><code>RoadDens = 0.3448 * PopDens ^0.3924</code></p>
<p>The data I have at hand is future household projections under the smart growth and current growth model of development, Maryland Property View 2007 (MDPV) data, and the MD SHA centerline road data. The smart growth and current growth model data sets show future developments and points with values for <strong>New Development Acres</strong>,<strong>Number of Units</strong> and <strong>Density</strong>. From this I figured I could easily define an equation to calculate miles of road needed per household. However, my equation also needed to to take into account the density of each point.</p>
<p>My equation was constructed via sampling and a regression analysis. First I began by taking 25 observations of parcels in the MDPV. I recorded the <strong>Number of Units</strong>,<strong>Miles of Road Connecting the Units</strong> and the <strong>Area of Those Units</strong>. From this I could calculate the Units per Road Mile and Units per Square Mile. These values were then fed into a regression analysis in Excel 2008.</p>
<p>The resulting equation is</p>
<p><code>Road Mileage per Household = 15.99 * Household Density +14.01</code></p>
<p>To calculate the total new road mileage for a new development I simply multiplied the Road Mileage per Household by the Number of New Units.</p>
<p><code>Road Mileage = Total Units * (15.99 * Household Density + 14.01)</code></p>
<p>This seams to work out pretty well. Unfortunately I forgot to email myself from work the map showing the results for Maryland. Hopefully I will be able to post this next week when I am back in. Also, I would like to work few some of the flaws in this analysis. The first flaw I can spot immediately is that the new road calculation does not include the distance to present roads.</p>
<p>Later Days,</p>
<p>Christopher Fricke</p>

