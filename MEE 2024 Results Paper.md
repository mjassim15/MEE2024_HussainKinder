---
abstract: |
  The goal of the Modern Eddington Experiment (MEE2024) is to make the
  most precise measurement ever of the gravitational deflection of
  stellar positions near the Sun during a total solar eclipse using
  ground-based optical images, and by so doing, we seek to demonstrate
  the nature of the 1/R relationship for deflected stars. Fourteen
  observing teams will perform the MEE2024 during the total solar
  eclipse crossing North America on April 8, 2024. Feasibility was shown
  in the 2017 total solar eclipse, with the expectation that the 2024
  results will be orders of magnitude more precise. This is primarily
  due to faster cameras, a longer totality, and multiple data sets. A
  computer program is being developed to semi-automatically complete the
  data analysis. This program will include corrections for optical
  distortion and finding accurate star centroid locations near the Sun.
  This should result in a final deflection curve accurate enough to
  verify Einstein's formula.
affiliation:
- id: 0
  organization: Portland Community College OR
- id: 1
  organization: Dallas, OR
- id: 2
  organization: San Diego, CA
- id: 3
  organization: Angelo State University, TX
article:
  doi: 10.3847/25c2cfeb.3ff37cfa
  elocation-id: 2024i3n002
  issue: 3
  volume: 56
author:
- William A. Dittrich
- Richard Berry
- Donald Bruns
- Kenneth Carrell
bibliography: /tmp/tmp-60N5Ijg6WIE0st.json
copyright:
  link: "https://creativecommons.org/licenses/by/4.0/"
  text: Creative Commons Attribution 4.0 International License
  type: CC-BY
csl: /app/dist/server/server/utils/citations/citeStyles/apa-6th-edition.csl
date:
  day: 02
  month: 03
  year: 2024
journal:
  eissn: 2330-9458
  publisher-name: Bulletin of the AAS
  title: Bulletin of the AAS
link-citations: true
title: Modern Eddington Experiment 2024 (MEE2024)
uri: "https://baas.aas.org/pub/2024i3n002"
---

# **1. Introduction**

