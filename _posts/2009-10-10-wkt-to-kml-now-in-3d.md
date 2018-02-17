---
layout: post
title: "WKT to KML now in 3d"
date: 2009-10-10T09:00:00
categories: ["Uncategorized"]
excerpt: >
 <p>Alright so I have not exactly tested this with 3d data, but I’m 95% certain it will work. I decided to preg_replace out the commas and spaces instead of preg_replacing the numerical values for lat and lon. This should allow for three values per each point (x,y and z). I am still learning regex, so please pardon the hack. It looks really ugly, but it works.</p><p> </p>
---
<p>Alright so I have not exactly tested this with 3d data, but I’m 95% certain it will work. I decided to preg_replace out the commas and spaces instead of preg_replacing the numerical values for lat and lon. This should allow for three values per each point (x,y and z). I am still learning regex, so please pardon the hack. It looks really ugly, but it works.</p>
<p>In addition I am no longer using If Then case. From this point forward I will be using Switch case. It is easier on the eyes.</p>
<p>Next step: Extrude! Maybe off of M Value?</p>
<p><a href=’http://www.bmoregeo.com/wp-content/uploads/2009/10/wkt2kml_20091009.txt’>wkt 2 kml</a></p>

