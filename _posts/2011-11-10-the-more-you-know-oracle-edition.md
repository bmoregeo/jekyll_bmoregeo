---
layout: post
title: "The More You Know: Oracle Edition"
date: 2011-11-10T10:00:00
categories: ["Uncategorized"]
excerpt: >
 <p>This past week I was working on a project where I compare a feature class to a table and delete the records in the feature class that don’t match.</p><p> </p>
---
<p>This past week I was working on a project where I compare a feature class to a table and delete the records in the feature class that don’t match.</p>
<p>Low and behold I hit an bug/error that set me off for about two hours.</p>
<p>I was generating a feature layer using arcpy.MakeFeatureLayer_Management with a query along the lines of ‘ID in (1,2,3,5…2000)’. This totally works on SQL, FGDB, PGDB, but kept returning null values in Oracle.</p>
<p>Not being a super oracle pro, I was dumbfounded. However it turns out, Oracle has a <a style='color: #5eb80b;text-decoration: none' href='http://stackoverflow.com/questions/400255/how-to-put-more-than-1000-values-into-an-oracle-in-clause'>1000 set limit for these sort of queries</a>. Something to put in the back of your head I guess.</p>

