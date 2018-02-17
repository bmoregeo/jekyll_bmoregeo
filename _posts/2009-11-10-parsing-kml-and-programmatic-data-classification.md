---
layout: post
title: "Parsing KML and Programmatic Data Classification"
date: 2009-11-10T10:00:00
categories: ["Uncategorized"]
excerpt: >
 <p>I don’t have any maps to show for this at the moment, but I am pretty excited. Thanks to reading this post by the BJØRN SANDVIK at the Thematic Mapping Blog, I finally got around to creating my own ASKMLesqu function in PHP for MYSQL. If you read anything about exporting database data to KML</p>
---
<p>I don’t have any maps to show for this at the moment, but I am pretty excited.</p>
<p>Thanks to reading <a href='http://blog.thematicmapping.org/2008/03/wkt-to-kml-transformation.html'>this post</a> by the BJØRN SANDVIK at the Thematic Mapping Blog, I finally got around to creating my own ASKMLesqu function in PHP for MYSQL. If you read anything about exporting database data to KML you probably realize how awesome PostgreSQL is and how just ehh MYSQL is. For one, PostgreSQL is supported by most, if not all, of the open source GIS software out there today. It is relatively easy to read and write data from a PostgreSQL database in QGIS or GRASS with little effort. Second of all, PostgreSQL has the ASKML function built in. This function automagically takes a data field stored as WKT and parses it to KML compatible markup.</p>
<p>Unfortunately MYSQL does not support geographic data as well as PostgreSQL does. Fortunately PHP exists and I was able to overcome this hurdle (Though I could have overcome this hurdle a whole lot easier by purchasing a hosting plan with PostgreSQL rather than MYSQL to begin with).</p>
<p>This function checks to see what type of geometry type each record is. This is necessary because MYSQL can store multiple geometry types in the same table in the same field. After checking the geometry type, it outputs the data in KML format. Beware I have only tested this officially with the polygon and multipolygon. I will be testing the others once I get the choropleth stuff working 100%.</p>
<p>In order to make choropleth maps, I first had to figure out how to programmatically classify the data coming over from the MYSQL database. First I had to query the DB and find the Maximum and Minimum values for the requested variable. Then from the URL I am grabbing how many quantiles to classify the data into. The breakValue array will then be used later on when styling the KML.</p>
<p>I am still trying to figure out how to style the choropleth map in the kml markup. I think I will probably use the Color Gradient PHP Class written by hamish to sort out the colors.</p>
<p>So I have been really productive, even if I do not have any pretty maps to show for it!</p>

