---
layout: post
title:  Running DymoLabel 7.x without a Dymo Printer
date:   2016-08-29 13:05:03 -0300
category: misc
tags: reblog
---

Updated from a solution found [here][original-post]. Thanks to the original author.

One of the projects I was working on required us to update an application that created ID cards using Dymo printers in order to support other brands of printers. 

However, Dymo labels are created and printed using a XML file with a custom schema, and I couldn't find another program that could open/import it to convert to a saner format.

To add insult to injury, trying to run DymoLabel (the application Dymo provides to design/create labels) or an application that uses the Dymo API without a printer installed fails with an error like *"This program requires a Dymo Printer. "*

Googling around (which saves lives) took me to [this 2013 post][original-post] which provides a workaround:

1. Go to the [Dymo Support][dymo-wayback-machine] and look for the first error at Troubleshoot > Error Messages. Download and run the provided ASINSTALL.EXE. The URL in the original post does not work anymore, though, so we're relying on the [Internet Archive WayBack Machine][wayback-machine] snapshot of it.
2. Add a fake printer manually through Windows' Devices and Printers.


[original-post]: http://windycitytech.blogspot.com.br/2013/06/running-dymo-label-without-dymo-printer.html 
[dymo-wayback-machine]: https://web.archive.org/web/20120216022217/http://global.dymo.com/enGB/Troubleshooting/LabelWriter_320.html
[wayback-machine]: https://archive.org/web/
