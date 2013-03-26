======
Origin
======

ZCI is an idea to build a better CI system. It is born from frustration with
current state-of-the-art which have advanced and offer great power but still
fail to do the right thing out of the box.

-----------
Inspiration
-----------

ZCI is based on my personal inspiration and experience with two open source
systems: Jenkins and Travis. ZCI is also somehow influenced by my experience as
a LAVA developer.

Jenkins
=======

Jenkins is a versatile CI system that is used in production by many people
24/7. It is a mature system with an active community and an rich ecosystem of
extensions. Jenkins is written in Java and works on most operating systems.

Advantages
----------

* Jenkins can be adopted by any project and configured to do what is required,
  given enough effort.
* Jenkins has a rich set of extensions or plug-ins that add features not
  present in the core. This allows users to satisfy any need, no matter how
  niche it is without affecting the core.
* Properly configured Jenkins instance, with the right set of plug-ins is
  pretty much the state-of-the-art as far as freely available CI systems go
  today.
* Due to large user base there is a lot of documentation, user stories and
  unofficial support available.

Disadvantages
-------------

* Jenkins is hard to set up right for the intended use case of ZCI. Virtually
  everything _can_ be done but requires a lot of research, trial and error, and
  maintenance.
* Jenkins configuration is not a part of the version control system data. It
  requires complex GUIs to configure and maintain. It is not easy to share a
  working configuration with anyone else as a template.
* Jenkins is not something one can run locally with the same set of tests that
  are performed by the *central* repository gateway.
* Jenkins is written in Java which is typically not pre-installed anywhere
  except for Oracle products. Java is annoying to work with due to **Sun**-JDK
  and **Open**-JDK split.

TravisCI
========

Travis is much younger than Jenkins and seems to address many of the
shortcomings that typically detract people from using CI systems.

Advantages
----------

* Travis is very easy to use for many types of software projects. There is
  practically learning curve to start testing. High-quality documentation and
  great examples allow users to configure Travis for their project in minutes.
* Travis is hosted and works for both open source and commercial projects.
  This precludes any configuration of the server-side bits.
* Travis keeps configuration in source code repository. This allows anyone to
  easily see how other projects are tested and learn by example. This also
  removes the necessity for most of the GUI on the side of Travis.
* Travis works by convention and provides many many common features out of the
  box. This is especially useful for web applications that typically may
  require a database, a message queue and many other complex services. Travis
  provides that with literally one line of configuration.
* Travis integrates with github.com and bitbucket.com. This again, works by
  convention as the user can sign-in with the credentials of their *forge* and
  see his repositories instantly.
* Travis tracks merge requests and automatically tests them as soon as code
  hits the forge. This provides very fast iteration cycle and allows users to
  easily merge software with confidence as Travis literally adds comments or
  other markers right to the merge/pull request on the forge.
* Travis sends emails to developers that broke the build without any additional
  configuration. It can extract email addresses from commit messages.
* Travis is open source and can be deployed inside a company if needed.

Disadvantages
-------------

* Travis supports only fixed set of environments and configurations. It either
  fits very well or not at all. It is uncertain if one can somehow define
  additional environments (for example, other architectures, other operating
  systems, custom software packages)
* Travis does not support bzr and launchpad.net so it cannot be used with
  Ubuntu easily (without setting up a repository on github and mirror on
  launchpad).
* Travis is not designed to be deployed internally in a company or on one's
  laptop. It is a large and complex stack of technology without any simple
  installation method.
* Travis has reliability problems as it is a free service used by massive
  number of people. Continuous support depends on the success of the company
  behind the project.
* Travis cannot be used for other tasks such as building documentation, code
  coverage analysis, downloadable packages or installers. All that Travis can
  do is "run something to see if it fails or not"
* Travis cannot be used while off-line.

LAVA
====

LAVA is a project started by Linaro and very much focused on what the
organization needs to be effective at their mission. LAVA is designed to allow
developers to run various external and some internal tests on a diverse
collection of ARM hardware.

LAVA solves the problem of getting software onto the hardware, setting it up
(booting, installation), testing and gathering results back to a designated
database (using JSON documents with strict schema as a transport). The only
LAVA installation that I know about (the official one) is coupled with Jenkins
as LAVA does not handle building software.

Advantages
----------

* LAVA handles the very complex problem of deploying software to ARM bare metal
  or special ARM simulators that is not supported by any standard software
  deployment systems.
* LAVA has provisions for both testing correctness and performance. This is
  provided at the core levels and is a good basis for running performance
  tests.
* LAVA supports Android and Ubuntu natively. This covers the need of virtually
  all non-system-level developers that intend to build services and
  applications on top of existing systems.
* LAVA has a pretty good way to store test results. Neither Travis nor Jenkins
  can really export anything without forcing people to go through their
  database internals. This allows specialized solutions to be built either on
  top of LAVA (as a plug-in to the LAVA web application) or separately, as an
  application that imports or processes test result files.
* LAVA is an integration framework allowing others to plug tests into it with
  various level of difficulty. This is similar to Travis but much more
  powerful.
* LAVA has some initial support for testing on multiple devices at once. This
  is not intended to run large tests in parallel but rather to be able to test
  interactions among networked machines or interactions of a base machine that
  can be measured by a companion device (e.g. power meter, HDMI capture card,
  software-controlled USB/HDMI/SD pass-through device, etc.)
* LAVA allows to test both the software and the hardware, having many features
  that can be used to test performance, correctness of a particular ARM
  platform.

Disadvantages
-------------

* LAVA has virtually no adoption outside of Linaro and organizations and
  companies associated with Linaro somehow.
* LAVA is pretty much for Linaro and whatever the organization needs is what
  LAVA will support. There is no official API stability. This can be a
  disadvantage for developers that wish to build customized solution on top of
  LAVA.
* LAVA does not handle tracking source code or building software. It is
  expected to be coupled with Jenkins. This doubles complexity and maintenance
  cost of the full solution.