In 1919, shortly after Einstein published his Theory of Relativity
([@temp_id_8940402112027483]), Sir Arthur Eddington and his colleague
Frank Dyson performed the first successful measurement of the Einstein
Coefficient ([@{1920RSPTA.220..291D}]) defined as the deflection
magnitude at the Sun's limb, nominally 1.75 arcseconds. They did this by
capturing only seven stars on two glass plates. During the next 100
years, a number of attempts at the "Eddington Experiment" were
undertaken with varying levels of success. These experiments are
detailed in [Figure 1](#n0h5of9srwa) below. Many were not successful
because this experiment is very hard to complete for a variety of
reasons. Decades ago, cumbersome equipment, the need to use glass plates
to capture images, and the need to image the sky months before or after
an eclipse to determine the actual locations of stars were all required.
Errors arose from many factors, including setup and teardown, changing
weather conditions for pre- and post-eclipse imaging, and traveling with
glass plates and processing them properly. The history and more detailed
descriptions of these past experiments are well presented in
von Klüber's paper [@temp_id_26897642182877934].

Their goal was to verify the stellar deflections θ near the Sun, assumed
to be equal to:

$$\theta = \ \frac{4\ G\ M_{\odot}}{R_{\odot \ }c^{2}}\left( \ \frac{1}{R}\  \right) = {1.75}^{"}\left( \ \frac{1}{R}\  \right)$$

where R is equal to the radial distance from the center of the Sun in
units of solar radii. At the limb of the Sun, where R=1, the angular
deflection of a photon is 1.75 arcseconds, which is called the Einstein
Coefficient (EC). The inverse law was assumed to be correct
([@nu4rcxrujj7]; [@nxca451wxgz]; [@nm8mrbd56mn];
[@temp_id_3710522505371445]; [@nopfjqtr77x]) and the experimenter's
goals have only been to measure the EC as accurately as possible.

![Table of
data](https://assets.pubpub.org/s1490zbr/21707884986466.jpeg){#n0h5of9srwa}

Historical Performances of the Eddington Experiment.

The attempt in 1922 solidified the results from 1919 by obtaining more
stellar images, shown in [Figure 2](#nuz2a5twjku). Although having more
data was convincing, there were no stars closer than two solar radii,
and the correct formula could not be demonstrated from the curve.
Subsequent experiments by van Biesbroeck [@temp_id_6516985269194722] and
Jones [@temp_id_85866104350128] had the same problem; few stars close to
the Sun and a wide scatter of deflections for stars at larger radii.
After 1973, there were no known experiments performed for over four
decades.

![](https://assets.pubpub.org/njq7y31u/71707884986467.png){#nuz2a5twjku}

A plot of the results from the 1922 eclipse reproduced from von Klüber
(1960).

In 2017 the era of the Modern Eddington Experiment began, mainly because
of computer-controlled equipment and electronic cameras. Another key
element in the modern experiment is the use of the extremely accurate
stellar positions from the Gaia satellite; taking comparison images
months earlier or later is no longer required. The data processing
procedure is still very complex. Therefore, a secondary goal of this
project is to make the overall experiment accessible for future amateur
astronomers, faculty, and students in upper-level lab courses in the
college curriculums. The creation of a Modern Eddington Experiment Lab
Manual and computer software for station control during data collection
and post eclipse data processing is essential to meet this secondary
goal. In the long course of time, this secondary goal could prove to be
more important to the mission of MEE2024 than the primary goal of
verification of the deflection power law.

In 2015, planning began to repeat this experiment during the total solar
eclipse that crossed the United States in 2017. The equipment set up in
Wyoming, along with the final results, is shown in [Figure
3](#nabcmrc35qq). For this eclipse, two bright stars just happened to be
located about 1.5 R~⊙~ from the Sun, a coincidence that will not be
repeated for decades. This data set was good enough to derive a very
precise Einstein Coefficient of 1.751 arcsec, when the theoretical value
is also 1.751 arcsec. The uncertainty of 3% came from atmospheric
turbulence ([@temp_id_9591699356042425]), after assuming an inverse
power law. Up to the present, every experiment performed with optical
and radio telescopes, both on the ground and satellites assumed the
hyperbolic 1/R power law. To adequately verify the inverse power law,
many additional stellar positions measurements will be necessary,
especially in the region of the corona from R = 1-2.

> ![man with a table and a
> telescope](https://assets.pubpub.org/ew75tba2/21707884986468.png){#nabcmrc35qq}
>
> Telescope setup for experiment for the 2017 total solar eclipse.

The data analysis plan applied to the data displayed in Figure 2 used
the exponent as a variable in a least-squares fit. An analysis of the
Bruns 2017 data ([@temp_id_9591699356042425]) resulted in the formula:

 $\theta = \ \frac{1.96}{R^{1.13}}$

When the exponent was constrained to -1, the result was:

$\theta = \ \frac{1.751}{R}$

a very nice fit to Einstein's theory. Each data was the result of a
single measurement and had no easily defined error associated with it.
The radial distance from the theoretical curve is the only measure of
the error. Individual measured centroids might be analyzed to have an
error proportional to the FWHM and SNR of each point, but that varied
too much, due to the variable solar background, to have much meaning.
Those errors ranged from 0.1 arcsec to 0.01 arcsec. The final curve did
not use a weighting factor based on these individual errors; each point
was weighted equally.

This same procedure will be applied to the 2024 data sets, with the
expectation that the best fit will be close to 1/R and the coefficient
close to 1.75. The residual errors, after subtracting the 1.75/R
baseline, will be examined for possible fits to higher powers. If there
is enough good data to show a good correlation, the results will be
offered to other interested experimental and gravitational experts.

Another Modern Eddington Experiment was performed in Oregon in 2017 by
Berry and Dittrich using similar equipment as the Bruns experiment.
While the results of this experiment were comparable to past experiments
(1.68 arcsec), four students from Portland Community College
participated and became the first students in history to measure the
curvature of space in the optical. The uncertainty caused by plate scale
difficulties was very large, so that the results were not publishable.

![](https://assets.pubpub.org/ddqcx8p8/51707884986468.jpeg){#ne5ct7pf1bp}

A plot showing the historical progression of the measurement of the
deflection coefficient. Modified from Figure 2 of Will (2015).

[Figure 4](#ne5ct7pf1bp) shows the historical experiments in the optical
and the experiments undertaken by single radio telescopes, Very Long
Baseline Interferometry of radio telescopes (VLBI) and the Hipparchus
satellite. This figure is modified from Figure 2 of Will
([@temp_id_9108824612449031]). The result is displayed as A = 1.0 if the
deflection at the limb of the sun is 1.75 arcsec, while the error bars
are shown by size.

In 2024, with exposure times as fast as 100msec with zero readout delay,
the fastest CMOS cameras will allow us to capture stars closer to the
Sun's limb. The larger format cameras are slower but capture stars out
to a larger radius. With 10 telescopes, this will give us 10
final-processed images with the likelihood of measuring thousands of
stars. Deflections of each star may be measured to a 1% accuracy, based
on current tests. The resulting Einstein Coefficient measurement error
may be of order 0.001 arcseconds (0.1%), which would be the most
accurate measurement performed in the optical range. This result has
been added to [Figure 4](#ne5ct7pf1bp) on the right. The predicted
uncertainty is based on acquiring data from 10 telescopes \[10x\], using
more efficient cameras \[8x\], wider fields of view \[2x\] a longer
eclipse \[2x\], and less atmospheric turbulence \[2x\]. This leads to a
fact of sqrt(10x8x2x2x2) = 25x improvement over the 3% error from 2017.
The large range of stars would finally allow a precise calculation of
the deflection power law.

Now, we have put together 14 observing teams of physicists, astronomers,
amateur observers, and students to perform the Modern Eddington
Experiment (MEE2024) during the total solar eclipse crossing North
America on April 8, 2024. This project has two main goals:

-   Demonstrate the inverse power law of the General Theory of
    Relativity when applied to stellar deflections measured near the
    Sun.

-   Produce the best determination of the deflection coefficient of
    stellar positions due to the Sun's gravity using optical images from
    the ground.

Colleges and universities worldwide use an Advanced Lab course in the
senior curriculum for physics/astronomy majors and yet there is
generally no experiment in this curriculum that involves General
Relativity (GR). It is important to have such an experiment for
undergraduates because GR and the curvature of space takes such an
important and popular place in physics and astronomy today. Other
experiments to involve students in GR are complicated and involve
expensive equipment that most schools do not have. The Modern Eddington
Experiment, with our completed lab manual and open-source data
processing software, will facilitate the future performance of the
experiment by student and amateur astronomers during the eclipse in 2027
and beyond.

An exciting aspect of this project is its members. The educational
institutions involved are from around the world and include community
colleges and primarily undergraduate institutions. In addition, we have
advanced amateur astronomers involved. With the benefit of their
experience and expertise in setting up telescopes and acquiring quality
data, our groups expect to succeed with excellent results.

# **2. Data & Methodology**

One limiting factor in the experiment is the atmospheric turbulence that
moves the stars randomly around the image. This can only be reduced by
integrating over a longer period. The 2024 eclipse lasts twice as long
as the 2017 eclipse, and the CMOS cameras have no dead time in the
acquisition process as there was with CCD cameras. The CMOS cameras will
thus integrate the turbulence effects over eight times longer than in
2017. Additionally, the 2024 eclipse occurs higher in altitude above the
horizon, further reducing turbulence. These factors will significantly
reduce the scatter in the measured deflections.

Some telescope-camera combinations also cover a larger field of view, so
stars farther from the Sun can be measured. Hundreds of stars are
expected in the 2024 images, compared to dozens in the 2017 experiment.
The field of view centered on the Sun during totality for the narrow and
wide-angle CMOS cameras is shown with the actual 2024 star field in
[Figure 5](#nm4hwuozkio). Stars are shown with a magnitude range of 4.3
on the bright end and 12.5 on the faint end. Magnitude 11 stars are
likely measurable close to the Sun, and magnitude 13 stars at the edges.

![](https://assets.pubpub.org/jbx2xkou/11707884986469.jpg){#nm4hwuozkio}

The 2024 eclipse field of view (FOV) centered on the Sun during totality
with right ascension (RA) increasing to the left and declination (DEC)
increasing up. The inner box is for a ZWO 1600 CMOS camera giving a 142
x 107 arcminute FOV, and the outer box is a wide-angle ZWO 6200 CMOS
camera with a larger 289 x 193 arcminute FOV. Star colors are
approximations of real star color and are only meant to be
representative.

An initial test of what our results might look like is shown in [Figure
6](#nt4yzb2zrwr), where we have simulated the deflections for the
eclipse field in 2024. The telescope field of view was based on the
Televue NP101 refractor with a 0.8x field flattener and a ZWO 1600 CMOS
camera. This combination gives us a total of 116 stars. We used the
theoretical relationship to determine the deflection for each star and
ran a Monte Carlo simulation to determine how well we can recover both
the deflection constant and the exponent of the power law in different
circumstances. We ran 1,000 randomized simulations by adding a random
Gaussian error to each stellar deflection and then fitting the resulting
points to determine the deflection coefficient and power law exponent.
With a typical individual position error of 0.07 arcseconds, we can
recover both the coefficient and exponent to an accuracy of 5%. This
demonstrates how important it is to recover as many stars as possible
from the eclipse images.

![](https://assets.pubpub.org/vz724344/51707884986469.jpg){#nt4yzb2zrwr}

Simulated 2024 results for one telescope and camera combination.

With the larger format ZWO 6200 CMOS camera we will obtain several times
more stars in the eclipse field. Therefore, we can expect a further
reduction in the errors for both curve fit verification and the
determination of the EC. If, on the other hand, we assume an inverse
power law for the relationship and only fit for the deflection
coefficient, our estimated error from the above simulation drops to 1%,
which would be the best ever determination of the coefficient using
optical ground-based observations of stars during a total eclipse.

The MEE2024 project has now been organized with 14 stations. Since each
one will be set up with different telescopes, cameras, and exposures,
the data sets should exhibit randomness among them. This justifies
combining the results from all of the stations to reduce the data
scatter even more. The final curve in this project should result in an
accurate determination of the correct inverse power law.

## 2.1 Detailed Data Acquisition and Analysis Procedures

To get the best possible final value for the gravitation deflection
coefficient, the detailed data acquisition and data analysis procedures
summarized here will be followed. They are slightly modified from the
manual procedures followed in 2017 that resulted in historically precise
results ([@temp_id_9591699356042425]). In 2024, we expect well over 100
stars surrounding the Sun from each telescope station, the result of
combining thousands of images. These large numbers require new data
analysis software.

The first steps are acquiring the different images and processing them
so that the centroids can be determined. Analyzing those images to
determine the distortion coefficients and the plate constants comes
next. The final step is to determine the gravitational deflection values
for each star. This procedure is presently being organized into a master
software program and will be automated as much as practical. In the
following we will provide more details on each of these steps, and
further details of data acquisition and analysis are presented in Bruns
([@temp_id_9591699356042425]).

### 2.1.1 Image Acquisitions and Processing

Telescope optical distortions should be measured at night, before or
after the eclipse, with as little change in the camera/telescope as
possible. To get the most accurate final numbers re-focusing may be
required, but disassembly should not be done. Longer exposures should be
taken at night for these calibration images; the purpose is to average
over turbulence to reduce centroid noise. These image series should
contain thousands of measurable stars. Commercial software can be used
to obtain the optical distortion coefficients.

The eclipse day imaging must occur in a window slightly less than 4.5
minutes long so the mount and camera should be fully automated.
Nominally, the plate scale calibration fields would be 5 to 10 degrees
distant from the Sun, where the deflections will be very small and
practically uniform across the field. The first field should be imaged
at the start of totality, for approximately 50 seconds. The field
surrounding the Sun is then imaged during the deepest part of totality,
for 160 seconds. The second field is then imaged for the final 50
seconds of totality. These calibration images will give accurate plate
scales, even though the integrated exposure times are relatively short,
because of the large number of stars. Variations in the procedures might
include a set of four images, with the Sun placed in each corner for
60 seconds. For the largest cameras, simply centering the Sun for the
total duration is an option, using stars in the corners for plate scale
calibration.

Prior to determining the centroids, the individual images for each field
should be aligned and stacked into master images. The thousand or more
images will be automatically aligned to produce a master image. The
fields containing the Sun show very few stars prior to additional
processing, but only a few stars far from the Sun are enough to align
the images. The next step is to remove the bright background from the
solar corona so many more stars will be measurable. Early testing showed
that this can be done using a blurred version of the image, but
additional testing is needed with the new software.

### 2.1.2 Centroid Locations and Star Matching

In 2017, centroids were found using three commercial software programs:
MaxIm DL, Astrometrica, and PinPoint. The centroids from each of these
programs had slightly different coordinates, so a comparison of the
centroid results as determined by slightly different centroiding methods
was warranted. The maximum difference between the centroids was
typically less than 0.1 pixel and the standard deviation of the
difference was 0.02 pixels. To reduce the errors for MEE2024,
centroiding will be done in the new data processing software that has
been developed. While creating this new Python program using elements
from the AstroPy library, the program has similar centroiding styles.
The new software has been compared favorably in performance with
Astrometrica and it was built to handle larger images.

### 2.1.3 Capturing stars with Large Deflections

A key component of the goals of MEE2024 is to image stars close to the
limb of the Sun, where the location is less than 2 R~⊙~ and the
deflections are larger than 1 arcsecond. This requires short exposures
to prevent saturating the camera from the Sun's corona. Since the CMOS
cameras download while imaging, exposures as short as 0.1 sec are
possible without losing integrated exposure time. With 160 seconds of
totality dedicated to the images close to the Sun, capturing 1600 images
per station is possible. To get stars even closer to the Sun, some
stations might use 0.025 second exposures, with an integrated exposure
still exceeding 40 seconds. This might show a few bright stars with
large deflections very close to the Sun's limb.

### 2.1.4 Corrections for the Master Centroid List

Once a preliminary list of centroids with matching star coordinates has
been generated, it must be edited to remove bad or potentially bad
centroids. This includes centroids too close to the image borders,
centroids that are abnormally broad or narrow, or centroids that contain
saturated pixels. The centroid list can be plotted to visually search
for any other anomalies. Close double stars might be noted, and those
can be removed to avoid possible errors. An automatic program to search
for all nearest-neighbor combinations, and deleting those within a few
pixels, will be completed.

Corrections to the raw centroid locations must be made by the automated
software, which include the effects of:

1.  Optical Image distortion (typically \<3 arcseconds and varies across
    the field),

2.  Differential atmospheric refraction (typically 2 arcseconds for the
    entire field) which is a result of the Sun's altitude of about 70
    degrees,

3.  Random seeing wobbles (typically 0.5 arcseconds and it random across
    the field) from air turbulence,

4.  Stellar proper motion and parallax (typically \<0.01 arcseconds and
    specific to certain stars), and

5.  Differential relativistic aberration (typically 0.01 arcseconds for
    the entire field) which is the effect of the motion of the earth and
    solar system.

Optical image distortion is corrected by measuring the positions of
stars near the zenith during nighttime calibrations. Differences in the
measured location compared to the perfect telescope give a set of
coefficients up to cubic order in distance from the optical axis. This
can be done before or after the eclipse date, since the coefficients are
related to the design of the optics and should remain stable. A good
observing session will image several star fields near zenith,
integrating for at least one minute to reduce turbulence.

Differential atmospheric refraction, stellar proper motion and parallax,
and relativistic aberration will be corrected by utilizing the US Naval
Observatory NOVAS program. The output of NOVAS corrects the Gaia catalog
star positions to the observation date and for refraction based on the
local weather conditions. This list is the precise apparent location of
where every star appears in the field, to micro-arcsecond precision.

Atmospheric turbulence creates the largest effect on uncertainty even
though optical image distortion is larger in size. These centroids dance
around randomly with a magnitude up to an arcsecond in short exposures
but averaging over even 30 seconds will reduce the variations to the 0.1
arcsecond range. Turbulence is a function of the local topography, local
temperature differences, and location of the high-altitude jet stream.
Since the location of the telescopes for this project are determined by
cloud predictions more than anything else, there is not much that can be
done to reduce this effect except integrate the exposures for as long as
possible.

These corrections provide the measured coordinates of all stellar
positions, which can be compared with the apparent positions from the
NOVAS-corrected list. The resulting deflections and distance from the
center of the Sun are then plotted. With a least-squares fit, the EC and
the power law coefficient are determined. This is the same procedure
that was used to produce the simulated results shown in [Figure
6](#nt4yzb2zrwr). The data from each telescope/camera system will be
evaluated, and weighting the solutions to each data set or telescope
station is an option, with the largest weights attached to those data
sets with the smallest uncertainties. This will result in a final
deflection and power law coefficient from the 2024 eclipse that is more
accurate than any previous optical determination in history. The data
obtained to produce this result will reside in the open-source website
[www.ModernEddingtonExperiment.org.](https://www.ModernEddingtonExperiment.org "null")

# **3. Summary and Relevance to Eclipse Science**

The MEE2024 project is very relevant to eclipse science. As mentioned
above, this experiment can only be accomplished during a total solar
eclipse. This has meant that progress on both the measurement of the
deflection constant, and the nature of the deflection relationship, has
been very slow. There were 60 total solar eclipses in the 20^th^ century
after Einstein's work was published in 1916, and another 14 so far in
the 21^st^ century. Experiments were not possible during all of these 74
total solar eclipses for a multitude of reasons. With typical durations
of several minutes, that means there has only been a grand total of
several hours that this experiment could have been performed since the
prediction in 1916.

The total eclipse in 2024 will be the last to pass through the
continental US for another 20 years. So, the 2024 eclipse event is a
unique opportunity to perform the Eddington Experiment with minimal
travel and huge impact in the US as far as outreach and community
involvement are concerned.

The summary by von Klüber [@temp_id_26897642182877934] is an extensive
and critical look at the history of light-deflection measurements near
the Sun prior to 1960. The difficulties and problems are discussed, and
the conclusion has several points and recommendations on how these
experiments should proceed in the future. In his first point, he notes
that the deflection of stellar positions near the Sun "quite obviously
exists" and follows that up with "the observations are not sufficient to
show decisively whether the deflection really follows the hyperbolic law
predicted by the General Theory of Relativity". He correctly attributes
this deficiency to the small number of stars measured very close to the
Sun. He also mentions that the data can "be represented quite well even
by straight lines" and there were arguments at least as late as 1959
that a straight line fit better represented all the available data
([@temp_id_4957787025496725]).

One may assume, incorrectly in this case, that because these arguments
and observations were made more than half a century ago, the current
state of the field is very different. However, since von Klüber's work,
there have been only two successful measurements of stellar deflections
during a total solar eclipse, one in 1973 ([@temp_id_85866104350128])
and one in 2017 ([@temp_id_9591699356042425]). Neither of these
measurements obtained enough stars to establish the inverse power law
relationship of the stellar deflections, so this remains a crucial point
to be verified, more than a century after the establishment of the
theory.

In his list of important points that needed to be addressed in future
observations of this type, von Klüber mentions better scale values, more
stars in the field, precise guiding, high- quality optics, and multiple
images during the eclipse. Our MEE2024 project and resulting images will
far surpass what von Klüber had in mind when he made these suggestions,
and we will finally be able to verify the inverse power law of stellar
deflections near the Sun, more than 60 years after this paper and more
than 100 years after Einstein first made the prediction. This
verification will also validate the results of the radio telescopes,
VLBI efforts and now the Hipparchus and Gaia satellites -- done with
undergraduate students and amateur astronomers operating the telescope
stations!

# **Appendix: MEE 2024 Participants**

William A. (TOBY) Dittrich. Principal Investigator, Portland Community
College OR

Richard Berry, Co-PI -- Amateur Astronomer Dallas OR

Don Bruns, Co-PI -- Amateur Astronomer San Diego CA

Kenneth Carrell, Co-PI -- Physics Professor, Angelo State Univ. TX

Paul Poncy, Director -- Oregon Observatory, Sun River OR

Cade Freels, Astronomer -- Oregon Observatory, Sun River OR

Doug Smith, Amateur Astronomer - London England

Andrew Smith, Cambridge University

Heather Hill, Physics Professor - Linn Benton Community College

Greg Mulder, Physics Professor - Linn Benton Community College

Daniel Borrero Echeverry, Physics Professor -- Willamette University

Joseph M. Izen,  Professor Emeritus of Physics -- University of Texas
Dallas

Jesse Kinder, Physics Professor -- Oregon Institute of Technology

Greg Kinne, Amateur Astronomer -- TN

Chris Matin, Student -- Portland Community College

Erika Weber, Student -- Portland Community College

Jed Rembold, Student -- Willamette University

Olivia Schutz, Student -- Willamette University

Sam Jeffe, Student -- Willamette University

Maddie Strate, Student -- Willamette University

Anna Hornbeck, Student -- Willamette University

Jared McSorley, Student -- Willamette University

Cesar Delgado, Student -- Willamette University

Jennie Delich, Student -- Willamette University

Bryn Bauer, Student -- Linn Benton Community College

Calvin Rajendram, Student -- Linn Benton Community College

Colin Bradley, Student -- Linn Benton Community College

Eve Kempe, Student -- Linn Benton Community College

Gavin Le, Student -- Linn Benton Community College

Austyn Moon, Student -- Linn Benton Community College

Josue Benitez-Flores, Student -- Linn Benton Community College

Kaleah Webb, Student -- Linn Benton Community College

Luana Fenstemacher, Student -- Linn Benton Community College

Michael Philip Clark, Student -- Linn Benton Community College

Nicole Serrano, Student -- Linn Benton Community College

Rose Smith, Student -- Linn Benton Community College

Sophia Plascencia, Student -- Linn Benton Community College

Tyler Slaght, Student -- Linn Benton Community College

Sara Leathers, Student -- Linn Benton Community College

Raymond Brown, Student -- Angelo State University

Kelsey Castaneda, Student -- Angelo State University

Yoojin Choi, Student -- Angelo State University

Noel Marichalar, Student -- Angelo State University

Isaac Muench, Student -- Angelo State University

Calvin Nash, Student -- Angelo State University

James Obermiller, Student -- Angelo State University

Andrew Tom, Student -- Angelo State University

Garath Vetters, Student -- Angelo State University

Dylan Villafranco, Student -- Angelo State University

Stasha Youngquist, Student -- Angelo State University
