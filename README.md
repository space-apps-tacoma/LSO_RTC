# LSO-RTC
> Lunar Surface Operations: Real-Time Collaboration

This project is a response to the 2021 NASA Space Apps Challenge
[Lunar Surface Operations: Real-Time Collaboration](https://2021.spaceappschallenge.org/challenges/statements/lunar-surface-operations-real-time-collaboration/details)

The goal of this challenge is to create an application that can
immediately and seamlessly integrate console log information of
many users (at least 100+ users on the same network). Such an
application could be valuable to real-time mission support and
long-term record keeping of future lunar human spaceflight
missions for the benefit of scientific communities and the public.

Your application should allow:

* Multiple simultaneous users creating their own console logs
* Real-time live editing of logs that are viewable to anyone on the same network
* Users to select which logs to view (on demand)
* A user to see his/her own console intermixed with the logs from others selected, which could be arranged by time, 'entry topic,' author, or other attributes
* Console log metadata that includes (at a minimum) a timestamp for every entry and a text entry (an entry could also include images)
* The ability to input sample type, written information including descriptions, time tags, hardware used, along with upload of supporting files (photo, video, and audio)
* The capability to add future input fields including user name, 'console seat/position,’ or other attributes
* Users to tag/link log entries from other authors to their own logs
* Each user to 'officially approve' his/her log once the user is ready. This action will create a permanent unmodifiable log that becomes the official written record for that user's profile

Your application should prohibit:

* Users from overwriting or deleting other user’s inputs
* Application access from unapproved people
    
----

## Reference


### Real-time collaborative document editing

* Theory
  * Operational Transform | Wikipedia [:link:](https://en.wikipedia.org/wiki/Operational_transformation)

  * Blog
    * Building a real-time collaborative editor [:link:](https://www.mahfuz.info/2021/07/04/collaborative-editor/)
    * [collab](https://github.com/mahfuzsust/collab)

    * [ottypes](https://github.com/ottypes) sketches

  * White papers
    * Achieving Convergence [:link:](http://www.dataluna.com/moca-papers/505.pdf)
    * google scholar [:link:](https://scholar.google.com/scholar?q=%22operational+transform%22&hl=en&as_sdt=0,48)

* Frameworks
  * Node.js
    * derbyjs [:link:](https://derbyjs.com/)  [:octocat:](https://github.com/derbyjs/derby)
    * sharejs [:link:](https://sharejs.org/)  [:octocat:](https://github.com/share)

* Editors
  * ckeditor [:link:](https://ckeditor.com/) [:octocat:](https://github.com/ckeditor/ckeditor5)
  * quill [:link:](https://quilljs.com/) [:octocat:](https://github.com/quilljs)
  * firepad active development ended September 2020.
  * blog
    * open-source-collaborative-text-editors | juretriglav [:link:](https://juretriglav.si/open-source-collaborative-text-editors/)

### Similar missions

* Lunar Reconnaissance Orbiter [LRO](https://lunar.gsfc.nasa.gov/index.html)
  * [Data Resources](https://lunar.gsfc.nasa.gov/resources.html)

### Mission Communication

* Shift Handover Communication [:link:](https://human-factors.arc.nasa.gov/publications/Parke_MER_SurfaceOps_Handovers_05.pdf)

### Dashboard inspiration

* sci-fi-designs-to-inspire [:link:](https://www.sitepoint.com/14-top-sci-fi-designs-to-inspire-your-next-interface/)
* MARS-UI-Screen-Graphics [:link:](https://www.behance.net/gallery/47272469/MARS-UI-Screen-Graphics)
* arwes [:link:](https://arwes.dev/design)
* daedalus [:link:](https://www.behance.net/gallery/47272469/MARS-UI-Screen-Graphics/modules/282048871)
