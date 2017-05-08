Computer Science Rankings
================================

This ranking of top computer science schools is designed to identify institutions and faculty actively engaged in research across a number of areas of computer science. Unlike US News and World Report's approach, which is <a target="_blank" href="http://www.usnews.com/education/best-graduate-schools/articles/science-schools-methodology">exclusively based on surveys</a>, this ranking is entirely metrics-based. It measures the number of publications by faculty that have appeared at the most selective conferences in each area of computer science.

This approach is intended to be difficult to game, since publishing in such conferences is generally difficult: contrast this with other approaches like citation-based metrics, which have been repeatedly shown to be <a target="_blank" href="http://arxiv.org/abs/1212.0638">easy</a> to <a target="_blank" href="http://evaluation.hypotheses.org/files/2010/12/pdf_IkeAntkareISSI.pdf">manipulate</a>. That said, incorporating citations in some form is a long-term goal. <em>This codebase is extensively based on <a target="_blank" href="https://github.com/emeryberger/CSrankings">https://github.com/emeryberger/CSrankings</a>. </em>

---

This repository contains all code and data used to build the computer science rankings website, hosted here:
http://wwwx.cs.unc.edu/~jenkinsr/CSrankings/

### Adding or modifying affiliations

To add or modify a faculty member's affiliation, please modify the
file ```faculty-affiliations.csv``` and issue a pull request. Make
sure that the faculty's name corresponds to their <a href="http://dblp.uni-trier.de/search/">DBLP</a> author entry;
for example, Les Valiant's entry is <a
href="http://dblp.uni-trier.de/pers/hd/v/Valiant:Leslie_G=">```Leslie
G. Valiant , Harvard University```</a>.

### Trying it out at home

The code should run on any generic linux server (these directions are based on the Red Hat 6 machine).
Because of GitHub size limits, to run this site, you will want to download the DBLP
data by running ``make update-dblp`` (note that this will consume
upwards of 1.9GB of memory). To then rebuild the databases, just run
``make``. The server will need a minimum of 2 GB of space.

You will also need to install libxml2-utils (or whatever package
includes xmllint on your distro), python, pypy, npm, typescript, and python-lxml at
a minimum via a command line like:

``apt-get install libxml2-utils, npm, python-lxml; npm install -g typescript``

Confirm pip was installed with python, and use pip to install google, requests, and nameparser.
Clone all code, which is available at https://github.com/rajenkins/CSrankings.
The website can be run by opening index.html located at the root of the CSrankings directory.
A cron job must be setup to run update.sh once a month, in order to update publications in the selected journals and conferences.

Cron code: ``@monthly cd /path/to/CSrankings/ && ./update.sh``

Note: ``./update.sh`` MUST be run inside the same folder where the Makefile resides (which is the case in the above cron command)

There are also basic tests that can be run by navigating to the 'util' folder and executing the test.py file by typing ``python test.py``

### Acknowledgements

Our codebase is an adapation of the codebase provided at <a target="_blank" href="https://github.com/emeryberger/CSrankings">https://github.com/emeryberger/CSrankings</a>, and our project would not be possible without their work.

We would also like to thank Professor Ming C. Lin for commissioning us to do this project, Professor Paul Stotts for keeping us on track throughout development, and John Sopko for helping us to host and update our website.


